import requests
r = requests.get('www.google.com')

print(r.status_code)