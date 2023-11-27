import SitesIcon from "../atoms/SitesIcon";
import CoverIcon from "../atoms/CoverIcon";
// import InfoIcon from "../atoms/InfoIcon";

function BottomActions(props) {
  function renderToggles() {
    return (
      <>
        <div className="bottom-action-block">
          {props.features.USE_SITES ? (
            <SitesIcon
              isActive={props.sites.enabled}
              onClickHandler={props.sites.toggle}
            />
          ) : null}
        </div>
        {/* ,
        <div className="botttom-action-block">
          <InfoIcon
            isActive={props.info.enabled}
            onClickHandler={props.info.toggle}
          />
        </div>
        , */}
        <div className="botttom-action-block">
          {props.features.USE_COVER ? (
            <CoverIcon onClickHandler={props.cover.toggle} />
          ) : null}
        </div>
        <div style={{ fontSize: 9, paddingTop: 10 }}>
          Made with{" "}
          <a href="https://github.com/bellingcat/ukraine-timemap"> TimeMap </a>
          <br />
          Free software made by <br />{" "}
          <a href="https://forensic-architecture.org"> Forensic Architecture </a>
            <br />
            and
            <a href="https://www.bellingcat.com/"> Bellingcat </a>

        </div>
      </>
    );
  }

  return <div className="bottom-actions">{renderToggles()}</div>;
}

export default BottomActions;
