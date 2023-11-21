import csv, re, json
from datetime import datetime

content = []
list_of_events = []
list_of_sources = {}
list_of_associations =[]
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


with open("ofu_data.csv") as file:
    reader = csv.reader(file, delimiter=',')
    content = [col for col in reader]
list_of_wrong = []
for ind, event in enumerate(content[1:]):

    res = re.search(r".*?[d|D]at[e|a] of (discovery|Discovery|dicovery|incident)\s?(:|-)?\s*(.*?\d\d\d\d)", event[1])
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
        # list_of_wrong.append(str(ind)+" "+res_first)
    list_of_events.append({
        "id": str(ind),
        "date": res_first,
        "latitude": event[-2],
        "longitude": event[-3],
        "location": res_second,
        "description": f"""{event[1]}""",
        "time": "00:00",
        "category": "",
        "sources": [f"sources{ind}"],
        "associations": [f"associations{ind}"]
    })
    print([event[-8]])
    list_of_sources[f"sources{ind}"] = {"id": f"sources{ind}", "paths": [event[-9]], "title": "", "description":""}
    list_of_associations.append({"id": f"associations{ind}", "desc": [event[-8]], "title": [event[-8]], "mode": "FILTER", "filter_paths": [event[-8]]})
list_of_events = {"Events": list_of_events, "list_of_sources": list_of_sources, "Associations":list_of_associations}
# print(list_of_wrong)
with open("list_of_events.json", "w") as f:
    json.dump(list_of_events, f, indent=4, sort_keys=True)
