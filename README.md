

git clone https://gitlab.com/FieldWorker/timemap.git
cd timemap
npm install --legacy-peer-deps
cp example.config_working.js config.js
CONFIG=config.js npm run dev

#you need to modify the timerange to see the events
http://localhost:8080/?range=2022-02-01&range=2023-01-31