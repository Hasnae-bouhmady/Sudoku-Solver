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
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50)
    for i in range(9):
        for j in range(9):
            if puzzle[j][i] != 0 :
                draw.text((i*100+35,j*100+25),str(puzzle[j][i]), fill =(0,0,0,255),font = font,align="center")
            else:
                draw.text((i * 100 + 35, j * 100 + 25), str(solution[j][i]), fill=(122, 0, 0, 255), font=font,align="center")
    im.show()

def draw1(puzzle):
    im = Image.new('RGBA', (900, 900), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(4):
        draw.line((i*300,0,i*300,900), (0,0,0,255),5)
        draw.line((0,i*300,900,i*300), (0,0,0,255),5)
        for j in range(2):
            draw.line((i * 300+(j+1)*100, 0, i * 300 + (j+1)*100, 900), (0, 0, 0, 255), 2)
            draw.line((0,i * 300 + (j + 1) * 100,900, i * 300 + (j + 1) * 100), (0, 0, 0, 255),2)
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50)
    for i in range(9):
        for j in range(9):
            if puzzle[j][i] != 0 :
                draw.text((i*100+35,j*100+25),str(puzzle[j][i]), fill =(0,0,0,255),font = font,align="center")
    im.show()

