import os

def save_trained_model(model, filename="fruit_model.h5"):
    """Saves the Keras model to the specified filename."""
    save_path = os.path.join(os.path.dirname(__file__), filename)
    model.save(save_path)
    print(f"💾 Model saved to: {save_path}")

if __name__ == "__main__":
    print("📦 Model saving utility ready.")
