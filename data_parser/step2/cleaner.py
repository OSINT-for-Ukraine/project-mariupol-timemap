import csv
import json
import math

with open("api.json") as file:
    our_data = json.load(file)
print(len(our_data["Events"]))

our_data_new = our_data
count = 0
for index1, event1 in enumerate(our_data["Events"]):
    for index2, event2 in enumerate(our_data["Events"]):
        try:
            distance = math.dist([float(event1["longitude"]), float(event1["latitude"])],
                                 [float(event2["longitude"]), float(event2["latitude"])])
        except ValueError:
            continue
        try:
            if event1["date"] == event2["date"] and distance < 0.3:
                our_data_new["Events"].pop(our_data_new["Events"].index(event1))
        except ValueError as e:
            count += 1
            continue
        try:
            if event1["date"] == event2["date"] and event1["longitude"][:-4] == event2["longitude"][:-4]:
                our_data_new["Events"].pop(our_data_new["Events"].index(event1))
        except ValueError as e:
            count += 1
            continue
        try:
            if event1["date"] == event2["date"] and event1["latitude"][:-4] == event2["latitude"][:-4]:
                our_data_new["Events"].pop(our_data_new["Events"].index(event1))
        except ValueError as e:
            count += 1
            continue
print(count)
print(len(our_data_new["Events"]))
print(len(our_data["Events"]))

with open("api2.json", "w") as f:
    json.dump(our_data_new, f, indent=4, sort_keys=True)