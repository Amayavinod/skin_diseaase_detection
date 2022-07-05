import numpy as np
from PIL import Image

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, BatchNormalization, Dropout, Dense, MaxPool2D

def create_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(16, kernel_size = (3,3), input_shape = (28, 28, 3), activation = 'relu', padding = 'same'))
    model.add(tf.keras.layers.MaxPool2D(pool_size = (2,2)))

    model.add(tf.keras.layers.Conv2D(32, kernel_size = (3,3), activation = 'relu', padding = 'same'))
    model.add(tf.keras.layers.MaxPool2D(pool_size = (2,2), padding = 'same'))

    model.add(tf.keras.layers.Conv2D(64, kernel_size = (3,3), activation = 'relu', padding = 'same'))
    model.add(tf.keras.layers.MaxPool2D(pool_size = (2,2), padding = 'same'))
    model.add(tf.keras.layers.Conv2D(128, kernel_size = (3,3), activation = 'relu', padding = 'same'))
    model.add(tf.keras.layers.MaxPool2D(pool_size = (2,2), padding = 'same'))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64, activation = 'relu'))
    model.add(tf.keras.layers.Dense(32, activation='relu'))
    model.add(tf.keras.layers.Dense(7, activation='softmax'))

    optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001)

    model.compile(loss = 'sparse_categorical_crossentropy',
                 optimizer = optimizer,
                  metrics = ['accuracy'])
    print(model.summary())
    return model

model = create_model()
model.load_weights(r'C:\Users\DELL\Desktop\Skin disease Project\prjct\skinClassifier\skin_classifier_model.h5')


def predict(image):
    image = np.asarray(image.resize((28,28)))
    image = image/255
    label = model.predict(np.array( [image,] ))
    return np.argmax(label[0])
