# Fruit Quality Recognition System 🍎🍌🍊

An AI-powered web application that uses Deep Learning to classify fruits as "Fresh" or "Rotten". Built with a Keras/Torch backend and a modern, responsive frontend.

## 🚀 Key Features
- **Real-time Prediction**: Instantly classify fruit quality with high confidence.
- **Deep Learning Core**: Powered by a Convolutional Neural Network (CNN) with Keras 3.
- **Modern UI**: A sleek, dark-themed dashboard with smooth animations and interactive data visualization.
- **Modular Architecture**: Clean separation between backend logic, frontend modules, and documentation.

## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Chart.js, FontAwesome.
- **Backend**: Python, Flask, Flask-CORS.
- **AI/ML**: Keras 3 (Torch Backend), NumPy, Pillow, OpenCV.

## 📁 Project Structure
- `backend/`: Flask server and utility modules.
- `frontend/`: Interactive web interface.
- `docs/`: Technical documentation and dataset details.
- `training/`: Scripts for model development and evaluation.

## 🏃 How to Run
1. **Install Dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. **Train the Model** (Optional, if `model.keras` is missing):
   ```bash
   python backend/train_model.py
   ```
3. **Start the Server**:
   ```bash
   python backend/app.py
   ```
4. **View the App**: Open `http://localhost:5000` in your browser.

## 👨‍💻 Developed By
Developed by the AntiGravity Team for Advanced Agentic Coding.
