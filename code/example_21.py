"""
Get data from an API and save it to file.
"""

import requests
import pickle 

base_url = "https://api.weather.gov/alerts"

headers = {}

params = {
    "status": "actual",
    "message_type": "alert",
    "limit": 20
}

response = requests.get(url=base_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # preserves data for further examination
    with open("outputs/series.pkl", "wb") as f:
        pickle.dump(data, f)
    print(f"Number of entries: {len(data)}")
else:
    print(f"Error: {response.status_code} - {response.text}")

