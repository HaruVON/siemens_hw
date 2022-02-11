import React, { Component } from "react";
import "../App.css";
import NewTicketModal from "./NewTicketModal";
import PackageInstallationModal from "./PackageInstallationModal";
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
				<PackageInstallationModal></PackageInstallationModal>
				<NewTicketModal></NewTicketModal>
			</div>
		);
	}
}

export default ButtonBar;
