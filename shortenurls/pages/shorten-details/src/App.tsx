import React from "react";
import logo from "./logo.svg";
import "./App.css";
const App = () => {
  const original = (((window as any).django)?.original);
  const shortenURL = (((window as any).django)?.shorten_url);
  const createdAt = (((window as any).django)?.created_at);
  const hasOriginal = original !== "{{ original }}";
  const hasShortenURL = shortenURL !== "{{ shorten_url }}";
  const hasCreatedAt = createdAt !== "{{ created_at }}";
  const hasDetails = hasOriginal && hasShortenURL && hasCreatedAt;
  if (window.location.pathname !== "/" && !hasDetails) {
    window.location.pathname = "/";
  }
  const fullShortenURL = `${window.location.href.split("/").slice(0, 3).join("/")}/${shortenURL}`;
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {
          hasDetails && (
            <>
              <span>
                Original URL:
                {" "}
                {original}
              </span>
              <span>
                Shorten URL:
                {" "}
                {fullShortenURL}
              </span>
              <span>
                Created At:
                {" "}
                {createdAt}
              </span>
            </>
          )
        }
      </header>
    </div>
  );
};
export default App;
