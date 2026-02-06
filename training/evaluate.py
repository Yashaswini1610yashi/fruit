import keras
import numpy as np

def evaluate_model(model, val_gen):
    """Evaluates the model on the validation generator."""
    print("📊 Evaluating model performance...")
    loss, accuracy = model.evaluate(val_gen)
    print(f"✅ Loss: {loss:.4f}")
    print(f"✅ Accuracy: {accuracy:.4f}")
    return loss, accuracy

if __name__ == "__main__":
    print("🔍 Evaluation script ready. Run with valid data generators.")
