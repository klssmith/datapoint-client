import logging
from logging import NullHandler

# Doing it this way makes the logger None
# logger = logging.getLogger(__name__).addHandler(NullHandler())

handler = NullHandler()
logger = logging.getLogger(__name__)
logger.addHandler(handler)
