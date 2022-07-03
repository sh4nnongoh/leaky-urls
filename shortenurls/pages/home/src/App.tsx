import React, { useState } from "react";
import base64 from "base-64";
import logo from "./logo.svg";
import "./App.css";
const App = () => {
  const [url, setUrl] = useState("");
  const encodedUrl = base64.encode(url);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <form>
          <label htmlFor="url">
            Enter the URL you want shorten below!
            <br />
            <input
              type="text"
              id="url"
              name="url"
              value={url}
              style={{
                width: 500,
                height: 30
              }}
              onChange={(e) => {
                setUrl(e.target.value);
              }}
            />
          </label>
          <br />
        </form>
        <a href={`/shorten/${encodedUrl}`}>
          <button type="submit"> Link button </button>
        </a>
      </header>
    </div>
  );
};
export default App;
