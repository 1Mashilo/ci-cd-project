"""
Service Package
"""

from service import routes  # Move imports to the top 
from service.common import log_handlers

from flask import Flask

app = Flask(__name__)

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
