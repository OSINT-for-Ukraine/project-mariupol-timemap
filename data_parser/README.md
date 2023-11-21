to run the script
it expects to have example.csv with the data from mariupol map
format: title,description,url,group,icon,color,visible,media_url,longitude,latitude,maphub_image_url

run:
only standard library is expected
```
python3 mapping.py
```
as an output we generate list_of_events.json
from which we want to create an endpoint serving just created json

```
npm install --prefix . json-server
```
it will create node_modules folder and package-lock.json, package.json config files.

```
#I didn't find any better way to locate locally installed executables then that
$(npm bin)/json-server --watch list_of_events.json
```