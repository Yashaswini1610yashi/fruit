import os
import keras
import numpy as np
from PIL import Image
from backend.config import IMAGE_SIZE

def load_fruit_model(model_path):
    """Loads the Keras model from the specified path."""
    if not os.path.exists(model_path):
        print(f"⚠️ WARNING: {model_path} not found.")
        return None
    
    print(f"🚀 Loading model from {model_path}...")
    model = keras.models.load_model(model_path)
    
    # Warmup
    print("🔥 Warming up model...")
    dummy_input = np.zeros((1, *IMAGE_SIZE, 3), dtype=np.float32)
    model(dummy_input)
    print("✅ Model ready!")
    return model

def preprocess_image(image):
    """Preprocesses a PIL image for the model."""
    image = image.resize(IMAGE_SIZE)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    image = image.astype(np.float32)
    return image
