"""
All parameters specific to the application
"""

from os import getenv

PARAMS = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "temperature"),
}
