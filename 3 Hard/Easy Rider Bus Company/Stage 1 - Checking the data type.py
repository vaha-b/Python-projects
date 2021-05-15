# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/680/implement

import json

json_data = json.loads(input())

bus_id_error = 0
stop_id_error = 0
stop_name_error = 0
next_stop_error = 0
stop_type_error = 0
a_time_error = 0

for a in json_data:
    if not isinstance(a["bus_id"], int):
        bus_id_error += 1
    if not isinstance(a["stop_id"], int):
        stop_id_error += 1
    if str(a["stop_name"]) == "" or not isinstance(a["stop_name"], str):
        stop_name_error += 1
    if not isinstance(a["next_stop"], int):
        next_stop_error += 1
    if isinstance(a["stop_type"], int) or isinstance(a["stop_type"], float) or len(a["stop_type"]) >= 2:
        stop_type_error += 1
    if ":" not in str(a["a_time"]):
        a_time_error += 1


error = bus_id_error + stop_id_error + stop_name_error + \
    next_stop_error + stop_type_error + a_time_error

print(f"Type and required field validation {error}", +
      "error:\n" if error == 1 else "errors:\n")
print("bus_id:", bus_id_error)
print("stop_id:", stop_id_error)
print("stop_name:", stop_name_error)
print("next_stop:", next_stop_error)
print("stop_type:", stop_type_error)
print("a_time:", a_time_error)
