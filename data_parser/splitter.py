import json

with open("deepstate_data.json") as file:
    old_data = json.load(file)

list_of_dates = {}
for event in old_data:
    if event["date"] not in list_of_dates:
        list_of_dates[event["date"]] = [event]
    else:
        list_of_dates[event["date"]].append(event)

for date in list_of_dates:
    datefile = date.replace("/", "-")
    with open(f"mil_data/{datefile}.json", "w") as f:
        json.dump(list_of_dates[date], f, indent=4, sort_keys=True)
