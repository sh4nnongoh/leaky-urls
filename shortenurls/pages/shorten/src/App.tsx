import React from "react";
import logo from "./logo.svg";
import "./App.css";
const App = () => {
  const shortenURL = (((window as any).django)?.shorten_url);
  const hasShortenURL = shortenURL !== "{{ shorten_url }}";
  if (window.location.pathname !== "/" && !hasShortenURL) {
    window.location.pathname = "/";
  }
  const fullShortenURL = `${window.location.href.split("/").slice(0, 3).join("/")}/${shortenURL}`;
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {hasShortenURL && (
          <>
            <p>
              Your shorten URL is below!
            </p>
            <div>
              {fullShortenURL}
            </div>
          </>
        )}
      </header>
    </div>
  );
};
export default App;
