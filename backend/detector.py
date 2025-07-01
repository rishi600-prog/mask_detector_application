# backend/detector.py
import cv2
import numpy as np
import os

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

maskColors = [
    ((90, 50, 70), (128, 255, 255)),
    ((36, 50, 70), (89, 255, 255)),
    ((0, 0, 180), (180, 50, 255)),
    ((0, 0, 0), (180, 255, 50))
]

def detect_mask(image_path, output_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))

    for (x, y, w, h) in faces:
        hsvFace = hsv[y:y + h, x:x + w]
        maskDetected = any(
            np.sum(cv2.inRange(hsvFace, np.array(lower), np.array(upper)) > 0) / (w * h) > 0.2
            for lower, upper in maskColors
        )

        label = "Mask" if maskDetected else "No Mask"
        color = (0, 255, 0) if maskDetected else (0, 0, 255)

        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    cv2.imwrite(output_path, image)
