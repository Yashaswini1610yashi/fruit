import torch
from torchvision import models, transforms
from PIL import Image

# Load model
try:
    model = models.mobilenet_v2(weights="IMAGENET1K_V1")
except:
    model = models.mobilenet_v2(pretrained=True)
model.eval()

# Common fruits in ImageNet (using standard indices)
# Some examples:
# 948: Granny Smith
# 949: strawberry
# 950: orange
# 951: lemon
# 952: fig
# 953: pineapple
# 954: banana
# 955: jackfruit
# 956: custard apple
# 957: pomegranate

print("Torchvision MobileNetV2 loaded successfully")
