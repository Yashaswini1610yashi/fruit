import os

# Base Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")

# Model Configuration
# Note: Currently the model is in the backend root as model.keras
# We will eventually move it to backend/model/ fruit_model.h5
MODEL_PATH = os.path.join(BASE_DIR, "model.keras")
IMAGE_SIZE = (128, 128)

# Upload Configuration
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Prediction Labels
# Based on current app.py logic: > 0.5 is Rotten, <= 0.5 is Fresh
CLASS_NAMES = ["Fresh", "Rotten"]

# Server Configuration
PORT = 5000
DEBUG = False
THREADED = False
