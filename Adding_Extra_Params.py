import requests

# adding extra params with &
requests.get("https://randomuser.me/api/?gender=male&nat=de").json()  # for dutch males
