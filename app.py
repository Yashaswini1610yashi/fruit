import os
import sys

# Add the current directory to sys.path to ensure absolute imports work
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Set Keras backend to Torch
os.environ["KERAS_BACKEND"] = "torch"

from flask import Flask
from flask_cors import CORS

# Import custom modules
from backend.config import FRONTEND_DIR, PORT, DEBUG, THREADED
from backend.routes.predict import predict_bp

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app) 

# Register Blueprints
app.register_blueprint(predict_bp)

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    print(f"⚡ Starting FruitAI Flask Server on port {PORT}...")
    app.run(host="0.0.0.0", debug=DEBUG, port=PORT, threaded=THREADED)
