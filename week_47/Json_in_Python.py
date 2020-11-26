import urllib.request
import json

url = "https://api.github.com/orgs/python-elective-fall-2019/repos"

data = urllib.request.urlopen(url).read().decode()

# Parse json object
obj = json.loads(data)

# Output some object attributes
print(obj)
