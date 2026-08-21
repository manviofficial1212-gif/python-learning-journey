import requests

response = requests.get("https://example.com", verify=False)

print(response.status_code)


# 200 → Success 
# 404 → Page not found 
# 500 → Server error 
# 403 → Access forbidden 