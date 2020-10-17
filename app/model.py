# -*- coding: UTF-8 -*-


from keras.models import load_model
import numpy as np




model = load_model('app/model/mnist_model.h5')

def predict(input):
    input = np.expand_dims(input, axis=0)
    result = model.predict(input)
    num = (np.where(result==np.max(result[0]))[1])[0]
    print(num)
    return num

