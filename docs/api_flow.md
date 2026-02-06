# API Flow & Documentation

This document outlines the communication flow between the Frontend and the Backend API.

## 🔄 Prediction Flow
1. **User Action**: The user selects or drags an image into the `upload.html` interface.
2. **Frontend Loading**: `upload.js` displays a preview and stores the image locally.
3. **API Call**: `predict.js` sends a `POST` request to `/predict` containing the image file as `multipart/form-data`.
4. **Backend Processing**: 
   - `app.py` receives the request.
   - `model_loader.py` preprocesses the image and runs inference via the Keras model.
   - `response_formatter.py` packages the result and confidence score.
5. **JSON Response**: The server returns a 200 OK with the classification data.
6. **Visualization**: `result.html` receives the data, displays the classification, and `chart.js` animates a confidence gauge.

## 📡 Endpoints

### `POST /predict`
Submits an image for classification.
- **Request Body**: `image` (File)
- **Response Format**:
  ```json
  {
    "result": "Fresh",
    "confidence": 98.45
  }
  ```

### `GET /`
Serves the main `index.html` landing page.
