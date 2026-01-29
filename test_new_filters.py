import requests

BASE_URL = "https://civitai.com/api/v1/models"

def test_param(name, params):
    print(f"--- Testing {name} ---")
    print(f"Params: {params}")
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        print(f"Status: {response.status_code}")
        print(f"Items count: {len(items)}")
        if len(items) > 0:
            print(f"First item name: {items[0].get('name')}")
    except Exception as e:
        print(f"Error: {e}")

# Checkpoint Type
test_param("Checkpoint Type: Trained", {"limit": 5, "types": "Checkpoint", "checkpointType": "Trained"})
test_param("Checkpoint Type: Merge", {"limit": 5, "types": "Checkpoint", "checkpointType": "Merge"})

# File Format
test_param("Format: SafeTensor", {"limit": 5, "format": "SafeTensor"})
test_param("Format: GGUF", {"limit": 5, "format": "GGUF"})

# Model Status
test_param("Status: Early Access (earlyAccess=true)", {"limit": 5, "earlyAccess": "true"})
test_param("Status: On-site Generation (supportsGeneration=true)", {"limit": 5, "supportsGeneration": "true"})
test_param("Status: Featured (featured=true)", {"limit": 5, "featured": "true"})

# New Types
test_param("Type: DoRA", {"limit": 5, "types": "DoRA"})
test_param("Type: Workflows", {"limit": 5, "types": "Workflows"})
