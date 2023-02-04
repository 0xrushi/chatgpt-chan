import requests
import json

reqUrl = "127.0.0.1:8088/?prompt=panda eating ice cream"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

response = requests.request("GET", reqUrl,  headers=headersList)

print(response.text)