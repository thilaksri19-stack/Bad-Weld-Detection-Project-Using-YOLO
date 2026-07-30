import time
from ultralytics import YOLO
import cv2
 
model = YOLO("runs/detect/yolo_weld_detection_project/weld_yolo_training/weights/best.pt")          # or the full runs/... path
 
image = cv2.imread("datasets\test\images\bad_weld_vid261_jpeg_jpg.rf.5ae3866fd5de7b144659fa7f7b92c5ba.jpg")
 
start = time.time()
results = model(image)
end = time.time()
 
latency = end - start
print("Inference Time:", latency, "seconds")
