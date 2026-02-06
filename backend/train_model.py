import os
import numpy as np
import cv2
os.environ["KERAS_BACKEND"] = "torch"
import keras

class FruitDataset(keras.utils.PyDataset):
    def __init__(self, directory, image_size=(224, 224), batch_size=32, **kwargs):
        super().__init__(**kwargs)
        self.directory = directory
        self.image_size = image_size
        self.batch_size = batch_size
        self.class_names = sorted(os.listdir(directory))
        self.file_paths = []
        self.labels = []
        
        for i, class_name in enumerate(self.class_names):
            class_dir = os.path.join(directory, class_name)
            for file_name in os.listdir(class_dir):
                self.file_paths.append(os.path.join(class_dir, file_name))
                self.labels.append(i)
                
        self.indices = np.arange(len(self.file_paths))
        np.random.shuffle(self.indices)

    def __len__(self):
        return int(np.ceil(len(self.file_paths) / self.batch_size))

    def __getitem__(self, idx):
        batch_indices = self.indices[idx * self.batch_size : (idx + 1) * self.batch_size]
        batch_x = []
        batch_y = []
        
        for i in batch_indices:
            img_path = self.file_paths[i]
            img = cv2.imread(img_path)
            if img is None: continue
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, self.image_size)
            
            # Simple Data Augmentation
            if np.random.rand() > 0.5:
                img = cv2.flip(img, 1) # Horizontal flip
            
            batch_x.append(img / 255.0)
            batch_y.append(self.labels[i])
            
        return np.array(batch_x, dtype=np.float32), np.array(batch_y, dtype=np.float32)

    def on_epoch_end(self):
        np.random.shuffle(self.indices)



from config import IMAGE_SIZE, CLASS_NAMES

BATCH_SIZE = 32

base_dir = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.join(base_dir, "dataset/train")
val_dir = os.path.join(base_dir, "dataset/validation")

print("🚀 Loading dataset...")
train_gen = FruitDataset(train_dir, image_size=IMAGE_SIZE, batch_size=BATCH_SIZE)
val_gen = FruitDataset(val_dir, image_size=IMAGE_SIZE, batch_size=BATCH_SIZE)

print(f"✅ Found {len(train_gen.file_paths)} files in training and {len(val_gen.file_paths)} files in validation.")

print("🏗️ Building model...")
model = keras.Sequential([
    keras.layers.Input(shape=(128, 128, 3)),
    keras.layers.Conv2D(32, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.2), # Dropout to prevent overfitting
    
    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.2),
    
    keras.layers.Conv2D(128, (3,3), activation='relu'), # Extra layer
    keras.layers.MaxPooling2D(),
    
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("🏋️ Starting training...")
# Train for more epochs to improve accuracy
model.fit(train_gen, validation_data=val_gen, epochs=10)

model.save("model.keras")
print("✅ Model saved as model.keras")
