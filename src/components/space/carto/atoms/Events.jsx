import colors from "../../../../common/global";
import ColoredMarkers from "../../../atoms/ColoredMarkers";
import Portal from "../../../Portal";
import hash from "object-hash";
import {
  calcOpacity,
  calculateColorPercentages,
  zipColorsToPercentages,
} from "../../../../common/utilities";
import { fetchMilitaryData } from "../../../../actions/index";
import { useState } from "react";

const formatDate = (date) => {
  const initialDate = new Date(date);

  const options = { year: "numeric", month: "2-digit", day: "2-digit" };

  return initialDate.toLocaleDateString("en-US", options).replace(/\//g, "-");
};

function MapEvents({
  getCategoryColor,
  categories,
  projectPoint,
  styleLocation,
  selected,
  narrative,
  onSelect,
  svg,
  locations,
  eventRadius,
  coloringSet,
  filterColors,
  features,
}) {
  const [militaryUnitsLocation, setMilitaryUnitsLocation] = useState([]);

  async function handleEventSelect(e, location) {
    const events = e.shiftKey
      ? selected.concat(location.events)
      : location.events;

    const formattedDate = formatDate(events[0].datetime);

    const data = await fetchMilitaryData(formattedDate);

    setMilitaryUnitsLocation(data);

    onSelect(events);
  }

  function handleMilitaryUnitSelect(e, location) {
    console.log(location);
    onSelect(location);
  }

  function renderBorder() {
    return (
      <>
        <circle
          className="event-hover"
          cx="0"
          cy="0"
          r="10"
          stroke={colors.primaryHighlight}
          fillOpacity="0.0"
        />
      </>
    );
  }

  function renderLocationSlicesByAssociation(location) {
    const colorPercentages = calculateColorPercentages([location], coloringSet);

    const styles = {
      stroke: colors.darkBackground,
      strokeWidth: 0,
      fillOpacity: narrative ? 1 : calcOpacity(location.events.length),
    };

    return (
      <ColoredMarkers
        radius={eventRadius}
        colorPercentMap={zipColorsToPercentages(filterColors, colorPercentages)}
        styles={{
          ...styles,
        }}
        className="location-event-marker"
      />
    );
  }

  function renderLocation(location) {
    /**
    {
      events: [...],
      label: 'Location name',
      latitude: '47.7',
      longitude: '32.2'
    }
    */
    if (!location.latitude || !location.longitude) return null;
    const { x, y } = projectPoint([location.latitude, location.longitude]);

    // in narrative mode, only render events in narrative
    // TODO: move this to a selector
    if (narrative) {
      const { steps } = narrative;
      const onlyIfInNarrative = (e) => steps.map((s) => s.id).includes(e.id);
      const eventsInNarrative = location.events.filter(onlyIfInNarrative);

      if (eventsInNarrative.length <= 0) {
        return null;
      }
    }

    const customStyles = styleLocation ? styleLocation(location) : null;
    const extraRender = () => <>{customStyles[1]}</>;

    const isSelected = selected.reduce((acc, event) => {
      return (
        acc ||
        (event.latitude === location.latitude &&
          event.longitude === location.longitude)
      );
    }, false);

    return (
      <svg key={hash(location)}>
        <g
          className={`location-event ${narrative ? "no-hover" : ""}`}
          transform={`translate(${x}, ${y})`}
          onClick={(e) => handleEventSelect(e, location)}
        >
          {renderLocationSlicesByAssociation(location)}
          {extraRender ? extraRender() : null}
          {isSelected ? null : renderBorder()}
        </g>
      </svg>
    );
  }

  function renderMilitary(location) {
    if (!location.latitude || !location.longitude) return null;
    const { x, y } = projectPoint([location.latitude, location.longitude]);

    return (
      <svg key={hash(location)}>
        <g
          className={`location-event`}
          transform={`translate(${x}, ${y})`}
          // onClick={(e) => handleMilitaryUnitSelect(e, location)}
        >
          <path
            d="M 8 0 A 8 8 0 1 1 8 -1.959434878635765e-15 L 0 0  L 8 0 Z"
            fill="black"
          />
          <circle
            className="event-hover"
            cx="0"
            cy="0"
            r={10.10136847440446 + 2}
            stroke={colors.primaryHighlight}
            fillOpacity="0.0"
          />
        </g>
      </svg>
    );
  }

  return (
    <Portal node={svg}>
      <svg>
        <g className="event-locations">{locations.map(renderLocation)}</g>
        {militaryUnitsLocation.length > 0 && (
          <g className="event-locations">
            {militaryUnitsLocation.map(renderMilitary)}
          </g>
        )}
      </svg>
    </Portal>
  );
}

export default MapEvents;
