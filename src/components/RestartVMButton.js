import React, { Component } from "react";
import { Button, Confirm } from "semantic-ui-react";
import { withSnackbar } from "notistack";

/*
	Component: Package Installation Form
	Description: User submits a request to install software packages
*/
class RestartVMButton extends Component {
	state = { open: false };

	open = () => this.setState({ open: true });
	close = () => this.setState({ open: false });

	// Handles the API call and displays a notification based
	// on the API's response
	restartVM = async () => {
		// Requesting API
		const response = await fetch("/api/restart-vm/");
		const data = await response.json();

		// Opening a notification
		this.props.enqueueSnackbar(data.msg, {
			variant: data.snack_bar_variant,
		});
	};

	render() {
		return (
			<div style={{ display: "inline", margin: "0.5rem" }}>
				<Button onClick={this.open} style={{ margin: "0.5rem" }}>
					VM Restart
				</Button>
				<Confirm
					open={this.state.open}
					onCancel={this.close}
					onConfirm={this.restartVM}
				/>
			</div>
		);
	}
}

export default withSnackbar(RestartVMButton);
