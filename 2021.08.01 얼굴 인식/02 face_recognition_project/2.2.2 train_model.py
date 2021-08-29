import numpy as np
import tensorflow as tf
import cv2, os
import matplotlib.pyplot as plt

from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop

base_dir = 'crop_img'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_IU_dir = os.path.join(train_dir, 'IU')
train_V_dir = os.path.join(train_dir, 'V')
print(train_IU_dir)
print(train_V_dir)


validation_IU_dir = os.path.join(validation_dir, 'IU')
validation_V_dir = os.path.join(validation_dir, 'V')
print(validation_IU_dir)
print(validation_V_dir)

train_IU_fnames = os.listdir( train_IU_dir )
train_V_fnames = os.listdir( train_V_dir )

print(train_IU_fnames[:5])
print(train_V_fnames[:5])

print('Total training IU images :', len(os.listdir(train_IU_dir)))
print('Total training V images :', len(os.listdir(train_V_dir)))

print('Total validation IU images :', len(os.listdir(validation_IU_dir)))
print('Total validation V images :', len(os.listdir(validation_V_dir)))

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(28, 28, 3)),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(optimizer=RMSprop(lr=0.001),
            loss='binary_crossentropy',
            metrics = ['accuracy'])



train_datagen = ImageDataGenerator( rescale = 1.0/255. )
test_datagen  = ImageDataGenerator( rescale = 1.0/255. )



train_generator = train_datagen.flow_from_directory(train_dir,
                                                  batch_size=20,
                                                  class_mode='binary',
                                                  target_size=(28, 28))
print(train_generator)

validation_generator =  test_datagen.flow_from_directory(validation_dir,
                                                       batch_size=20,
                                                       class_mode  = 'binary',
                                                       target_size = (28, 28))

history = model.fit(train_generator,
                    validation_data=validation_generator,
                    epochs=100,
                    validation_steps=50,
                    verbose=2)

model.save('etc/my_model.h5')