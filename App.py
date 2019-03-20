from flask import Flask
import logging as logger
import datetime
import os
from configs.config import Config



#controllers
from controllers.reporting_controller import reporting_controller
from controllers.notification_controller import notification_controller
from controllers.job_controller import job_controller
from controllers.third_party_controller import third_party_controller


logger.basicConfig(format='%(asctime)s %(process)d-%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                   level=logger.DEBUG)
app = Flask(__name__)

app.register_blueprint(reporting_controller)
app.register_blueprint(notification_controller)
app.register_blueprint(job_controller)
app.register_blueprint(third_party_controller)


if __name__ == '__main__':
    port = Config.PORT
    debug = Config.DEBUG
    logger.info('starting helios on port: [{}] at time {}'.format(port, datetime.datetime.now()))
    app.run(port=port, debug=debug)
