import React, { Component } from "react";
import { Button, Modal } from "semantic-ui-react";
import PackageInstallationForm from "./PackageInstallationForm";

/* 
	Component: PackageInstallationModal
	Description: This is the modal for the Package Installation button. It opens a form to submit an API request via the 
	PackageInstallaationForm
*/
class PackageInstallationModal extends Component {
	// Set state of modal
	state = {
		modalOpen: false,
	};

	// Handles the opening and closing of the modal based on
	// the button being clicked
	handleOpen = () => this.setState({ modalOpen: true });
	handleClose = () => this.setState({ modalOpen: false });

	// The Modal
	render() {
		return (
			<div style={{ display: "inline", margin: "0.5rem" }}>
				<Button onClick={this.handleOpen}>Package Installation</Button>

				<Modal
					size="small"
					open={this.state.modalOpen}
					onClose={this.handleClose}
					closeIcon
				>
					<Modal.Header>Package Installation</Modal.Header>
					<Modal.Content>
						<PackageInstallationForm
							handleClose={this.handleClose}
						/>
					</Modal.Content>
				</Modal>
			</div>
		);
	}
}

export default PackageInstallationModal;
