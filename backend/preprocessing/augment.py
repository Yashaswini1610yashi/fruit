import numpy as np
import cv2

def apply_augmentation(image_np):
    """
    Applies basic data augmentation to a numpy image.
    Used during training or for robust testing.
    """
    # Random horizontal flip
    if np.random.rand() > 0.5:
        image_np = np.flip(image_np, axis=1)
        
    # Subtle brightness adjustment
    brightness = 1.0 + (np.random.rand() - 0.5) * 0.2
    image_np = np.clip(image_np * brightness, 0, 1)
    
    return image_np
