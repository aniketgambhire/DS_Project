# import libraries
import os
import sys

import dill

# import modules
from src.exception import CustomException

def save_object(file_path, obj)->None:
    """ Store object on local disk for future use """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)