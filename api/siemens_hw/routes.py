from flask import request
from siemens_hw import app
from siemens_hw.tasks import restart_vm_task

# Function: restart_vm_route
# Description: Route to restart a vm
# Returns: A response dictionary used by the React from end
@app.route('/api/restart-vm/')
def restart_vm_route():
    pass