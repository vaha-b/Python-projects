# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/683/implement

import json
from collections import defaultdict

data_json = json.loads(input())
bus_ends = defaultdict(int)
start_stops = []
finish_stops = []
count_stops = {}
transfer_stops = []

for i in data_json:
    if i['stop_type'] == 'S':
        stop_end = bus_ends.get(i['bus_id'], {"Start": None, "Stop": None})
        stop_end['Start'] = i['stop_name']
        bus_ends[i['bus_id']] = stop_end
        if i['stop_name'] not in start_stops:
            start_stops.append(i['stop_name'])
    if i['stop_type'] == 'F':
        stop_end = bus_ends.get(i['bus_id'], {"Start": None, "Stop": None})
        stop_end['Stop'] = i['stop_name']
        bus_ends[i['bus_id']] = stop_end
        if i['stop_name'] not in finish_stops:
            finish_stops.append(i['stop_name'])
    count_stops[i['stop_name']] = count_stops.setdefault(i['stop_name'], 0) + 1

for key, value in bus_ends.items():
    if value['Start'] is None or value['Stop'] is None:
        print(f'There is no start or end stop for the line: {key}.')
        exit()

for key, value in count_stops.items():
    if value > 1:
        transfer_stops.append(key)

print('Start stops:', len(start_stops), sorted(start_stops))
print('Transfer stops:', len(transfer_stops), sorted(transfer_stops))
print('Finish stops:', len(finish_stops), sorted(finish_stops))
