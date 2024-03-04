import json
from datetime import datetime

with open("deepstate_data") as file:
    old_data = json.load(file)

list_of_dates = {}
for event in old_data:
    if event["date"] not in list_of_dates:
        list_of_dates[event["date"]] = [event]
    else:
        list_of_dates[event["date"]].append(event)

for date in list_of_dates:
    datefile = date.replace("/", "-")
    date_obj = datetime.strptime(datefile, "%m-%d-%Y")
    new_date_str = date_obj.strftime("%d-%m-%Y")
    with open(f"{new_date_str}", "w") as f:
        json.dump(list_of_dates[date], f, indent=4, sort_keys=True)
