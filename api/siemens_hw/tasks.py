# api/siemens_hw/tasks.py
# This file contains the api functions for this web app


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