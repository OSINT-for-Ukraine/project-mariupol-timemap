# prerequisties 

## add repostiories for Node 16
```
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

```
NODE_MAJOR=16
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

## install node 16
```
sudo apt-get update
sudo apt-get install nodejs -y
```
# installation
## install timemap

```
git clone https://gitlab.com/FieldWorker/timemap.git
cd timemap
npm install --legacy-peer-deps
cp example.config_working.js config.js
```

## set top directory variable
This step is just to ease up the setup for you, if you know what you're doing just skip it

```
TOP_DIRECTORY=$(pwd)
```

## install json-server

```
cd "${TOP_DIRECTORY}/csv_to_json_mapping"
npm install --prefix . json-server
```

# start of timemap and json-server
First we need to start our json endpoint providing data for the map

## start json-server

```
cd "${TOP_DIRECTORY}/csv_to_json_mapping"
$(npm bin)/json-server --watch list_of_events.json --port 4040
```

## start timemap in the second terminal
open new terminal and navigate to timemap folder
then execute
```
CONFIG=config.js npm run dev
```

you need to modify the timerange to see the events. Use below URL:
http://localhost:8080/?range=2022-02-01&range=2023-01-31