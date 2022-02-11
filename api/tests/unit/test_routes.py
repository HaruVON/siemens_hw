from ipaddress import ip_address
from siemens_hw import app
from siemens_hw.routes import check_request
from siemens_hw.tasks import restart_vm_task

ip_address = '192.168.10.5'

# Function: test_check_request
# Description: Tests the test_check_request function
# GIVEN a response from the API
# WHEN a request is made to the API
# THEN check the msg, status, and snack_bar_variant
def test_check_request():

    # Create log and api_response vars
    log = "Test Log"
    api_response = restart_vm_task(ip_address)

    # Call check_request
    result = check_request(api_response, log)

    # Assert the return object has the correct variables
    assert result["msg"] == api_response["response"]
    assert result["status"] == "200"
    assert result["snack_bar_variant"] == "success"


# Function: test_create_ticket_route
# Description: Tests the test_create_ticket_route route
# GIVEN a response from the url route
# WHEN a request is made to the API
# THEN check the status code to see if the route exists
def test_create_ticket_route():
    with app.test_client() as c:
        response = c.get('/api/create-ticket/Test/-1/')
        assert response.status_code == 200


# Function: test_install_package_route
# Description: Tests the test_install_package_route route
# GIVEN a response from the url route
# WHEN a request is made to the API
# THEN check the status code to see if the route exists and
# check to make sure invalid package routes do not exist
def test_install_package_route():
    packages = ["docker", "kdiff3", "meld", "postgres", "tmux"]

    for package in packages:
        url = '/api/install-package/' + package + '/'
        with app.test_client() as c:
            response = c.get(url)
            assert response.status_code == 200

    with app.test_client() as c:
        response = c.get('/api/install-package/python')
        assert response.status_code != 200


# Function: test_restart_vm_route
# Description: Tests the test_restart_vm_route route
# GIVEN a response from the url route
# WHEN a request is made to the API
# THEN check the status code to see if the route exists
def test_restart_vm_route():
    with app.test_client() as c:
        response = c.get('/api/restart-vm/')
        assert response.status_code == 200