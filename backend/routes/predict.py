import os
import sys
from flask import Blueprint, request
from PIL import Image

from backend.config import UPLOAD_FOLDER, MODEL_PATH
from backend.model_impl.model_loader import load_fruit_model
from backend.preprocessing.image_preprocess import preprocess_image
from backend.utils.response_formatter import format_prediction_response, format_error_response

predict_bp = Blueprint('predict', __name__)

# Load the model once
model = load_fruit_model(MODEL_PATH)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return format_error_response("Model not loaded. Please train the model first.", 500)
        
    if "image" not in request.files:
        return format_error_response("No image uploaded", 400)

    file = request.files["image"]
    if file.filename == "":
        return format_error_response("No selected file", 400)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    try:
        image = Image.open(path).convert("RGB")
        processed_image = preprocess_image(image)

        # Keras 3 with Torch backend
        output_tensor = model(processed_image, training=False)
        
        # Extract prediction value
        if hasattr(output_tensor, "detach"):
             prediction = output_tensor.detach().cpu().numpy()[0][0]
        else:
             prediction = output_tensor.numpy()[0][0]

        # Logic for Fresh vs Rotten
        if prediction > 0.5:
            result = "Rotten"
            confidence = prediction * 100
        else:
            result = "Fresh"
            confidence = (1 - prediction) * 100

        return format_prediction_response(result, confidence)

    except Exception as e:
        print(f"❌ Error during prediction: {str(e)}")
        return format_error_response(str(e), 500)
