import requests

url = "http://20.102.90.50:2017/wiki17_abstracts"
payload = {
    "query": "What's the name of the castle that David Gregory inherited?",
    "k": 3
}

try:
    response = requests.get(url, params=payload, timeout=10)
    
    print(f"Status Code: {response.status_code}")
    print("--- RAW PAYLOAD START ---")
    print(response.text)
    print("--- RAW PAYLOAD END ---")
    
    # Check if it parses as JSON
    try:
        data = response.json()
        if "topk" not in data:
            print("\nISSUE FOUND: JSON is valid, but 'topk' key is missing.")
            print(f"Keys present: {list(data.keys())}")
    except Exception:
        print("\nISSUE FOUND: Response is not valid JSON (likely an HTML error page).")

except Exception as e:
    print(f"Request failed: {e}")