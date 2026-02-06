import sys
import os
print("CWD:", os.getcwd())
print("LISTDIR:", os.listdir('.'))
try:
    import backend
    print("SUCCESS: Imported backend from", backend.__file__)
except Exception as e:
    print("FAILURE IMPORTING backend:", e)

try:
    from backend import config
    print("SUCCESS: Imported backend.config")
except Exception as e:
    print("FAILURE IMPORTING backend.config:", e)
