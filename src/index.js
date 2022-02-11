import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { SnackbarProvider } from "notistack";
import reportWebVitals from "./reportWebVitals";
import "semantic-ui-css/semantic.min.css";

ReactDOM.render(
	// Must have App wrapped in SnackbarProvider to be
	// able to use notifications throughout app
	<SnackbarProvider maxSnack={3}>
		<App />
	</SnackbarProvider>,
	document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
