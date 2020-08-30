import requests

# TODO: create a basic request for data
#resp = requests.get("http://httpbin.org/xml")
#print(resp.status_code)
#print(resp.text)

# TODO: create a request using parameters
#args = {"key1": 1, "key2": "two", "key3": False}
#resp = requests.get("http://httpbin.org/get", params=args)
#print(resp.text)
#print(resp.url)

# TODO: create a request using post
#resp = requests.post("http://httpbin.org/post", data={"key": "value"})
#print(resp.text)

# TODO: create a request using custom headers
heads = {"my-custom-header": "My custom header"}
resp = requests.get("http://httpbin.org/get", headers=heads)
print(resp.text)