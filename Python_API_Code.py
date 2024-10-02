# from python console
import requests

# query parameter
requests.get("https://randomuser.me/api/?gender=female").json()

# can add extra params with &
requests.get("https://randomuser.me/api/?gender=male&nat=de").json()  # for dutch males
print(response)

# to pre-list query items
query_params = {"gender": "female", "nat": "de"}
requests.get("https://randomuser.me/api/", params=query_params).json()

query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
requests.get(endpoint, params=query_params).json()
