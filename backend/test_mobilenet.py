import keras
import numpy as np

try:
    model = keras.applications.MobileNetV2(weights='imagenet')
    # This might take a moment to download if not cached
    print("MobileNetV2 loaded")
except Exception as e:
    print(f"Error loading model: {e}")
