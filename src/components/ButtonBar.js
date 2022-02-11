import React, { Component } from "react";
import "../App.css";
import RestartVMButton from "./RestartVMButton";
import PackageInstallationModal from "./PackageInstallationModal";

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
				<PackageInstallationModal></PackageInstallationModal>
			</div>
		);
	}
}

export default ButtonBar;
