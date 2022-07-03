import React from "react";
import { render, screen } from "@testing-library/react";
import App from "../App";
const userStory = `
Given no inital state,
When user navigates to the web page,
Then user sees the static information
`;
describe(userStory, () => {
  render(<App />);
  it("shows the static info", () => {
    const linkElement = screen.getByText(/Original URL:/i);
    expect(linkElement).toBeInTheDocument();
  });
});
