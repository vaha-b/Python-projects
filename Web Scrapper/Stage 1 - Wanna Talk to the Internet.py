# About the project:
# https://hyperskill.org/projects/145?track=2

# Stage description
# https://hyperskill.org/projects/145/stages/781/implement

import requests
import json

# r = requests.get("http://api.quotable.io/quotes/-CzNrWMGIg8V") terminal uses link like this one as an input
r = requests.get(input("Input the URL:\n"))
j = json.loads(r.content)
j_values_list = [*j.values()]

if r.status_code == 200:
    for i in j_values_list:
        # checks if string(i) is a mixed(upper and lower) case
        if type(i) == str and not i.islower() and not i.isupper():
            print(i)
    else:
        print("\nInvalid quote resource!")

else:
    print("\nInvalid quote resource!")
