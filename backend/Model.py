from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

class Model:
    @staticmethod
    def build(largeur, hauteur, profondeur, classes):
        # initialiser le modèle
            model = Sequential()
            inputshape = (largeur, hauteur, profondeur)
        # 1ère couche de convolution (Conv), Redressement (ReLU) et Pooling (mise en commun)
            model.add(Conv2D(32, (5, 5), padding="same",input_shape=inputshape))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2, 2)))
        # 2ème couche de convolution (Conv), Redressement (ReLU) et Pooling (mise en commun)
            model.add(Conv2D(32, (3, 3), padding="same"))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2, 2)))
        # 1ère couche des neurons entièrement connecté (FC) et redressement (RELU)
            model.add(Flatten())
            model.add(Dense(64))
            model.add(Activation("relu"))
            model.add(Dropout(0.5))
        # 2ème couche des neurons entièrement connecté (FC) et redressement (RELU)
            model.add(Dense(64))
            model.add(Activation("relu"))
            model.add(Dropout(0.5))
        # softmax classifier
            model.add(Dense(classes))
            model.add(Activation("softmax"))
        # retourner l'architecture de neurones construite
            return model