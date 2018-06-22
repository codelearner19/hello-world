import requests
import json

url = "http://192.168.10.100/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t\t}\n\t\t}\n\t}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_respone = json.loads(response.text)
print(response.text)
print(json_respone)()
