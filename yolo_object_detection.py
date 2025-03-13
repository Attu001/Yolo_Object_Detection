import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load YOLO Model (using torch, ONNX, or TensorFlow backend)
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Use a YOLOv8 pretrained model



# Load Image
image_path = str(input("Enter the path of the image: "))
image = Image.open(image_path)

# Convert image to NumPy array
img_array = np.array(image)

# Run object detection
results = model(img_array)

# Draw bounding boxes using PIL
draw = ImageDraw.Draw(image)
for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=3)

# Show the image using Matplotlib
plt.imshow(image)
plt.axis("off")
plt.show()
