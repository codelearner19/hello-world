import requests

url = "http://192.168.10.80/restconf/api/config/native/ip/route/"

payload = "{ \"ned:route\": {\r\n    \"ip-route-interface-forwarding-list\": [\r\n      { \"prefix\": \"216.48.1.0\",\r\n        \"mask\": \"255.255.255.0\",\r\n        \"fwd-list\": [ { \"fwd\": \"10.1.1.1\" } ]\r\n      }\r\n    ]\r\n  }\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
