import os
import numpy as np
from PIL import Image

def generate_random_images(directory, count=5):
    os.makedirs(directory, exist_ok=True)
    for i in range(count):
        # Create a random RGB image of 224x224
        random_data = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        img = Image.fromarray(random_data)
        img.save(os.path.join(directory, f"image_{i}.jpg"))

base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(base_dir, "dataset")

# Train set
generate_random_images(os.path.join(dataset_dir, "train", "fresh"), 16)
generate_random_images(os.path.join(dataset_dir, "train", "rotten"), 16)

# Validation set
generate_random_images(os.path.join(dataset_dir, "validation", "fresh"), 8)
generate_random_images(os.path.join(dataset_dir, "validation", "rotten"), 8)

print("✅ Dummy dataset created.")
