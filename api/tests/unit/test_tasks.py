# api/tests/unit/test_tasks.py
# This file contains the unit tests for the tasks.py file

import os
import re
from siemens_hw.tasks import install_package_task, process_ticket_task, restart_vm_task


# Test IP address ( Would have to either spin up a Docker container to test against or have an outside testing server)
ip_address = '192.168.10.5'


# Function: test_install_package_task
# Description: Tests the install_package_task function
# GIVEN a response status code and message
# WHEN a request is made to install a valid package (in packages) and invalid package
# THEN check the response status code and message
def test_install_package_task():
    # Testing all valid packages
    packages = ["docker", "kdiff3", "meld", "postgres", "tmux"]

    for package in packages:
        result = install_package_task(ip_address, package)

        assert result['status'] == 200
        assert result['response'] == 'Package Installed'

    # Testing invalid package
    result = install_package_task(ip_address, 'python')

    assert result['status'] == 500
    assert result['response'] == 'Invalid Package'


# Function: test_process_ticket_task
# Description: Tests the test_process_ticket_task function
# GIVEN a response status code and message
# WHEN a request is made to restart a vm
# THEN check the response status code, message, and ticket log
def test_process_ticket_task():

    # Create a fake ticket and call the process_ticket_task function
    ticket = {'msg': 'Test TEST Test', 'rate': '-1'}
    result = process_ticket_task(ip_address, ticket["msg"], ticket["rate"])

    # Check to see if the ticket wrote to the grafana_tickets.csv 
    # file
    cmd = os.popen('grep \'Test\' ./logs/grafana/grafana_tickets.csv')
    cmd_res = cmd.read()

    # Clean up the testing tickets (-1 priority rating)
    path = "logs/grafana/grafana_tickets.csv"
    with open (path, 'r+') as f:
        content = f.read()
        f.seek(0)
        content_new = re.sub('-1.*\n', '', content, flags = re.M)
        f.write(content_new)
        f.truncate()
        

    # Assert that the ticket is in the grafana_tickets.csv file
    # and that the function returns the proper object
    assert ticket["rate"] in cmd_res
    assert ticket["msg"] in cmd_res
    assert result['status'] == 200
    assert result['response'] == 'Ticket Processed'


    # Test for invalid rates to make sure it responds with an 
    # error
    ticket = {'msg': 'Test TEST Test', 'rate': '-500'}
    result = process_ticket_task(ip_address, ticket["msg"], ticket["rate"])

    assert result['status'] != 200
    assert result['response'] != 'Ticket Processed'
    

# Function: test_restart_vm_task
# Description: Tests test_restart_vm_task
# GIVEN a response status code and message
# WHEN a request is made to restart a vm
# THEN check the response status code and message
def test_restart_vm_task():
    
    # Call the restart_vm_task function
    result = restart_vm_task(ip_address)
    
    assert result['status'] == 200
    assert result['response'] == 'VM Restarted'