import numpy as np
from PIL import Image
from backend.config import IMAGE_SIZE

def preprocess_image(image):
    """
    Standard image preprocessing for the fruit model.
    Resizes image to config.IMAGE_SIZE and normalizes pixel values.
    """
    image = image.resize(IMAGE_SIZE)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    image = image.astype(np.float32)
    return image
