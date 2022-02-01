from matplotlib import pyplot as plt
import numpy as np
from Model import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
import argparse

# construire l'analyseur des arguments et analyser les arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="Models/digit_classifier.h5")
args = vars(ap.parse_args())

# initialiser le taux d'entrainement initiale, et le nombre d'epoques pour s'entrainer et la taille du lot (batch size)
INIT_LR = 1e-3
EPOCHS = 10
BS = 128

# Prendre la base de donnée de MNIST
print("[INFO] accès à MNIST...")
((trainData, trainLabels), (testData, testLabels)) = mnist.load_data()

# ajouter une dimension de canal (c'est-à-dire en niveaux de gris) aux chiffres
trainData = trainData.reshape((trainData.shape[0], 28, 28,1 ))
testData = testData.reshape((testData.shape[0], 28, 28, 1))

# mettre les données à l'échelle dans la plage de [0, 1]
trainData = trainData.astype("float32") / 255.0
testData = testData.astype("float32") / 255.0

# convertir les étiquettes d'entiers en vecteurs
le = LabelBinarizer()
trainLabels = le.fit_transform(trainLabels)
testLabels = le.transform(testLabels)

# initialiser l'optimiseur et le modèle
print("[INFO] compilation du modèle ...")
opt = Adam(learning_rate=INIT_LR)
model = Model.build(28, 28, 1, 10)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

# former le réseau
print("[INFO] Formation du réseau ...")
H = model.fit(trainData, trainLabels, validation_data=(testData, testLabels), batch_size=BS, epochs=EPOCHS, verbose=1)

# évaluer le réseau
print("[INFO] évaluation de réseau...")
predictions = model.predict(testData)
print(classification_report(testLabels.argmax(axis=1), predictions.argmax(axis=1),target_names=[str(x) for x in le.classes_]))

# sérialiser le modèle sur le disque
print("[INFO] sérialisation du modèle des chiffres ...")
model.save(args["model"], save_format="h5")
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.title("Pertes et précision de l'entainementy")
plt.xlabel("Epoques")
plt.ylabel("Pertes")
plt.legend(loc="lower left")
plt.show();
