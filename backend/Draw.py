import os.path
from io import BytesIO

import requests
from PIL import Image, ImageDraw
from PIL import ImageFont


def draw(puzzle,solution):
    im = Image.new('RGBA', (900, 900), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(4):
        draw.line((i*300,0,i*300,900), (0,0,0,255),5)
        draw.line((0,i*300,900,i*300), (0,0,0,255),5)
        for j in range(2):
            draw.line((i * 300+(j+1)*100, 0, i * 300 + (j+1)*100, 900), (0, 0, 0, 255), 2)
            draw.line((0,i * 300 + (j + 1) * 100,900, i * 300 + (j + 1) * 100), (0, 0, 0, 255),2)
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50) #si erreur remplacer par  ImageFont.truetype("arial", 50)
    for i in range(9):
        for j in range(9):
            if puzzle[j][i] != 0 :
                draw.text((i*100+35,j*100+25),str(puzzle[j][i]), fill =(0,0,0,255),font = font,align="center")
            else:
                draw.text((i * 100 + 35, j * 100 + 25), str(solution[j][i]), fill=(0, 255, 0, 255), font=font,align="center")
    im.save("Temp/sol.png")
    return im

def draw1(puzzle):
    im = Image.new('RGBA', (900, 900), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(4):
        draw.line((i*300,0,i*300,900), (0,0,0,255),5)
        draw.line((0,i*300,900,i*300), (0,0,0,255),5)
        for j in range(2):
            draw.line((i * 300+(j+1)*100, 0, i * 300 + (j+1)*100, 900), (0, 0, 0, 255), 2)
            draw.line((0,i * 300 + (j + 1) * 100,900, i * 300 + (j + 1) * 100), (0, 0, 0, 255),2)
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50) #si erreur remplacer par  ImageFont.truetype("arial", 50)
    for i in range(9):
        for j in range(9):
            if puzzle[j][i] != 0 :
                draw.text((i*100+35,j*100+25),str(puzzle[j][i]), fill =(0,0,0,255),font = font,align="center")
    im.show()

def drawtxt(texte):
    a= len(texte)
    im = Image.new('RGBA', (a*30, 100), (255, 255, 255, 0))
    #font = ImageFont.truetype("C:/Users/MOHAMMED AMINE/PycharmProjects/sudokusolver/backend/Audiowide/Audiowide-Regular.ttf", 50)
    font = ImageFont.truetype(os.path.abspath("Audiowide/Audiowide-Regular.ttf"), 50) #si erreur remplacer par  font = ImageFont.truetype(os.path.abspath("Audiowide/Audiowide-Regular.ttf"), 50)
    draw = ImageDraw.Draw(im)
    draw.text((5,5), texte, fill=(0,0,0), font=font, align="center")
    draw.text((7,7),texte, fill =(255,255,255,255),font = font,align="center")
    return im



