import React, { Component } from "react";
import { withSnackbar } from "notistack";
import { Form, Select, TextArea } from "semantic-ui-react";

// The allowed options for ticket rating
const options = [
	{ key: "1", text: "1", value: "1" },
	{ key: "2", text: "2", value: "2" },
	{ key: "3", text: "3", value: "3" },
	{ key: "4", text: "4", value: "4" },
	{ key: "5", text: "5", value: "5" },
];

/* 
	Component: NewTicketForm
	Description: The form of the NewTicket button/modal. Handles all of the logic of sending an api request for a new ticket
*/
class NewTicketForm extends Component {
	// Set state
	constructor(props) {
		super(props);
		this.state = {
			msg: "",
			rate: "",
		};
	}

	// Handles the update of the message component of the form
	// and changes the state
	handleMsgChange = (e, result) => {
		const { name, value } = result;
		this.setState({ [name]: value });
	};

	// Handles the update of the rate component of the form
	// and changes the state
	handleRateChange = (e, result) => {
		const { name, value } = result;
		this.setState({ [name]: value });
	};

	// Handles the API call and displays a notification based
	// on the API's response
	submitTicketAPI = async () => {
		// Requesting API
		const response = await fetch(
			"/api/create-ticket/" + this.state.msg + "/" + this.state.rate + "/"
		);
		const data = await response.json();

		// Opening notification
		this.props.enqueueSnackbar(data.msg, {
			variant: data.snack_bar_variant,
		});
	};

	// The form
	render() {
		return (
			<Form>
				<Form.Field
					control={TextArea}
					name="msg"
					label="Message"
					placeholder="Message..."
					onChange={this.handleMsgChange}
					value={this.state.msg}
				/>
				<Form.Field
					control={Select}
					name="rate"
					label="Priotity Rating (higher # = higher priority)"
					options={options}
					placeholder="Rate"
					onChange={this.handleRateChange}
					value={this.state.rate}
				/>
				<Form.Button content="Submit" onClick={this.submitTicketAPI} />
			</Form>
		);
	}
}

export default withSnackbar(NewTicketForm);
