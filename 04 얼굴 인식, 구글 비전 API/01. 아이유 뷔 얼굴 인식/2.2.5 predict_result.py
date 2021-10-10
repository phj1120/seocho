import numpy as np
import cv2, os
import matplotlib.pyplot as plt

from tensorflow.keras import models


model = models.load_model('etc/my_model.h5')

test_path = 'test_image'
test_list = os.listdir(test_path)

for image_name in test_list:
    img = cv2.imread(f'{test_path}/{image_name}')
    s_img = cv2.resize(img, dsize=(28, 28))
    s_img = np.array(s_img)
    s_img = s_img.reshape(1, 28,28, 3)
    
    classes = model.predict(s_img, batch_size=10)
    
    if classes[0]>0:
      result = "IU"
    else:
      result = "V"
    
    plt.figure(figsize=(3,3))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xlabel(result)
    plt.grid(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()