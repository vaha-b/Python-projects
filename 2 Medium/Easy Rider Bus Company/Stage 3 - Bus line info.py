# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/682/implement

import json
import re

json_data = json.loads(input())

stop_id_128 = 0
stop_id_256 = 0
stop_id_512 = 0
stop_id_1024 = 0

for data in json_data:
    if re.match("128", str(data["bus_id"])) and isinstance(data["bus_id"], int):
        stop_id_128 += 1
    if re.match("256", str(data["bus_id"])) and isinstance(data["bus_id"], int):
        stop_id_256 += 1
    if re.match("512", str(data["bus_id"])) and isinstance(data["bus_id"], int):
        stop_id_512 += 1
    if re.match("1024", str(data["bus_id"])) and isinstance(data["bus_id"], int):
        stop_id_1024 += 1

print(f"Line names and number of stops:")
print(f"bus_id: 128, stops: {stop_id_128}")
print(f"bus_id: 256, stops: {stop_id_256}")
print(f"bus_id: 512, stops: {stop_id_512}")
print(f"bus_id: 1024, stops: {stop_id_1024}")
