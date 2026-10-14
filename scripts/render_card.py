"""Render an editable SVG card. No publishing or network access."""
import argparse
import html
import json
from pathlib import Path
import re
import textwrap


def render(brand, post):
    colors = [brand.get('background', '#F7EFE5'), brand.get('foreground', '#642E3A')]
    if not all(re.fullmatch(r'#[0-9a-fA-F]{6}', c) for c in colors):
        raise ValueError('Colors must be six-digit hex values')
    title = textwrap.wrap(post['title'], 23)
    body = textwrap.wrap(post.get('body', ''), 38)
    handle = brand['handle']
    if not title or len(title) > 4 or len(body) > 5 or len(handle) > 40:
        raise ValueError('Copy too long for this layout; shorten and inspect the export')
    bg, fg = colors
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350"><rect width="1080" height="1350" fill="{bg}"/><g fill="{fg}" font-family="Arial, sans-serif">']
    y = 430
    for line in title:
        lines.append(f'<text x="110" y="{y}" font-size="64" font-weight="bold">{html.escape(line)}</text>')
        y += 82
    y += 50
    for line in body:
        lines.append(f'<text x="110" y="{y}" font-size="36">{html.escape(line)}</text>')
        y += 52
    lines.append(f'<text x="110" y="1230" font-size="25">{html.escape(handle)}</text></g></svg>')
    return '\n'.join(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('brand', type=Path)
    parser.add_argument('post', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    svg = render(json.loads(args.brand.read_text()), json.loads(args.post.read_text()))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(svg)
    print(args.out)
