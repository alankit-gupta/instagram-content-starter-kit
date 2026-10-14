# Publishing handoff

## Confirm the destination

Read connected brands, match the exact Instagram handle, and retain the returned brand ID privately. Never copy a brand ID from someone else's tutorial. Inspect the queue covering the intended date range using the brand's timezone.

## Metricool connector behavior verified during development

The exposed create action accepted `blogId`, an offset-aware `date`, `mediaFiles` and `info`. In that connector, `info` had to be a JSON-encoded string; prose caused a parse error. Local absolute media paths worked in that particular workspace, but do not assume this is portable to other environments. Read the live tool schema.

Illustrative `info` contents (replace placeholders and serialize once):

```json
{
  "text": "YOUR CAPTION",
  "providers": [{"network": "instagram"}],
  "publicationDate": {"dateTime": "FUTURE LOCAL DATE AND TIME", "timezone": "YOUR IANA TIMEZONE"},
  "instagramData": {"type": "POST"},
  "autoPublish": true
}
```

`POST` worked for single images and an ordered five-image carousel; `REEL` worked for an MP4. This is observed connector behavior, not a complete API contract. Check current documentation before adding fields. Alt text was not populated in the initial integration; inspect the returned `mediaAltText` rather than assuming it transferred.

## Verify and reconcile

After writing, verify every queued item's account, timestamp, caption, asset count, format, status and automatic-publishing flag. Retain the remote ID and UUID. The connector's update action can change the numeric ID while retaining the UUID, so use the latest ID.

On timeout, read the queue before retrying. If a scheduled item disappears, check published history or the live profile: disappearance alone is not proof of success. Do not automatically repost when publication status is unknown.

## Limits

Account type, connection method, plan and provider restrictions affect features. The web editor can offer functions that the connector does not expose. Do not collect passwords or extract session cookies as a workaround. Do not imply that the direct Metricool API is included in every plan.

Current references:
- https://help.metricool.com/schedule-and-post-on-instagram-6b6q5
- https://help.metricool.com/how-to-add-audio-to-your-instagram-reels-from-metricool-2o2ks
- https://help.metricool.com/basic-guide-for-api-integration-r97af
