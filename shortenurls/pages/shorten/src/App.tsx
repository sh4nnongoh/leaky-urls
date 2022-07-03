import React from "react";
import logo from "./logo.svg";
import "./App.css";
const App = () => {
  const shortenURL = (((window as any).django)?.shorten_url || "");
  if (window.location.pathname !== "/" && !shortenURL) {
    window.location.pathname = "/";
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {shortenURL && (
          <>
            <p>
              Your shorten URL is below!
            </p>
            <text>
              {shortenURL}
            </text>
          </>
        )}
      </header>
    </div>
  );
};
export default App;
