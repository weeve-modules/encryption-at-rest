"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""
from .params import PARAMS
from logging import getLogger
from cryptography.fernet import Fernet
import numpy as np
from scipy.stats import entropy
import json

log = getLogger("module")


def get_entropy(labels):
    log.debug("Calculating entropy...")
    _, counts = np.unique(list(labels), return_counts=True)
    return entropy(counts, base=len(counts))


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        value = received_data[PARAMS["INPUT_LABEL"]]

        NUM_VALUES = 2621440
        MAX_DEVIATION = 1

        log.info("Extrapolating the input data...")
        random_values = list(
            (value - MAX_DEVIATION) * np.ones(NUM_VALUES)
            + np.random.random_sample((NUM_VALUES,)) * MAX_DEVIATION * 2
        )
        new_dict = {PARAMS["INPUT_LABEL"]: random_values}
        data_str = json.JSONEncoder().encode(new_dict)

        log.info(
            "Extrapolated "
            + str(NUM_VALUES / (1024 * 1024))
            + "MB of values with max deviation of "
            + str(MAX_DEVIATION)
        )

        decrypted_entropy = get_entropy(data_str)

        log.info("Decrypted entropy: " + str(decrypted_entropy))

        log.debug("Generating the encryption key...")
        key = Fernet.generate_key()

        log.debug("Key generated successfully")
        f = Fernet(key)

        log.debug("Encrypting...")
        encrypted_data = f.encrypt(bytes(data_str, encoding="ascii"))

        log.debug("Encrypted.")
        encrypted_entropy = get_entropy(encrypted_data)

        log.info("Encrypted entropy: " + str(encrypted_entropy))
        return received_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
