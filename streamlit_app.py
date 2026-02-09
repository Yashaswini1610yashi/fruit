import streamlit as st
import os
import sys
from PIL import Image
import numpy as np

# Set Keras backend to Torch BEFORE importing keras
os.environ["KERAS_BACKEND"] = "torch"

# Add current directory to path
curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.insert(0, curr_dir)

# Import backend modules
try:
    from backend.config import MODEL_PATH
    from backend.model_impl.model_loader import load_fruit_model
    from backend.preprocessing.image_preprocess import preprocess_image
except ImportError:
    st.error("❌ Could not import backend modules. Ensure the project structure is intact.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="FruitAI - Quality Recognition",
    page_icon="🍎",
    layout="centered",
)

# Custom CSS for rich aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: none;
        transform: scale(1.02);
    }
    .prediction-card {
        padding: 2rem;
        border-radius: 15px;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 2rem;
    }
    .fresh { color: #28a745; font-size: 2.5rem; font-weight: bold; }
    .rotten { color: #dc3545; font-size: 2.5rem; font-weight: bold; }
    .confidence { color: #6c757d; font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

# App Title & Header
st.title("🍎 FruitAI Quality Recognition")
st.markdown("---")
st.markdown("### Upload a fruit image to check its quality")

# Load model with caching
@st.cache_resource
def get_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at {MODEL_PATH}. Please ensure `backend/model.keras` exists.")
        return None
    return load_fruit_model(MODEL_PATH)

model = get_model()

# Sidebar info
with st.sidebar:
    st.header("About FruitAI")
    st.info("This AI model recognizes whether a fruit is Fresh or Rotten using deep learning (MobileNetV2).")
    st.markdown("### How to use:")
    st.markdown("1. Upload an image of a fruit.\n2. Wait for the AI to process.\n3. Get the quality result and confidence.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption='Uploaded Fruit Image', use_container_width=True)
    
    if st.button("Analyze Quality"):
        if model is None:
            st.error("Model is not loaded. Cannot perform prediction.")
        else:
            with st.spinner('🚀 Analyzing quality...'):
                try:
                    # Preprocess
                    processed_image = preprocess_image(image)
                    
                    # Predict
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
                        css_class = "rotten"
                    else:
                        result = "Fresh"
                        confidence = (1 - prediction) * 100
                        css_class = "fresh"

                    # Display result in a nice card
                    st.markdown(f"""
                    <div class="prediction-card">
                        <h3>Result:</h3>
                        <p class="{css_class}">{result}</p>
                        <p class="confidence">Confidence: {confidence:.2f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if result == "Fresh":
                        st.balloons()

                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")

else:
    st.info("Please upload an image to start analysis.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6c757d;'>Built with ❤️ by FruitAI Team</p>", unsafe_allow_html=True)
