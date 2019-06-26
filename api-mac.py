import requests
import json
import re
import http.client
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

API_URL = "https://api.macaddress.io/"

def auth_token():
    #auth = request.headers.get("Authorization", None)
    API_key = 'at_6KQIokfk5IhAe8Q2gdd6Zk7kd10rS'
    return API_key

# Ask input to user
def ask_input():
    mac = input("Enter MAC ")
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        result = CallApi(mac)
        print(result)
    else:
        print('Invalid MAC')


#Call API
def CallApi(mac):
    token_api = auth_token()
    response = requests.get(API_URL+'v1?apiKey='+token_api+'&output=json&search='+mac)
    # mac = '44:38:39:ff:ef:51'
    # Print the status code of the response
    if(response.status_code==200):
        json_str = json.loads(response.content)
        return_val = json_str['vendorDetails']['companyName']
    return return_val

if __name__ == "__main__":
   #call apic from url
   #api-mac.py?get_token = ABC & mac = 44:38:39:ff:ef:51
    token = form.getvalue('get_token')
    mac = form.getvalue('mac')
    ask_input()
    '''if token=='None':
        ask_input()
    else:
        CallApi(mac)'''

'''
print("\n GET example")
conn = http.client.HTTPSConnection("httpbin.org")
conn.request("GET", "/get")
response = conn.getresponse()
data = response.read().decode('utf-8')
print(response.status, response.reason)
print(data)'''
