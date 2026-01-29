# Walkthrough - Download Manager & Library Scanner

## Completed Tasks

### 1. Download Manager (`app/download_manager.py`)
- Implemented a singleton `DownloadManager` class.
- **Queue**: Handles multiple download requests sequentially.
- **Worker Thread**: Processes tasks in the background without blocking the main thread.
- **Progress Tracking**: Maintains state (`queued`, `downloading`, `completed`, `failed`) and progress percentage.
- **History**: Keeps track of recent tasks to display completion/failure status.
- **Logging**: Added debug logs to trace worker execution.
- **Cleanup**: Automatically removes database entries for models that are no longer found on disk after a full library scan.

### 2. Library Scanner (`app/scanner.py`) [NEW]
- Implemented `scan_directory` function to:
    - Walk through configured directories.
    - Identify model files by extension (`.safetensors`, `.ckpt`, etc.).
    - Calculate SHA256 hash for unidentified files.
    - Look up model version via Civitai API using the hash.
    - Download missing companion files (Metadata JSON, Preview Image).
    - Register/Update the model in the database.
    - Return a list of found model IDs for cleanup logic.
- Integrated into `DownloadManager` as a `scan` task type.

### 3. Downloader Updates (`app/downloader.py`)
- Modified `download_file` and `download_model` to accept a `progress_callback`.
- **Authorization**: Updated `download_file` to accept and use `api_key` in request headers, fixing 401 errors for protected downloads.
- Calculates and reports download percentage during file streaming.

### 4. Backend Integration (`app/routes.py`)
- Initialized `DownloadManager` on app startup.
- Updated `/download` route to add tasks to the manager's queue.
- Added `/settings/scan` route to trigger the library scan.
- Added `/api/downloads/status` endpoint for frontend polling.
- Injected `downloaded_models` into templates via a context processor.
- **Library Route**: Added `/library` to list downloaded models.
- **File Serving**: Added `/files/<path:filename>` to serve local images.

### 5. Frontend - Status Indicators & UI
- **Models List (`models.html`)**: Added "Downloaded" (Green) and "Update" (Yellow) badges.
- **Model Detail (`model_detail.html`)**: Added similar badges next to the NSFW indicator.
- **Settings (`settings.html`)**: Added "Scan Library" button to trigger the scan.
- **Persistent Progress (`base.html`)**:
    - Added a fixed-position progress container.
    - Implemented JavaScript polling (`setInterval`) to fetch status.
    - Displays current task (download or scan), queue count, and recent failures.
    - **Scan Feedback**: Shows "Scanning Library..." and "Scan Failed" appropriately.
- **Navigation**:
    - Renamed "Models" to "Civitai".
    - Removed "Creators".
    - Added "Models" link pointing to `/library`.
- **Library Page (`library.html`)**:
    - Lists all downloaded models.
    - Sidebar filter by model type.
    - Displays local preview images.

## Verification Results

### Automated Verification
- Ran `test_queue_fix.py` which confirmed queue logic and history tracking.
- Ran `test_auth.py` which confirmed that `download_file` correctly sends the `Authorization` header.
- Ran `test_scanner.py` which confirmed correct scanning and identification.
- Ran `test_cleanup.py` which confirmed that models missing from disk are removed from the database after a scan.
- Ran `debug_images.py` which confirmed that `image_path` property works and files exist on disk.

### Manual Verification Steps
1. **Queue**: Click download on multiple models. Verify "X queued" appears in the progress box.
2. **Scan**: Go to Settings -> Scan Library. Verify the progress bar shows "Scanning Library..." and updates as it processes files.
3. **Cleanup**: Delete a model file from your disk. Run "Scan Library". Verify the model is no longer marked as "Downloaded" in the UI.
4. **Indicators**:
    - After download/scan completes, refresh the page.
    - Verify the Green "Downloaded" badge appears.
5. **Library**:
    - Click "Models" in nav.
    - Verify images load correctly.
    - Verify filtering by type works.
