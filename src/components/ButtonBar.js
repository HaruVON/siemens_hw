import React, { Component } from "react";
import "../App.css";
import RestartVMButton from "./RestartVMButton";

/* 
	Component: ButtonBar
	Description: Wrapper class that ecompasses the Button 
	functions
*/
class ButtonBar extends Component {
	render() {
		return (
			<div>
				<RestartVMButton></RestartVMButton>
			</div>
		);
	}
}

export default ButtonBar;
