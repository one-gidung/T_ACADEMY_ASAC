from models import Yolov4
import cv2

model -= Yolov4(weight_path="yolov4.weights",
    class_name_path='class_names.coco_clasdss.txt')
img, df  =model.predict('street_view.jpg')
