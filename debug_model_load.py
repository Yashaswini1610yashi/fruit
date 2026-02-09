import os
import sys

# Set Keras backend to Torch
os.environ["KERAS_BACKEND"] = "torch"

try:
    import keras
    import numpy as np
    print(f"Keras Version: {keras.__version__}")
    print(f"Keras Backend: {keras.backend.backend()}")
    
    MODEL_PATH = os.path.join(os.getcwd(), "backend", "model.keras")
    print(f"Attempting to load model from: {MODEL_PATH}")
    
    if not os.path.exists(MODEL_PATH):
        print(f"ERROR: Model file not found at {MODEL_PATH}")
        sys.exit(1)
        
    print("\n--- Attempt 1: Default load_model ---")
    try:
        model = keras.models.load_model(MODEL_PATH)
        print("✅ Attempt 1 Success!")
    except Exception as e:
        print(f"❌ Attempt 1 Failed: {str(e)}")
        
    print("\n--- Attempt 2: load_model(compile=False) ---")
    try:
        model = keras.models.load_model(MODEL_PATH, compile=False)
        print("✅ Attempt 2 Success!")
        
        # Test a prediction
        dummy_input = np.zeros((1, 128, 128, 3), dtype=np.float32)
        output = model(dummy_input)
        print(f"✅ Prediction Test Success! Output shape: {output.shape}")
    except Exception as e:
        print(f"❌ Attempt 2 Failed: {str(e)}")

except ImportError as e:
    print(f"Import Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
