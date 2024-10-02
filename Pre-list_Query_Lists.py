import requests

# using pre-lists query items
query_params = {"gender": "female", "nat": "de"}
requests.get("https://randomuser.me/api/", params=query_params).json()

query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
requests.get(endpoint, params=query_params).json()
