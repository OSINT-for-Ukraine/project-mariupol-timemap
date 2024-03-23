<h1 align="center">Project Mariupol TimeMap</h1>

![map.osintforukraine.com timemap preview](https://github.com/OSINT-for-Ukraine/project-mariupol-timemap/assets/74001397/20cc1902-4a6e-448b-bd72-c2869ec756ca)

<p align="center">
<strong>
	TimeMap is a tool for exploration, monitoring and classification of incidents in time and space, originally forked from Bellingcat's <a href="https://github.com/bellingcat/ukraine-timemap">Civilian Harm Ukraine-Timemap</a>, with special thanks to <a href="https://github.com/forensic-architecture">Forensic Architecture</a> for the original repository: <a href="https://github.com/forensic-architecture/timemap">forensic-architecture/timemap</a>.
</strong>
</p>
<br>
<br>

## Development Setup
1. Run `npm install` to install dependencies
2. Adjust any local configs in [config.js](config.js)
    * Documentation of [config.js](config.js)
        * `SERVER_ROOT` - points to the API base address
        * `XXXX_EXT` - points to the respective JSONs of the data, for events, sources, and associations
        * `API_DATA` - S3 file address that can be downloaded or integrated into external apps/visualizations
        * `MAPBOX_TOKEN` - used to load the custom styles
        * `DATE_FMT` and `TIME_FMT` - how to consume the events' date/time from the API
        * `store.app.map` - configures the initial map view and the UX limits
        * `store.app.cluster` - configures how clusters/bubbles are grouped into larger clusters, larger `radius` means bigger cluster bubbles
        * `store.app.timeline` - configure timeline ranges, zoom level options, and default range
        * `store.app.intro` - the intro panel that shows on start
        * `store.app.cover` - configuration for the full page cover, the `description` is a list of markdown entities, can also contain html
        * `store.ui.colors` and `store.ui.maxNumOfColors` are applied to filters, as they are selected
          
    * Easiest way to deploy the static files is through
        * `nvm use 16`
        * `npm run build` (rather: `CI=false npm run build`)
        * Copy the files to your server, for example to `/var/www/html`

3. Run `npm run dev` to start the development server. If you're using a custom config file, prefix the commad with `CONFIG=your_custom_config.js`
4. For more info visit the [original repo](https://github.com/forensic-architecture/timemap)
5. Run `npm run build` to build the webapp and `pm2 serve build/ 80 --name "map" --spa` to start the server
6. If you need to provide any specific env variable for the config in runtime:
6.a modify config.js adding new constant variable e.g. `const api_url = import.meta.env.VITE_API_URL;`
    variable has to start with the prefix 'VITE_'
6.b assign new created variable to what was previously stored in config dictionary e.g. 
config = {
...
-SERVER_ROOT: "https://api.osintforukraine.com/",
+SERVER_ROOT: api_url,
...
}
6.c update dynamically .env file by running `echo -e "\nVITE_API_URL=https://api.osintforukraine.com/" >> .env && npm run build`

## Deployment
This project is now living in github pages and the API has switched to auto-updated S3 files.

Release with `npm run deploy`

## Contributing
Please check our [issues page](https://github.com/OSINT-for-Ukraine/project-mariupol-timemap/issues) for desired contributions, and feel free to suggest your own. 

## Credits
* [Vasile Popa](https://github.com/popovvasile)
* [Filip Chudzyński](https://github.com/curcher)
* [Richard Mwewa](https://github.com/rly0nheart)
* [Cătălina Hasnaș](https://github.com/Catalina-Hasnas)
