# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/685/implement


import json

with open("2 Medium\Easy Rider Bus Company\input example 3 - stage 6.json", "r") as json_file:
    json_data = json.load(json_file)

# json_data = json.loads(input())
print("On demand stops test:")
stop_name_list = []
num = 0

for index, data in enumerate(json_data):
    if len(data['stop_type']) == 0:
        stop_name_list.append(data['stop_name'])
        num = index
        continue
    elif num == (index - 1):
        stop_name_list.append(data['stop_name'])

if not stop_name_list:
    print('OK')
else:
    stop_name_list.sort()
    # stop_name_tuple = tuple(stop_name_list)
    print(f"Wrong stop type: {stop_name_list}")
