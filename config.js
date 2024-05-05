const one_day = 1440;
import dotenv from 'dotenv';
dotenv.config();

const api_url = import.meta.env.VITE_API_URL;
console.log(import.meta.env.VITE_API_URL);
const config = {
  title: "Project Mariupol",
  display_title: "Project Mariupol",
  SERVER_ROOT: api_url,
  MILITARY_EXT: "Military",
  EVENTS_EXT: "Events",
  SOURCES_EXT: "Sources",
  ASSOCIATIONS_EXT: "Associations",
  LOGIN_EXT: "login",
  // API_DATA: "https://api.osintforukraine.com/Events",
  API_DATA: api_url + "Events",
  MAPBOX_TOKEN:
    "pk.eyJ1IjoiYmVsbGluZ2NhdC1tYXBib3giLCJhIjoiY2tleW0wbWliMDA1cTJ5bzdkbTRraHgwZSJ9.GJQkjPzj8554VhR5SPsfJg",
  // MEDIA_EXT: "/api/media",
  DATE_FMT: "MM/DD/YYYY",
  TIME_FMT: "hh:mm",

  store: {
    app: {
      debug: false,
      map: {
        // anchor: [49.02421913, 31.43836003],
        anchor: [48.3326259, 33.19951447],
        maxZoom: 18,
        minZoom: 4,
        startZoom: 6,
        // maxBounds: []
      },
      cluster: { radius: 50, minZoom: 5, maxZoom: 12 },
      associations: {
        defaultCategory: "Weapon System",
      },
      timeline: {
        dimensions: {
          height: 90,
          contentHeight: 90,
        },
        zoomLevels: [
          // { label: "Zoom to 2 weeks", duration: 14 * one_day },
          { label: "Zoom to 1 month", duration: 31 * one_day },
          { label: "Zoom to 6 months", duration: 6 * 31 * one_day },
          { label: "Zoom to 1 year", duration: 12 * 31 * one_day },
          { label: "Zoom to 2 years", duration: 24 * 31 * one_day },
        ],
        range: {
          /**
           * Initial date range shown on map load.
           * Use [start, end] (strings in ISO 8601 format) for a fixed range.
           * Use undefined for a dynamic initial range based on the browser time.
           */
          initial: undefined,
          /** The number of days to show when using a dynamic initial range */
          initialDaysShown: 31,
          limits: {
            /** Required. The lower bound of the range that can be accessed on the map. (ISO 8601) */
            lower: "2022-02-01T00:00:00.000Z",
            /**
             * The upper bound of the range that can be accessed on the map.
             * Defaults to current browser time if undefined.
             */
            upper: undefined,
          },
        },
      },
      intro: [
        '<div class="two-columns"><div class="two-columns_column"><figure><img style="width: 100%; display:block;" src="https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/ukraine-timemap/cover01-s.jpg" frameborder="0"><figcaption>Image: Vyacheslav Madiyevskyy/Reuters</figcaption></figure></div><div class="two-columns_column"><figure><img style="width: 100%; display:block;" src="https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/ukraine-timemap/cover02-s.jpg" frameborder="0"><figcaption>Image: Järva Teataja/Scanpix Baltics via Reuters</figcaption></figure></div></div>',
        "Each day, new information and imagery of war crimes in occupied territories and combat zones around Ukraine emerge. Since the revelation of the Bucha massacre at the beginning of April 2022, there have been various efforts to document war crimes in Ukraine. However, as part of southern and parts of eastern Ukraine remain occupied, traditional modes of investigation have not been successful in gathering information from those regions.\n" +
        "Open-source information is information in any format (audio, visual and/or metadata) that is available to be accessed online without restrictions. Popular examples are photos from social media apps and pages. In the context of Ukraine, OSINT has been utilised vastly for many purposes. During the first few weeks of the war (and still today), OSINT pages and channels on Telegram and Twitter have been tracking the war (uploading troop movements, tallying unit casualties from photos and videos, tracking planes via the ‘flightradar’ app). In mid-March, the first OSINT information on war crimes emerged with MAXAR satellite imagery of corpse covered roads in occupied Bucha, Hostomel, and Irpin (towns near Kyiv). From then on, various OSINT investigation efforts have been conducted by both governmental and private organisations to document war crimes in Ukraine.\n" +
        "The project has a twofold goal:\n" +
        "- mapping international crimes committed in Ukraine by the Russian Federation,\n" +
        "- providing a learning environment to new OSINTers by training them by practice. \n" +
        "We achieve our mission by:\n" +
        "- documenting international crimes by our OSINTers,\n" +
        "- aggregating already mapped data from other OSINT groups,\n" +
        "- collaborating with international and local NGOs, \n" +
        "- collaboration with academic institutions."
      ],

      flags: { isInfopoup: false, isCover: false },
      cover: {
        title: "About and Methodology",
        exploreButton: "BACK TO THE PLATFORM",
        description: [
          "Each day, new information and imagery of war crimes in occupied territories and combat zones around Ukraine emerge. Since the revelation of the Bucha Massacre at the beginning of April 2022, there have been various efforts to document war crimes in Ukraine. However, as part of southern and parts of eastern Ukraine remain occupied, traditional modes of investigation have not been successful in gathering information from those regions.\n" +
          "\n" +
          "Open-source information is information in any format (audio, visual and/or metadata) that is available to be accessed online without restrictions. Popular examples are photos from social media apps and pages. In the context of Ukraine, OSINT has been utilised vastly for many purposes. During the first few weeks of the war (and still today) OSINT pages and channels on Telegram and Twitter have been tracking the war (uploading troop movements, tallying unit casualties from photos and videos, tracking planes via the ‘flightradar’ app). In mid-March, the first OSINT information on war crimes emerged with MAXAR satellite imagery of corpse covered roads in occupied Bucha, Hostomel and Irpin (towns near Kyiv). From then on, various OSINT investigation efforts have been conducted by both governmental and private organisations to document war crimes in Ukraine.\n" +
          "\n" +
          "The project has a two fold goal: \n" +
          "\n" +
          "    - Mapping international crimes committed in Ukraine by the Russian Federation \n" +
          "\n" +
          "    - Providing a learning environment to new OSINTers by training them by practice \n" +
          "\n" +
          "We achieve our mission by: \n" +
          "\n" +
          "    - Documenting International Crimes by our OSINTers\n" +
          "\n" +
          "    - Aggregating already mapped data from other OSINT groups\n" +
          "\n" +
          "    - Collaborating with International and Local NGO’s \n" +
          "\n" +
          "    - Collaboration with Academic Institutions",
        ],
      },
      toolbar: {
        panels: {
          categories: {
            // TRUE: {
            //   icon: "public",
            //   label: "Verified",
            //   description: "todo",
            // },
            // FALSE: {
            //   icon: "public",
            //   label: "Unverified",
            //   description: "todo",
            // }
          },
        },
      },
      spotlights: {},
    },
    ui: {
      coloring: { // todo change color
        mode: "STATIC",
        maxNumOfColors: 10,
        defaultColor: "#262323",
        colors: [
          "#8B0000",
          "#442020",
          "#2F4F4F",
          "#08B2E3",
          "#A1887F",
          "#E57373",
          "#90A4AE",
          "#80CBC4",
          "#7E57C2",
          "#FFEB3B",
        ],
      },
      card: {
        layout: {
          template: "sourced",
        },
      },
      carto: {
        eventRadius: 8,
      },
      timeline: {
        eventRadius: 9,
      },
      tiles: {
        current: "bellingcat-mapbox/cl0qnou2y003m15s8ieuyhgsy",
        default: "bellingcat-mapbox/cl0qnou2y003m15s8ieuyhgsy",
        satellite: "bellingcat-mapbox/cl1win2vp003914pdhateva6p"
      },
    },
    features: {
      USE_CATEGORIES: false,
      CATEGORIES_AS_FILTERS: false,
      COLOR_BY_CATEGORY: false,
      COLOR_BY_ASSOCIATION: true,
      USE_ASSOCIATIONS: true,
      USE_FULLSCREEN: true,
      USE_DOWNLOAD: false,
      USE_SOURCES: true,
      USE_SPOTLIGHTS: false,
      USE_SHAPES: false,
      USE_COVER: true,
      USE_INTRO: false,
      USE_SATELLITE_OVERLAY_TOGGLE: true,
      USE_SEARCH: false,
      USE_SITES: false,
      ZOOM_TO_TIMEFRAME_ON_TIMELINE_CLICK: one_day,
      FETCH_EXTERNAL_MEDIA: false,
      USE_MEDIA_CACHE: false,
      GRAPH_NONLOCATED: false,
      NARRATIVE_STEP_STYLES: false,
      CUSTOM_EVENT_FIELDS: [],
    },
  },
};

export default config;