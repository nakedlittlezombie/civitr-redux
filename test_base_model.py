import requests

BASE_URL = "https://civitai.com/api/v1/models"

def test_base_model(name, params):
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
        else:
            print("No items returned.")
    except Exception as e:
        print(f"Error: {e}")

# Test 1: No baseModels param (Control)
test_base_model("No baseModels param", {"limit": 5})

# Test 2: Empty baseModels param
test_base_model("Empty baseModels param", {"limit": 5, "baseModels": ""})

# Test 3: Valid baseModels param
test_base_model("Valid baseModels param", {"limit": 5, "baseModels": "SD 1.5"})
