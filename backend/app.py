import os
# Set backend before importing keras
os.environ["KERAS_BACKEND"] = "torch"

from flask import Flask, request, jsonify
from flask_cors import CORS
import keras
from PIL import Image
import numpy as np

# Set paths relative to this file
base_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(os.path.dirname(base_dir), "frontend")

app = Flask(__name__, static_folder=frontend_dir, static_url_path="")
CORS(app) # Enable CORS for all routes

@app.route("/")
def index():
    return app.send_static_file("index.html")

# Load model relative to current file
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "model.keras")

if os.path.exists(model_path):
    print(f"🚀 Loading model from {model_path}...")
    model = keras.models.load_model(model_path)
    
    # Warmup the model to prevent slow first prediction
    print("🔥 Warming up model...")
    dummy_input = np.zeros((1, 128, 128, 3), dtype=np.float32)
    model(dummy_input) # Run one pass
    print("✅ Model ready!")
else:
    model = None
    print(f"⚠️ WARNING: {model_path} not found. Please run train_model.py first.")

UPLOAD_FOLDER = os.path.join(base_dir, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def preprocess_image(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    # Ensure it's a float32 array
    image = image.astype(np.float32)
    return image

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Please train the model first."}), 500
        
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    try:
        image = Image.open(path).convert("RGB")
        image = preprocess_image(image)

        print(f"DEBUG: Image shape before inference: {image.shape}")
        
        # Keras 3 with Torch backend
        # Note: model(image) returns a torch Tensor
        # We must detach from graph before converting to numpy
        output_tensor = model(image, training=False)
        if hasattr(output_tensor, "detach"):
             prediction = output_tensor.detach().cpu().numpy()[0][0]
        else:
             prediction = output_tensor.numpy()[0][0]

        if prediction > 0.5:
            result = "Rotten"
            confidence = prediction * 100
        else:
            result = "Fresh"
            confidence = (1 - prediction) * 100

        return jsonify({
            "result": result,
            "confidence": round(float(confidence), 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run in single-threaded mode to prevent Model/TensorFlow/Torch deadlocks
    # This often fixes "hanging" requests on Windows/Flask
    print("⚡ Starting Flask in single-threaded mode...")
    app.run(debug=False, port=5000, threaded=False)
