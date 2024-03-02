import csv
import json
import math

with open("step1.json") as file:
    our_data = json.load(file)

with open("associations.json") as file:
    associations = json.load(file)
with open("sources.json") as file:
    sources = json.load(file)
with open("events.json") as file:
    events = json.load(file)

our_data_new = our_data
events_new = events
sources_new = sources
associations_new = associations


def filter_dublicates():
    count = 0
    for index1, event1 in enumerate(our_data["Events"]):
        for index2, event2 in enumerate(events):
            if not event1["sources"]:
                our_data_new.pop(index1)
            if not event2["sources"]:
                events_new.pop(index2)
            if event2["sources"] and event1["sources"]:
                try:
                    if our_data["Sources"][event1["sources"][0]]["paths"][0] in sources[event2["sources"][0]]["paths"]:
                        our_data_new["Events"].pop(index1)
                    elif event1["description"] == event2["description"]:
                        our_data_new["Events"].pop(index1)
                except ValueError:
                    continue
    for index1, event1 in enumerate(our_data["Events"]):
        for index2, event2 in enumerate(events):
            try:
                distance = math.dist([float(event1["longitude"]), float(event1["latitude"])],
                                     [float(event2["longitude"]), float(event2["latitude"])])
            except ValueError:
                continue
            try:
                if event1["date"] == event2["date"] and distance < 0.3:
                    our_data_new["Events"].pop(index1)
                elif event1["date"] == event2["date"] and event1["longitude"][:-4] == event2["longitude"][:-4]:
                    our_data_new["Events"].pop(index1)
                elif event1["date"] == event2["date"] and event1["latitude"][:-4] == event2["latitude"][:-4]:
                    our_data_new["Events"].pop(index1)
            except ValueError as e:
                count += 1
                continue
    print(count)

    for event1 in our_data["Events"]:
        for event2 in events:
            if our_data["Sources"][event1["sources"][0]]["paths"][0] in sources[event2["sources"][0]]["paths"]:
                our_data_new["Events"].pop(our_data["Events"].index(event1))
    for event1 in our_data["Events"]:
        for event2 in events:
            if event1["description"] == event2["description"]:
                our_data_new["Events"].pop(our_data["Events"].index(event1))

filter_dublicates()
for event in events_new:
    event["associations"] = ["associations95"]


sources_new.update(our_data["Sources"])
events_new.extend(our_data["Events"])
print(len(events))
list_of_crimes = {"Events": events, "Sources": sources, "Associations": our_data["Associations"]}
with open("api.json", "w") as f:
    json.dump(list_of_crimes, f, indent=4, sort_keys=True)

# with open("almost_final_data.json") as file:
#     combined = json.load(file)
#
# events = combined["Events"]
# for event1 in combined["Events"]:
#     for event2 in combined["Events"]:
#         try:
#             if (event1["date"] == event2["date"] and
#                     event1["longitude"][:-3] == event2["longitude"][:-3]) and event1["latitude"][:-3] == event2["latitude"][:-3]:
#                 events[events.index(event1)]["sources"].extend(event2["sources"])
#                 events.pop(events.index(event2))
#                 print(event1, event2)
#         except ValueError:
#             continue
# print(len(events))
# list_of_crimes = {"Events": events, "Sources": combined["Sources"], "Associations": combined["Associations"]}
#
# with open("combined3.json", "w") as f:
#     json.dump(list_of_crimes, f, indent=4, sort_keys=True)
# associations = combined["Associations"]
# associations_list = ['Source needs revision', 'Miscellaneous', 'Type of area affected',
#                      'Sexual Violence and Rape', 'Weapon System', 'Environmental Damage',
#                      'POW and Internment camps', 'Killed or injured journalists',
#                      "Violations against POW's", 'Direct attacks on civilians',
#                      'Aerial and Artillery strikes targeting the civilian population']
# list_of_bullshit = {'Source needs revision': [],
#                     'Miscellaneous': [],
#                     'Type of area affected': [],
#                     'Sexual Violence and Rape': [],
#                     'Weapon System': [],
#                     'Environmental Damage': [],
#                     'POW and Internment camps': [],
#                     'Killed or injured journalists': [],
#                     "Violations against POW's": [],
#                     'Direct attacks on civilians': [],
#                     'Aerial and Artillery strikes targeting the civilian population': []}
# for association in associations_list:
#     for assoc in associations:
#         if association in assoc["filter_paths"]:
#             list_of_bullshit[association].append(assoc["id"])
#             # first_ids[association] = first_id
# # print(list_of_bullshit)
# # print(first_ids)
# list_of_firsts = {'Source needs revision': "associations1275",
#                   'Miscellaneous': "associations1076",
#                   'Sexual Violence and Rape': "associations1121",
#                   'Environmental Damage': "associations1214",
#                   'POW and Internment camps': "associations0",
#                   'Killed or injured journalists': "associations1245",
#                   "Violations against POW's": "associations1218",
#                   'Direct attacks on civilians': "associations1143",
#                   'Aerial and Artillery strikes targeting the civilian population': "associations95"}
# events = combined["Events"]
#
# for event in events:
#     for key, value in list_of_bullshit.items():
#         for asoc in event["associations"]:
#             try:
#                 if asoc in value:
#                     event["associations"].pop(event["associations"].index(asoc))
#                     event["associations"].append(list_of_firsts[key])
#             except KeyError:
#                 continue
#
# print(events)
# list_of_associations = []
# for first in list_of_firsts:
#     try:
#         list_of_associations.append({
#             "desc": [
#                 first
#             ],
#             "filter_paths": [
#                 first
#             ],
#             "id": list_of_firsts[first],
#             "mode": "FILTER",
#             "title": [
#                 first
#             ]
#         }
#         )
#     except ValueError:
#         continue
# list_of_crimes = {"Events": events, "Sources": combined["Sources"], "Associations": list_of_associations}
# with open("combined2.json", "w") as f:
#     json.dump(list_of_crimes, f, indent=4, sort_keys=True)


# for assoc in associations:
#     if association in assoc["filter_paths"]:
#         assoc["filter_paths"] = [association]
#         print(assoc)
# for association in associations:
#     # if len(association["filter_paths"]) > 1:
#     #     associations_list.append(association["filter_paths"][1])
#     # else:
#     associations_list.append(association["filter_paths"][0])
#
# associations_list = list(set(associations_list))
# print(associations_list)
