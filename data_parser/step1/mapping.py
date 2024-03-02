import csv, re, json
from datetime import datetime
from random import randint

new_data = []
list_of_events = []
list_of_sources = {}
list_of_associations = []
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# Day of the month as a zero-padded decimal number;Month as locale’s full name.;
# Year with century as a decimal number.
expected_date_format = '%d %B %Y'
second_expected_date_format = '%B %d %Y'
third_expected_date_format = '%d/%m/%Y'
fourth_expected_date_format = '%B %d, %Y'
fifth_expected_date_format = '%m/%d/%Y'
sixth_expected_date_format = '%d%B %Y'
seventh_expected_date_format = '%d %B%Y'
eight_expected_date_format = '%d %B%Y'

# Month as a zero-padded decimal number.;Day of the month as a zero-padded decimal number;
# Year without century as a zero-padded decimal number.
wished_date_format = '%m/%d/%Y'


def try_parsing_date(text):
    for fmt in [expected_date_format,
                second_expected_date_format,
                third_expected_date_format,
                fourth_expected_date_format,
                fifth_expected_date_format,
                sixth_expected_date_format,
                seventh_expected_date_format,
                eight_expected_date_format]:
        try:
            date = datetime.strptime(text, fmt).strftime(wished_date_format)
            return date
        except Exception as e:
            pass
    return ""


with open("ProjectMariupol.csv") as file:
    reader = csv.reader(file, delimiter=',')
    new_data = [col for col in reader]
with open("list_of_events.json") as file:
    old_data = json.load(file)


def find_sources(latitude, longitude):
    for event in old_data["Events"]:
        if event["latitude"] == latitude and event["longitude"] == longitude:
            return event["sources"]
    return []


list_of_firsts = {'Miscellaneous': "associations1076",
                  'Sexual Violence and Rape': "associations1121",
                  'Environmental Damage': "associations1214",
                  'POW and Internment camps': "associations0",
                  'Killed or injured journalists': "associations1245",
                  "Violations against POWs": "associations1218",
                  'Direct attacks on civilians': "associations1143",
                  'Aerial and Artillery strikes targeting the civilian population': "associations95"}

list_of_wrong = []
for event in new_data[1:]:
    if event[8] not in list_of_firsts.keys():
        continue
    res = re.search(r".*?[d|D]at[e|a] of (discovery|Discovery|dicovery|incident)\s?(:|-)?\s*(.*?\d\d\d\d)",
                    event[1])
    res_first = ''
    if res:
        res_first = res.group(3)
        res_first = try_parsing_date(res_first)
    res = re.search(r"(Province|Prevince|country):(.*)(\n(City|country)?.*:(.*))?", event[1])
    res_second = ''
    if res:
        res_second = f"{res.group(2)} {res.group(5) if res.group(5) is not None else ''}"
    # if res_first == "":
    #     print(f"no date for {event[1]}")
    #
    sources = find_sources(event[2], event[3])
    source_id = f"sources11{str(randint(0, 10000))}"
    if not sources:
        if "http" in event[5]:
            sources = [source_id]  # todo fix the links thing, example at the end of step1.json
            paths = event[5].replace("[", "") \
                .replace("]", "") \
                .replace("'", "") \
                .replace('"', "")
        else:
            continue
    else:
        paths = old_data["Sources"][sources[0]]["paths"]

    event_id = f"CIV{str(randint(10000, 100000))}"

    if not event[1]:
        print(f"no date for {event[1]}")
        list_of_wrong.append(str(event_id) + " " + res_first)
        continue
    try:

        list_of_events.append({
            "id": str(event_id),
            "date": res_first,
            "graphic": "FALSE",
            "latitude": event[2],
            "longitude": event[3],
            "location": res_second,
            "description": f"""{event[1]}""",
            "time": "00:00",
            "category": "",
            "sources": sources,
            "associations": [list_of_firsts[event[8]], ]
        })

        list_of_sources[sources[0]] = {"id": sources[0],
                                       "title": event_id,
                                       "description": f"""{event[1]}""",
                                       "paths": paths,
                                       }
    except IndexError:
        print(f"no date for {event[1]}")
        list_of_wrong.append(str(event_id) + " " + res_first)
        continue

for first in list_of_firsts:
    try:
        list_of_associations.append({
            "desc": [
                first
            ],
            "filter_paths": [
                first
            ],
            "id": list_of_firsts[first],
            "mode": "FILTER",
            "title": [
                first
            ]
        }
        )
    except ValueError:
        continue

print(len(list_of_events))
print(len(list_of_wrong))

list_of_events = {"Events": list_of_events, "Sources": list_of_sources, "Associations": list_of_associations}

with open("step1.json", "w") as f:
    json.dump(list_of_events, f, indent=4, sort_keys=True)
