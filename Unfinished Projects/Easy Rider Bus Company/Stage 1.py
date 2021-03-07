import json

with open("Unfinished Projects\Easy Rider Bus Company\json.json", "r") as json_file:
    json_file = json.load(json_file)

bus_id_error = 0
stop_id_error = 0
stop_name_error = 0
next_stop_error = 0
stop_type_error = 0
a_time_error = 0

for a in json_file:
    # or not ""
    # not a["stop_name"].isupper() or
    if not isinstance(a["bus_id"], int):
        bus_id_error += 1
    if not isinstance(a["stop_id"], int):
        stop_id_error += 1
    if not a["stop_name"].istitle() or a["stop_name"] == "":
        stop_name_error += 1
    if not isinstance(a["next_stop"], int) or "":
        next_stop_error += 1
    if not str(a["stop_type"]) in "asf" or not str(a["stop_type"]) in "ASF" or str(a["stop_type"]) != "":
        stop_type_error += 1
    if not isinstance(a["a_time"], str):
        a_time_error += 1


error = bus_id_error + stop_id_error + stop_name_error + \
    next_stop_error + next_stop_error + stop_type_error + a_time_error

print(
    f"Type and required field validation {error}", + "error:\n" if error == 1 else "errors:\n")
print("bus_id:", bus_id_error)
print("stop_id:", stop_id_error)
print("stop_name:", stop_name_error)
print("next_stop:", next_stop_error)
print("stop_type:", stop_type_error)
print("a_time:", a_time_error)
