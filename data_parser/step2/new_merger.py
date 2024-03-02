import csv
import json
import math

with open("step1.json") as file:
    our_data = json.load(file)
our_data_new = our_data
with open("associations.json") as file:
    associations = json.load(file)
with open("sources.json") as file:
    sources = json.load(file)
with open("events.json") as file:
    events = json.load(file)

new_events = events


def item_removal(item, list):
    if item in list:
        list.remove(item)


def filter_dublicates():
    count = 0
    for index2, event2 in enumerate(events):
        for index1, event1 in enumerate(our_data["Events"]):
            try:
                distance = math.dist([float(event1["longitude"]), float(event1["latitude"])],
                                     [float(event2["longitude"]), float(event2["latitude"])])
                if event1["date"] == event2["date"] and distance < 0.02:
                    item_removal(event1, our_data_new["Events"])
            except ValueError as e:
                item_removal(event1, our_data_new["Events"])
                count += 1
                continue
            if not event1["sources"]:
                item_removal(event1, our_data_new["Events"])
            elif not event2["sources"]:
                item_removal(event2, new_events)
            elif event2["sources"] and event1["sources"]:
                try:
                    if our_data["Sources"][event1["sources"][0]]["paths"][0] in sources[event2["sources"][0]]["paths"]:
                        item_removal(event1, our_data_new["Events"])
                    elif event1["description"] == event2["description"]:
                        item_removal(event1, our_data_new["Events"])
                except ValueError:
                    continue
            elif not event1["longitude"] or not event2["longitude"] or not event1["latitude"] or not event2["latitude"]:
                item_removal(event1, our_data_new["Events"])

    for event1 in our_data["Events"]:
        for event2 in events:
            if our_data["Sources"][event1["sources"][0]]["paths"][0] in sources[event2["sources"][0]]["paths"]:
                if event1 in our_data["Events"]: our_data_new["Events"].remove(event1)
    for event1 in our_data["Events"]:
        for event2 in events:
            if event1["description"] == event2["description"]:
                if event1 in our_data["Events"]: our_data_new["Events"].remove(event1)
    print(count)

filter_dublicates()


# def filter_dublicates2():
#     count = 0
#     for index2, event2 in enumerate(events):
#         for index1, event1 in enumerate(events):
#             try:
#                 distance = math.dist([float(event1["longitude"]), float(event1["latitude"])],
#                                      [float(event2["longitude"]), float(event2["latitude"])])
#                 if event1["date"] == event2["date"] and distance < 0.02:  # aprx 2 km
#                     print(distance)
#                     item_removal(event1, new_events)
#                     count += 1
#             except ValueError as e:
#                 breakpoint()
#                 count += 1
#                 continue
#             else:
#                 continue

# filter_dublicates2()
for event in events:
    event["associations"] = ["associations95"]

for source in our_data["Sources"]:
    if type(our_data["Sources"][source]["paths"]) is str:
        our_data["Sources"][source]["paths"] = our_data["Sources"][source]["paths"].strip().split(",")

sources.update(our_data["Sources"])
events.extend(our_data["Events"])
print(len(events))
list_of_crimes = {"Events": events, "Sources": sources, "Associations": our_data["Associations"]}
with open("api.json", "w") as f:
    json.dump(list_of_crimes, f, indent=4, sort_keys=True)
