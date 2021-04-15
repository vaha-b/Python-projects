# About the project:
# https://hyperskill.org/projects/157

# Stage description
# https://hyperskill.org/projects/157/stages/821/implement


import json
import urllib

with urllib.request.urlopen(f"http://www.floatrates.com/daily/{input()}.json".lower()) as response:
    data = json.loads(response.read().decode())
    print(data["usd"])
    print(data["eur"])


# OR

import requests

r = requests.get(f'http://www.floatrates.com/daily/{input()}.json').json()

print(r['usd'])
print(r['eur'])
