"""
All logic related to the module's main application
Mostly only this file requires changes
"""

from logging import getLogger, DEBUG
from app.config import APPLICATION
from cryptography.fernet import Fernet
import numpy as np
from scipy.stats import entropy
import json


log = getLogger("business")

def get_entropy(labels):
    _, counts = np.unique(list(labels), return_counts=True)
    return entropy(counts, base=len(counts))

def module_main(data):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [[JSON Object], string]: [data, error]
    """
    log.setLevel(DEBUG)

    try:
        log.debug("At the start of business main.")

        value = data[APPLICATION['INPUT_LABEL']]

        NUM_VALUES = 1000000
        MAX_DEVIATION = 1
        random_values = list((value - MAX_DEVIATION) * np.ones(NUM_VALUES) + np.random.random_sample((NUM_VALUES,)) * MAX_DEVIATION * 2)
        new_dict = {APPLICATION['OUTPUT_LABEL']: random_values}
        data_str = json.JSONEncoder().encode(new_dict)

        log.debug("1")
        decrypted_entropy = get_entropy(data_str)

        log.debug("2")
        log.warning("Decrypted entropy: " + str(decrypted_entropy))

        log.debug("3")
        key = Fernet.generate_key()

        log.debug("4")
        f = Fernet(key)

        log.debug("5")
        encrypted_data = f.encrypt(bytes(data_str, encoding='ascii'))

        log.debug("6")
        encrypted_entropy = get_entropy(encrypted_data)

        log.debug("7")
        log.warning("Encrypted entropy: " + str(encrypted_entropy))

        log.debug("At the end of business main.")
        return data, None
    except Exception as e:
        log.error("Error in the module logic: {}".format(e))
        return None, "Unable to perform the module logic"

if __name__ == "__main__":
    _, b = module_main([])
    print(b)
