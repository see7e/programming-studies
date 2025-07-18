import logging
import os
import sys


# Disable cs50 logger by default
logging.getLogger("cs50").disabled = True

# Import cs50_*
try:
    from cs50 import get_char, get_float, get_int, get_string
    from cs50 import get_long
except Exception as e:
    print(e)
    pass

# Hook into flask importing
from . import flask

# Wrap SQLAlchemy
from .sql import SQL