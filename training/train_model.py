import os
import keras
from keras import layers
import numpy as np

def build_model(input_shape=(128, 128, 3)):
    """Constructs a CNN model for fruit quality classification."""
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(32, (3,3), activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        
        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D(),
        
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

if __name__ == "__main__":
    print("🏗️ Building CNN Model...")
    model = build_model()
    model.summary()
    print("✅ Model built successfully. Use this script as part of your training pipeline.")
