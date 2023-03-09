import sys

from src.data.download_data import get_file_count
import tensorflow as tf
from tensorflow import keras

REQUIRED_PYTHON = "python3"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))

    if tf.__version__ < "2.8.0":
        raise TypeError(
            "This project requires Tensorflow 2.8.0 or higher. Found: Tensorflow {}".format(
                tf.__version__))
    if keras.__version__ < "2.8.0":
        raise TypeError(
            "This project requires Keras 2.8.0 or higher. Found: Keras {}".format(
                keras.__version__))

    try:
        assert get_file_count("data") > 0
    except Exception as e:
        raise e

    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
