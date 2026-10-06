import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy


X = np.array([[1,3,5],[5,6,8]])
y = np.array([[2,4]])

model = Sequential([
    Dense(25,activation='sigmoid'),
    Dense(15 , activation='sigmoid'),
    Dense(1,activation='sigmoid')
])

model.compile(loss=BinaryCrossentropy())

model.fit(X,y,epochs=400)
# L(f(x),y) = -y*log(f(x)) - (1-y)log(1-f(x))

def compute(w , x , b , a,dj_dw,dj_db):

    z = np.dot(w,x) +b
    f_x = 1 /(1+np.exp(-z))

    #log loss
    loss = -y*np.log(f_x) - (1-y) *np.log(1-f_x)


    w = w - a*dj_dw
    b = b - a*dj_db