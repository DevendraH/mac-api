import requests
import json
mac = input("Enter MAC ")
#mac = '44:38:39:ff:ef:51'
PARAMS = {'mac':mac}
response = requests.get("https://api.macaddress.io/v1?apiKey=at_6KQIokfk5IhAe8Q2gdd6Zk7kd10rS&output=json&search="+mac)
# Print the status code of the response.
json_str = json.loads(response.content)
print(json_str['vendorDetails']['companyName'])