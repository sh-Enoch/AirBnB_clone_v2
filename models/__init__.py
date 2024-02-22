#!/usr/bin/python3
"""This module initializes the storage mechanism based on environment variable"""

import os
# from models.state import State


# Import necessary storage classes
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload storage after instantiation
storage.reload()
