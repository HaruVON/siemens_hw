import React, { Component } from "react";
import { Button, Modal } from "semantic-ui-react";
import NewTicketForm from "./NewTicketForm";

/* 
	Component: NewTicketModal
	Description: This is the modal for the New Ticket button. It 
	opens a form to submit an API request via the NewTicketForm
*/
class ModalForm extends Component {
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
				<Button onClick={this.handleOpen}>New Ticket</Button>
				<Modal
					size="small"
					open={this.state.modalOpen}
					onClose={this.handleClose}
					closeIcon
				>
					<Modal.Header>New Ticket</Modal.Header>
					<Modal.Content>
						<NewTicketForm handleClose={this.handleClose} />
					</Modal.Content>
				</Modal>
			</div>
		);
	}
}

export default ModalForm;
