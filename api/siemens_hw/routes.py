from flask import request
from siemens_hw import app
from siemens_hw.tasks import restart_vm_task


# Function: check_request
# Description: Check the api call's (task file) response to 
# respond to the frontend with the correct variables given a 
# success or an error
# Returns: A response dictionary used by the React from end
def check_request(api_response, log):
    # Check status code (200 is successful)
    if api_response["status"] == 200:
        # If 200 then log the api call and return a success object
        app.logger.info(log)
        return {"msg": api_response["response"], "status": "200", "snack_bar_variant": "success"}

    # Default: Return an error object
    app.logger.info("Error On: %s", log)
    return {"msg": api_response["response"], "status": "500", "snack_bar_variant": "error"}

# Function: get_ip
# Description: Get the client's IP address from the request 
# environment
# Returns: the client's IP address
def get_ip():
    # Getting IP address from different environment 
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']


# Function: restart_vm_route
# Description: Route to restart a vm
# Returns: A response dictionary used by the React from end
@app.route('/api/restart-vm/')
def restart_vm_route():
    # Get the client's IP address
    ip_address = get_ip()

    # Call the restart_vm_task function
    api_response = restart_vm_task(ip_address)
    log = "IP Address: %s restarted their vm", ip_address
    msg = api_response["response"]

    return check_request(api_response, log)