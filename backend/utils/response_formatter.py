from flask import jsonify

def format_prediction_response(result, confidence):
    """Formats the prediction results into a JSON-ready dictionary."""
    return jsonify({
        "result": result,
        "confidence": round(float(confidence), 2)
    })

def format_error_response(message, status_code=400):
    """Formats an error message into a JSON-ready dictionary."""
    return jsonify({"error": message}), status_code
