# About the project:
# https://hyperskill.org/projects/145

# Stage decsription
# https://hyperskill.org/projects/145/stages/783/implement


import requests

r = requests.get(input("Input the URL:\n"))

if r.status_code == 200:
    with open("..stage3/source.html", "wb") as f:
        for i in r.content:
            f.write(bytes(str(i), encoding="utf-8"))
        print("\nContent saved.")
else:
    print(f"\nThe url returned {r.reason}!")
