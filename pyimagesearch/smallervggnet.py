# import the necessary packages
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

class SmallerVGGNet:
	@staticmethod
	def build(width, height, depth, classes):
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

        # # CONV => RELU => POOL
		# model.add(Conv2D(32, (3, 3), padding="same",
		# 	input_shape=inputShape))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization(axis=chanDim))
		# model.add(MaxPooling2D(pool_size=(3, 3)))
		# model.add(Dropout(0.25))

        # # We’re increasing our filter size from 32  to 64 . The deeper we go in the network, the smaller the spatial dimensions of our volume, and the more filters we learn.
        # # We decreased how max pooling size from 3 x 3  to 2 x 2  to ensure we do not reduce our spatial dimensions too quickly.

        # # (CONV => RELU) * 2 => POOL
		# model.add(Conv2D(64, (3, 3), padding="same"))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization(axis=chanDim))
		# model.add(Conv2D(64, (3, 3), padding="same"))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization(axis=chanDim))
		# model.add(MaxPooling2D(pool_size=(2, 2)))
		# model.add(Dropout(0.25))

        # # (CONV => RELU) * 2 => POOL
		# model.add(Conv2D(128, (3, 3), padding="same"))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization(axis=chanDim))
		# model.add(Conv2D(128, (3, 3), padding="same"))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization(axis=chanDim))
		# model.add(MaxPooling2D(pool_size=(2, 2)))
		# model.add(Dropout(0.25))

        # # first (and only) set of FC => RELU layers
		# model.add(Flatten())
		# model.add(Dense(1024))
		# model.add(Activation("relu"))
		# model.add(BatchNormalization())
		# model.add(Dropout(0.5))

		# # softmax classifier
		# model.add(Dense(classes))
		# model.add(Activation("softmax"))

        # Versión simplificada pero en principio peores resultados pero entrenamiento más rápido, quizás al poder
		# tener más épocas en el mismo tiempo que el modelo de arriba pueda ser mejor ¿?
		model.add(Flatten(input_shape=(96, 96, 3), name="Input_layer"))
		model.add(Dense(100, activation='relu', name="Hidden_layer_1"))
		model.add(Dense(50, activation='relu', name="Hidden_layer_2"))
		model.add(Dense(5, activation='softmax', name="Output_layer"))

		# return the constructed network architecture
		return model
