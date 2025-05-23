import requests

url="https://www.googleapis.com/customsearch/v1"
# url="https://www.googleapis.com/customsearch/v1?key=.......&q=Model Context Protocol MCP"


params = {
    "key":"",
    "cx":"",
    "q":"Model Context Protocol MCP",
}


response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
