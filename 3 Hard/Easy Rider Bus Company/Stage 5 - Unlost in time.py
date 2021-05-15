# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/684/implement


import json
from datetime import datetime


json_data = json.loads(input())
print('Arrival time test:')
d_bus_id = {}
trash = []
flag = False

for data in json_data:
    current_time = datetime.strptime(data['a_time'], '%H:%M')

    if data['bus_id'] not in d_bus_id:
        d_bus_id[data['bus_id']] = [current_time]

    elif current_time > d_bus_id[data['bus_id']][-1]:
        d_bus_id[data['bus_id']].append(current_time)

    elif data['bus_id'] not in trash:
        print(
            f'bus_id line {data["bus_id"]}: wrong time on station {data["stop_name"]}')
        trash.append(data['bus_id'])
        flag = True

if not flag:
    print('OK')
