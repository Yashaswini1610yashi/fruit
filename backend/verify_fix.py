import requests
import numpy as np
from PIL import Image
import io

# URL of the running server
url = "http://127.0.0.1:5000/predict"

# 1. Create a dummy image with the EXACT dimensions that caused the error
# Error said: torch.Tensor(shape=(1, 769, 1079, 3))
width = 1079
height = 769
print(f"📉 Generating dummy image of size {width}x{height} (Simulating the error case)...")

# Create random RGB image
img_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
img = Image.fromarray(img_array)

# Save to memory buffer
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr.seek(0)

# 2. Send to backend
print(f"🚀 Sending image to {url}...")
try:
    files = {'image': ('error_test.png', img_byte_arr, 'image/png')}
    response = requests.post(url, files=files)
    
    # 3. Check result
    if response.status_code == 200:
        print("✅ SUCCESS! Server handled the large image correctly.")
        print("Response:", response.json())
    else:
        print(f"❌ FAILED. Status Code: {response.status_code}")
        print("Error:", response.text)

except Exception as e:
    print(f"❌ Connection Error: {e}")
