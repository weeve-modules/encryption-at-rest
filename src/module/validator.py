"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

from logging import getLogger
from .params import PARAMS

log = getLogger("validator")


def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        # YOUR CODE HERE

        allowed_data_types = [dict]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"

        # check if data contains required label
        if type(data) == dict and not PARAMS["INPUT_LABEL"] in data:
            return f"Data does not contain required label: {PARAMS['INPUT_LABEL']}."

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"
