# Implementation Plan - Navigation Restructure & Library Page

## Goal Description
Restructure the navigation bar to prioritize Civitai browsing and local library management.
1. Rename "Models" to "Civitai".
2. Remove "Creators".
3. Add "Models" link pointing to a new `/library` page.
4. Create the `/library` page to list downloaded models with filtering capabilities.

## Proposed Changes

### Navigation (`app/templates/base.html`)
- [MODIFY] Rename "Models" dropdown to "Civitai".
- [DELETE] Remove "Creators" link.
- [NEW] Add "Models" link pointing to `{{ url_for('main.library') }}`.

### Routes (`app/routes.py`)
- [NEW] Add `/library` route.
    - Query `Download` model.
    - Filter by `type` query parameter.
    - Pass `models` and `types` to template.
- [NEW] Add `/files/<path:filename>` route to serve local files (images) from configured directories.

### Templates
- [NEW] `app/templates/library.html`
    - Extend `base.html`.
    - Sidebar with model types (derived from DB).
    - Grid of model cards (Image, Name, Type, Version).
    - Link to existing model detail page (or new local detail page? User said "link to a page that has all the models...").
    - *Assumption*: Clicking a model should go to the API-backed detail page for now, as we have the ID.

## Verification Plan
### Manual Verification
- Click "Civitai" -> Verify it goes to existing models page.
- Click "Models" -> Verify it goes to new Library page.
- Verify "Creators" is gone.
- On Library page:
    - Verify downloaded models are listed.
    - Verify images load (via new file serving route).
    - Verify filtering by type works.
