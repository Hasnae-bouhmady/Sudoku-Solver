from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os, io, sys
import numpy as np
import base64
import cv2
from Extract_Puzzle import extract_puzzle
from Puzzle import *
from Draw import *
from tensorflow.keras.models import load_model
from io import BytesIO

app = Flask(__name__, static_url_path='')
CORS(app)
globvar = False
model = load_model('Models/digit_classifier.h5') #soit  load_model(Models/image_to_number_model.hdf5')
def getModel():
    global model
    return model


def set_globvar_to_False():
    global globvar    # Needed to modify global copy of globvar
    globvar = False

def set_globvar_to_True():
    global globvar    # Needed to modify global copy of globvar
    globvar = True

def get_globvar():
    return globvar     # No need for global declaration to read value of globvar

def serve_pil_image(pil_img):
    img_io= BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/solution', methods=['GET'])
def solution():
    while(True):
        if get_globvar():
            puzzle = np.loadtxt("Temp/array", delimiter=',', dtype='int32')
            puzzleglb = Puzzle(puzzle,puzzle)

            set_globvar_to_False()
            if (np.array_equal(puzzle, np.zeros((9, 9), dtype='int'))):
                return serve_pil_image(drawtxt("Puzzle sudoku non identifié!"))
            else:
                i = puzzleglb.resoudre()
                if (i == 1):
                    img = draw(puzzle,puzzleglb.resolu)
                    return serve_pil_image(img)
                else:
                    return serve_pil_image(drawtxt("Pas de solution pour votre puzzle!"))



@app.route('/getPuzzle', methods=['POST'])
def getPuzzle():
    file = request.files['image'].read()  ## byte file
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    ######### Do preprocessing here ################
    # img[img > 150] = 0
    ## any random stuff do here
    ################################################
    img = Image.fromarray(img.astype("uint8"))
    rawBytes = io.BytesIO()
    img.save(rawBytes, "JPEG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())
    puzzle = extract_puzzle(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR), getModel())
    np.savetxt("Temp/array",puzzle, delimiter=',')
    set_globvar_to_True()
    return jsonify({'status':"REPONSE"})


if __name__ == "__main__":
    app.run(debug=True)