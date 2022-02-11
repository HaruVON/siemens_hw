# api/siemens_hw/tasks.py
# This file contains the api functions for this web app

import csv

# Function: install_package_task
# Description: Installs an approved package to the corresponding
# IP
# Returns: A response dictionary used by the routes file
def install_package_task(ip_address, package):
    
    # List of approved packages
    packages = ["docker", "kdiff3", "meld", "postgres", "tmux"]

    # Run install package command if package is in the approved
    # packages list
    if package in packages:
        # Actual command
        # result = os.popen('ssh root@%s \'dnf install %s -y\'', ip_address, package)
        # if result = 0:
        #    return Response("Package Installed", status=200)
        # else:
        #    return Response("Something went wrong", status=500)
        return { "response": "Package Installed", "status": 200 }
    
    return { "response": "Invalid Package", "status": 500 }
        

# Function: process_ticket_task
# Description: Appends a ticket row to the CSV file
# Returns: A response dictionary used by the routes file
def process_ticket_task(ip_address, ticket_msg, ticket_rate):

    # Check if ticket_rate is a valid rate, if not return error
    rates = ['-1', '1', '2', '3', '4', '5']
    if ticket_rate not in rates:
        return { "response": "Invalid Rate", "status": 500 }
 

    # Log the ticket rate and message to the grafana_tickets.csv 
    # file
    path = "logs/grafana/grafana_tickets.csv"

    with open(path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([ticket_rate, ticket_msg])


    return { "response": "Ticket Processed", "status": 200 }


# Function: restart_vm_task
# Description: Restarts the VM with the corresponding IP
# Returns: A response dictionary used by the routes file
def restart_vm_task(ip_address):
    
    # Actual command
    # result = os.popen('ssh root@%s reboot', ip_address)
    result = 0

    if result == 0:
        return { "response": "VM Restarted", "status": 200 }

    return { "response": "Something went wrong", "status": 500 }