# 🚀 YOLO Object Detection

## 🔥 Introduction
Welcome to **YOLO (You Only Look Once) Object Detection**! 🦾 This project brings you real-time object detection at lightning-fast speeds using deep learning.

## ✨ Features
✅ **Supports Multiple YOLO Models** - YOLOv3, YOLOv4, YOLOv5, and YOLOv8 🧠  
✅ **Works with Images, Videos** - Detect objects anywhere🌍  
✅ **Built with OpenCV & Deep Learning** - Optimized for performance ⚡  

---

## 📥 Installation
### 🔹 Prerequisites
Before you get started, make sure you have the following installed:
- 🐍 **Python (>= 3.7)**
- 📸 **OpenCV**
- 🔢 **NumPy**
- 🤖 **PyTorch (for YOLOv5)**

### 🔹 Clone the Repository
```sh
git clone https://github.com/Attu001/Yolo_Object_Detection.git
cd Yolo_Object_Detection
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🚀 How to Use
### 🖼️ Run YOLO on an Image
```sh
python detect.py --source images/sample.jpg --weights yolov5s.pt --conf 0.4
```

### 🎥 Run YOLO on a Video
```sh
python detect.py --source videos/sample.mp4 --weights yolov5s.pt --conf 0.4
```

### 📹 Run YOLO with Live Webcam
```sh
python detect.py --source 0 --weights yolov5s.pt --conf 0.4
```

---

## ⚙️ Configuration
You can tweak settings in **config.yaml** to:
- 🏋️‍♂️ **Change Model Weights**
- 🎯 **Adjust Confidence Threshold**
- 🔍 **Modify IOU Threshold**
- 💾 **Set Output Directory**

---

## 🏆 Supported Models
🚀 This project supports multiple YOLO versions, including:
- **YOLOv3** 🏆
- **YOLOv4** 🔥
- **YOLOv5** ⚡
- **YOLOv8** (with modifications) 🎯

---

## 🎯 Output
📂 Detected images and videos will be saved in the `output/` folder.

---

## 🤝 Contributing
🚀 Want to make YOLO even better? Fork this repo, make your changes, and send a pull request! 💡

---

## 📜 License
This project is licensed under the **MIT License** 📜.

---

## 📧 Contact
Got questions? Need help? Open an issue on [GitHub Issues](https://github.com/Attu001/Yolo_Object_Detection/issues) 🚀.

