import logging
from logging.handlers import RotatingFileHandler
import os
import csv

from flask import Flask


# Create App Var
app = Flask(__name__)


# Setup Logging if Flask API is not run in debug mode
if not app.debug:
    # Make sure logs directory is created
    if not os.path.exists('logs'):
        os.mkdir('logs')
    # Create the filehandler
    file_handler = RotatingFileHandler('logs/siemens_hw.log', maxBytes=10240, backupCount=10)

    # Set formatting and level for logger
    log_formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    # Setup csv file for grafana
    path = "./logs/grafana/grafana_tickets.csv"

    # Make sure logs/grafana path exists
    if not os.path.exists('logs/grafana'):
        os.mkdir('logs/grafana')

    # Check to see if csv file exists, if not setup headers in 
    # csv file
    if not os.path.exists(path):
        fields = ['Priority Rating', 'Ticket Message']
        with open(path, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)


from siemens_hw import routes