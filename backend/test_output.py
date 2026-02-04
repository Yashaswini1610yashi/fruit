import requests
import os

# The backend is running on port 5000
url = "http://127.0.0.1:5000/predict"
image_path = r"c:\Users\yy291\.gemini\antigravity\scratch\fruit-quality-recognition\backend\dataset\validation\fresh\freshapples_Screen Shot 2018-06-08 at 4.59.44 PM.png"

if not os.path.exists(image_path):
    print(f"❌ Image not found at {image_path}")
    exit(1)

print(f"🚀 Sending image {os.path.basename(image_path)} to backend...")

with open(image_path, "rb") as img_file:
    files = {"image": img_file}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print("✅ Result received:")
    print(response.json())
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)
