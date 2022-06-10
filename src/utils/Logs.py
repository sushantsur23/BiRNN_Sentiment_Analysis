from datetime import datetime
import logging
import os

class Logger():

    def logg():
        logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")