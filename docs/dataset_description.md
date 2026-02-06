# Dataset Description

The Fruit Quality Recognition system is trained on a curated collection of fruit images categorized into two primary classes: **Fresh** and **Rotten**.

## 📦 Dataset Composition
The dataset is split into training and validation sets:
- **Training Set**: Used to teach the model patterns of freshness and decay.
- **Validation Set**: Used to evaluate the model's accuracy on unseen data.

## 🍎 Supported Fruit Types
The model currently provides robust support for:
1. **Apples** (Fresh vs. Rotten)
2. **Bananas** (Fresh vs. Rotten)
3. **Oranges** (Fresh vs. Rotten)

## 🏗️ Data Structure
- `dataset/train/`: Subdirectories for each class containing training images.
- `dataset/validation/`: Subdirectories for each class containing validation images.

## ⚙️ Preprocessing Details
- **Resolution**: All images are resized to 128x128 pixels.
- **Normalization**: Pixel values are scaled to the range [0, 1].
- **Augmentation**: Techniques like horizontal flipping are applied during training to improve generalization.
