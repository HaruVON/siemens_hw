# api/siemens_hw/tasks.py
# This file contains the api functions for this web app

import csv

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