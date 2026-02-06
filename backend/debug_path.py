import sys
import os
print("CWD:", os.getcwd())
print("SYS PATH:", sys.path)
try:
    import model
    print("SUCCESS: Imported model from", model.__file__)
except Exception as e:
    print("FAILURE:", e)
