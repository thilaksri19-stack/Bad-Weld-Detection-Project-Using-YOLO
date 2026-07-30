# 🔥 Weld Defect Detection using YOLOv8

An AI-powered Computer Vision project that automatically detects welding defects and classifies weld quality as **Good** or **Defective** using the YOLOv8 object detection model.

---

## 📖 Project Overview

Manual weld inspection is often time-consuming and prone to human error. This project leverages **YOLOv8**, a state-of-the-art object detection model, to automate the inspection process by detecting weld defects from images.

The model identifies different weld conditions and generates a final binary prediction:

- ✅ Good Weld
- ❌ Defective Weld

This solution can help improve manufacturing quality control by providing fast and reliable weld inspection.

---

## 🎯 Objectives

- Detect weld defects using Deep Learning.
- Classify welds into Good or Defective categories.
- Generate confidence scores for predictions.
- Visualize detections with bounding boxes.
- Export predictions in JSON format for integration with other applications.

---

## 📂 Project Structure

```text
Weld-Defect-Detection/
│
├── datasets/
│   ├── train/
│   ├── valid/
│   └── test/
│
├── runs/
│   └── detect/
│
├── data.yaml
├── dataset_check.py
├── inference.py
├── prediction.json
├── requirements.txt
└── README.md
```

---

## 🗂 Dataset Information

The dataset contains three object classes:

| Class ID | Class Name | Final Category |
|----------|------------|----------------|
| 0 | Bad Weld | Defective |
| 1 | Good Weld | Good |
| 2 | Defect | Defective |

The model converts these three classes into a binary classification:

- **Good Weld → Good**
- **Bad Weld + Defect → Defective**

---

## ⚙️ Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- JSON
- Deep Learning
- Computer Vision

---

## 🚀 Workflow

1. Load the trained YOLOv8 model.
2. Read the input weld image.
3. Detect weld regions and defects.
4. Draw bounding boxes around detected objects.
5. Calculate confidence scores.
6. Generate the final Good/Defective prediction.
7. Save the prediction as a JSON file.

---

## 📊 Dataset Validation

The project includes a dataset validation script (`dataset_check.py`) that:

- Reads YOLO annotation files.
- Counts Good Weld samples.
- Counts Defective Weld samples.
- Helps verify class distribution before model training.

---

## 🔍 Model Inference

The inference script performs the following operations:

- Loads the trained YOLOv8 model.
- Detects weld defects in an input image.
- Assigns confidence scores to detections.
- Determines the final weld quality.
- Displays the image with bounding boxes.
- Exports prediction results to a JSON file.

---

## 📄 Sample JSON Output

```json
{
    "class": "good",
    "confidence": 0.6499
}
```

---

## 📈 Output

The model provides:

- Bounding box visualization
- Detected class labels
- Confidence scores
- Final weld quality prediction
- JSON output for further processing

---

## 💡 Applications

- Industrial Quality Inspection
- Manufacturing Automation
- Smart Factory Systems
- Robotic Welding Inspection
- Production Line Monitoring

---

## 📚 Skills Demonstrated

- Object Detection
- Computer Vision
- Deep Learning
- YOLOv8
- OpenCV
- Python Programming
- Dataset Preparation
- Image Processing
- Model Inference
- JSON Data Handling

---

## 🔮 Future Enhancements

- Real-time camera-based detection
- Streamlit web application
- Flask/FastAPI deployment
- Cloud deployment
- Edge AI implementation
- Mobile application support

---

## 📌 Learning Outcomes

Through this project, I gained practical experience in:

- Training custom YOLOv8 models
- Preparing and validating datasets
- Object detection using Computer Vision
- Image preprocessing
- Deep Learning model inference
- Real-world industrial AI applications

---

## 👨‍💻 Author

**V. Thilak Sri**

**Aspiring Data Scientist | Machine Learning Engineer | Computer Vision Enthusiast**

### Connect with Me

- 💼 LinkedIn: *www.linkedin.com/in/thilak-sri-788315407*
- 💻 GitHub: *Add your GitHub profile*

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub!

---

### 📌 Key Highlights

- End-to-End Computer Vision Project
- Custom YOLOv8 Object Detection Model
- Automated Weld Quality Inspection
- Binary Classification (Good vs Defective)
- Industrial Manufacturing Use Case
- JSON-Based Prediction Output
- Real-World AI Application
