"""Check local post inputs; this does not prove platform acceptance."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


def check(post, base, now=None):
    errors = []
    caption = post.get('caption', '')
    if not isinstance(caption, str) or not caption.strip() or 'REPLACE_WITH' in caption:
        errors.append('Supply a real caption')
    if post.get('format') not in {'POST', 'REEL', 'STORY'}:
        errors.append('Format must be POST, REEL or STORY')
    try:
        when = datetime.fromisoformat(post['publish_at'].replace('Z', '+00:00'))
        if when.utcoffset() is None or when <= (now or datetime.now(timezone.utc)):
            errors.append('Publish time must be future and include a UTC offset')
    except (KeyError, TypeError, ValueError, AttributeError):
        errors.append('Supply a valid ISO publish_at value')
    media = post.get('media')
    if not isinstance(media, list) or not media:
        errors.append('Supply a nonempty list of media paths')
    else:
        for item in media:
            if not isinstance(item, str):
                errors.append('Media paths must be strings'); continue
            path = base / item
            if not path.is_file():
                errors.append(f'Missing media: {item}')
            if path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.mp4', '.mov'}:
                errors.append(f'Export to a supported upload format: {item}')
        if post.get('format') == 'REEL' and (len(media) != 1 or not isinstance(media[0], str) or Path(media[0]).suffix.lower() not in {'.mp4', '.mov'}):
            errors.append('Reel requires exactly one video')
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('post', type=Path)
    args = parser.parse_args()
    errors = check(json.loads(args.post.read_text()), args.post.resolve().parent)
    print('\n'.join(errors) if errors else 'Local inputs pass. Inspect media and verify provider limits before scheduling.')
    raise SystemExit(bool(errors))
