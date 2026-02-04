import kagglehub
import shutil
import os
from organize_utils import organize

# Download latest version
print("🚀 Starting download from Kaggle (this may take a few minutes)...")
path = kagglehub.dataset_download("sriramr/fruits-fresh-and-rotten-for-classification")

print("✅ Downloaded to:", path)

# Define project dataset paths
base_dir = os.path.dirname(os.path.abspath(__file__))
project_dataset_dir = os.path.join(base_dir, "dataset")

# Ensure dataset directory is clean for new data
if os.path.exists(project_dataset_dir):
    shutil.rmtree(project_dataset_dir)
os.makedirs(project_dataset_dir)

print("📦 Organizing files...")
organize(path, project_dataset_dir)
print("✨ Dataset ready in", project_dataset_dir)
