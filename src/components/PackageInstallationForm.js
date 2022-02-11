import React, { Component } from "react";
import { Form, Select } from "semantic-ui-react";
import { withSnackbar } from "notistack";

// List of allowed packages
const options = [
	{ key: "d", text: "Docker", value: "docker" },
	{ key: "k", text: "kdiff3 ", value: "kdiff3" },
	{ key: "m", text: "Meld", value: "meld" },
	{ key: "p", text: "Postgres", value: "postgres" },
	{ key: "t", text: "TMUX", value: "tmux" },
];

/*
	Component: PackageInstallationForm
	Description: User submits a request to install software 
	packages
*/
class PackageInstallationForm extends Component {
	// Set state for desired package
	constructor(props) {
		super(props);
		this.state = {
			package: "",
		};
	}

	// Handles the change of the selected package and updates
	// state accordingly
	handleChange = (e, result) => {
		const { name, value } = result;
		this.setState({ [name]: value });
	};

	// Handles the API call and displays a notification based
	// on the API's response
	installPackageAPI = async () => {
		// Requesting API
		const response = await fetch(
			"/api/install-package/" + this.state.package + "/"
		);
		const data = await response.json();

		// Opening notification
		this.props.enqueueSnackbar(data.msg, {
			variant: data.snack_bar_variant,
		});
	};

	// The Form
	render() {
		return (
			<Form>
				<Form.Field
					control={Select}
					placeholder="Package"
					name="package"
					label="Package"
					onChange={this.handleChange}
					options={options}
					value={this.state.package}
				/>
				<Form.Button
					content="Submit"
					onClick={this.installPackageAPI}
				/>
			</Form>
		);
	}
}

export default withSnackbar(PackageInstallationForm);
