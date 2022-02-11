import React from "react";
import "./App.css";
import { Message } from "semantic-ui-react";

/*
	Component: Content
	Description: Shows the instructions
*/
class Content extends React.Component {
	// The Content
	render() {
		return (
			<div>
				<Message className="banner">
					Ticketing System. Below you can do the following:
					<ol>
						<li>Restart your VM</li>
						<li>Request a software package install</li>
					</ol>
				</Message>
			</div>
		);
	}
}

/*
	Component: App
	Description: Wrapper for everything in the App
*/
class App extends React.Component {
	render() {
		return (
			<div className="App">
				<Content />
				<br />
			</div>
		);
	}
}

export default App;
