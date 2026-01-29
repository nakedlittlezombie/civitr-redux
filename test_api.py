import requests
import json

BASE_URL = "https://civitai.com/api/v1/models"

def test_params(name, params):
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
        
        # Check metadata if available
        metadata = data.get("metadata", {})
        print(f"Metadata: {metadata}")
        return items
    except Exception as e:
        print(f"Error: {e}")
        return []

# Test 1: Limit 0 (for base models)
test_params("Limit 0", {"limit": 0})

# Test 2: Sort 'Highest Rated' (with space)
test_params("Sort 'Highest Rated'", {"limit": 5, "sort": "Highest Rated"})

# Test 3: Sort 'HighestRated' (no space)
test_params("Sort 'HighestRated'", {"limit": 5, "sort": "HighestRated"})

# Test 4: Sort 'Most Downloaded'
test_params("Sort 'Most Downloaded'", {"limit": 5, "sort": "Most Downloaded"})

# Test 5: Sort 'MostDownloaded'
test_params("Sort 'MostDownloaded'", {"limit": 5, "sort": "MostDownloaded"})

# Test 6: Type 'LORA'
test_params("Type 'LORA'", {"limit": 5, "types": "LORA"}) # Note: API docs said 'types' in example but query param list said 'type'? Let's check.
# Actually docs said: `types=TextualInversion` in the example. But the param list had `(OPTIONAL)` blocks.
# Let's try 'type' vs 'types'.
test_params("Type 'LORA' (param=type)", {"limit": 5, "type": "LORA"})
test_params("Type 'LORA' (param=types)", {"limit": 5, "types": "LORA"})

# Test 7: Period 'AllTime'
test_params("Period 'AllTime'", {"limit": 5, "period": "AllTime"})
