import cv2
import numpy as np
from urllib.request import urlopen

def blur_background(image_path, name):
    req = urlopen(image_path)
    image_arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(image_arr, 3)

    cv2.imwrite(name+"_original.png", image)
    blurred_img = cv2.GaussianBlur(image, (21, 21), 0)

    img_width, img_height, _ = image.shape
    mask = np.zeros((img_width, img_height, 3), dtype=np.uint8)

    # Detect the facial region
    faceCascade = cv2.CascadeClassifier('/model/haarcascade_frontalface_alt.xml')
    faces = faceCascade.detectMultiScale(image, 1.3, 5)
    if len(faces) == 0:
        print("no face found")
        return "no face found"

    # Get facial coordinates and blur the background
    (x,y,w,h) = faces[0]
    mask = cv2.circle(mask, (int((2*x+w)/2), int((2*y+h)/2)), int(h/2)+10, (255, 255, 255), -1)
    out = np.where(mask==np.array([255, 255, 255]), image, blurred_img)

    cv2.imwrite(name+"_blurred.png", out)
    return
