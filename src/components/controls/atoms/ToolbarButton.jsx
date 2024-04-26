export function ToolbarButton({ isActive, iconKey, onClick, label, children }) {
  return (
    <div
      className={isActive ? "toolbar-tab active" : "toolbar-tab"}
      key={iconKey}
      onClick={onClick}
    >
      {children ? (
        children
      ) : (
        <>
          <i className="material-icons">{iconKey}</i>
          <div className="tab-caption">{label}</div>
        </>
      )}
    </div>
  );
}

// https://github.com/reactjs/react-tabs#set-tabsrole
ToolbarButton.tabsRole = "Tab";
