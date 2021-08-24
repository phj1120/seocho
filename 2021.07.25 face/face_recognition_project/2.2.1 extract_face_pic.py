import numpy as np
import cv2
import os, sys
import uuid

from imutils import paths

faceCascade = cv2.CascadeClassifier('etc/haarcascade_frontalface_alt2.xml')

def make_dir(path):
    try:
      if not os.path.exists(path):
        os.mkdir(path)
    
    except OSError:
        print('Error : Creating directory.' + path)
    
make_dir('crop_img')

# test
# imagePaths = list(paths.list_images('Image'))
# full
imagePaths = list(paths.list_images('full_img'))

# loop over the image paths
count = 1
for (i, img) in enumerate(imagePaths):
    name = img.split(os.path.sep)[-2]
    folder_path = f'crop_img/{name}'
    make_dir(folder_path)
    
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    box = []
    
    for (x, y, w, h) in faces:
        box = (x, y, w, h)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        crop_img = image[y:y + h, x:x + w]
        try:
            # cv2.imshow('img', image)
            # cv2.imshow('crop_img', crop_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            crop_img = cv2.resize(crop_img, dsize=(28,28))
            file_name = f'{folder_path}/{uuid.uuid4()}.jpg'
            cv2.imwrite(file_name, crop_img)
            print(f'Saving {count} : {file_name}')
            count+=1
        except:
            pass
        