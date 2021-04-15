# About the project:
# https://hyperskill.org/projects/128?track=2

# Stage description
# https://hyperskill.org/projects/128/stages/681/implement

import json
import re

json_data = json.loads(input())

bus_id_error = 0
stop_id_error = 0
stop_name_error = 0
next_stop_error = 0
stop_type_error = 0
a_time_error = 0

for a in json_data:
    if not re.match("(128|256|512)", str(a["bus_id"])) and not isinstance(a["bus_id"], int):
        bus_id_error += 1
    if not isinstance(a["stop_id"], int):
        stop_id_error += 1
    if str(a["stop_name"]) == "" or not re.match("([A-Z][a-z ]*){1,} (Avenue|Boulevard|Road|Street)$", a["stop_name"]):
        stop_name_error += 1
    if not re.match("\d", str(a["next_stop"])) and not isinstance(a["next_stop"], int):
        next_stop_error += 1
    if a[stop_type_error] not in not in ["F", "O", "S", ""]:
        stop_type_error += 1
    if not re.match("(0|1|2)\d:[0-5]\d$", a["a_time"]):
        a_time_error += 1

error = bus_id_error + stop_id_error + stop_name_error + \
    next_stop_error + stop_type_error + a_time_error

print(f"Type and required field validation {error}", +
      "error:" if error == 1 else "errors:")
print("bus_id:", bus_id_error) if bus_id_error >= 1 else None
print("stop_id:", stop_id_error) if stop_id_error >= 1 else None
print("stop_name:", stop_name_error) if stop_name_error >= 1 else None
print("next_stop:", next_stop_error) if next_stop_error >= 1 else None
print("stop_type:", stop_type_error) if stop_type_error >= 1 else None
print("a_time:", a_time_error) if a_time_error >= 1 else None
