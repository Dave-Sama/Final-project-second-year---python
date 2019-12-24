# -*- coding: utf-8 -*-
"""
@author: Jean-Gabriel JOLLY
"""

# ===============
# Importing modules
# ===============

# modules for GUI
# from tkinter import *
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning

# modules for image processing
import PIL
from PIL import Image

# module for Manage files and use system commands
import os
import glob

# ===============
# variables declaration
# ===============


# List of rectangles displays on screen
global rectangleList
rectangleList = [[], [], [], [], [], [], [], [], [], []]

# Counters for managing rectangles and pictures
global numberImage, numberRectangle, totalRectangle, numberPicture
numberImage, numberRectangle, totalRectangle, numberPicture = 0, 0, 0, 0

global numberTotalImagePerLabel
numberTotalImagePerLabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

global numberImagePerLabel
numberImagePerLabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Square position
global x1, x2, y1, y2
x1, x2, y1, y2 = 0, 0, 0, 0

# for select the folder
global selectFolder
selectFolder = 0

global listFolder
listFolder = ["nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope"]

global listLabel
listLabel = ["nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope", "nope"]

global labelDisplay
labelDisplay = "txt"


# ===============
# ===============
# ===============


# Square position


def leftClick(event):
    chaine.configure(text=str(event.x) + " " + str(event.y))
    global x1, y1
    x1 = event.x
    y1 = event.y


def holdLeftClick(event):
    chaine.configure(text=str(event.x) + " " + str(event.y) + "Frame object number " + str(numberRectangle))
    cadre.coords(rectangle, x1, y1, event.x, event.y)
    # cadre.coords(oval,x1+90,y1+90, event.x-90, event.y-90)


def releaseLeftClick(event):
    cadre.coords(rectangle, 0, 0, 0, 0)
    cadre.coords(oval, 0, 0, 0, 0)
    global x2, y2, numberRectangle, rectangleList, totalRectangle, hpercent, numberImagePerLabel, numberTotalImagePerLabel
    chaine.configure(text="Number of frames:" + str(numberRectangle + 1) + " Selected folder: " + listLabel[int(selectFolder)])
    x2 = event.x
    y2 = event.y
    rectangleList[int(selectFolder)].append(cadre.create_rectangle(x1, y1, x2, y2))
    numberRectangle += 1
    numberImagePerLabel[int(selectFolder)] = numberImagePerLabel[int(selectFolder)] + 1
    totalRectangle += 1
    numberTotalImagePerLabel[int(selectFolder)] = numberTotalImagePerLabel[int(selectFolder)] + 1

    ####Selection orientation management PART#####
    if x1 < x2 and y1 < y2:
        area = (int(x1 / hpercent), int(y1 / hpercent), int(x2 / hpercent), int(y2 / hpercent))
    elif x2 < x1 and y2 < y1:
        area = (int(x2 / hpercent), int(y2 / hpercent), int(x1 / hpercent), int(y1 / hpercent))
    elif x2 < x1 and y1 < y2:
        area = (int(x2 / hpercent), int(y1 / hpercent), int(x1 / hpercent), int(y2 / hpercent))
    elif x1 < x2 and y2 < y1:
        area = (int(x1 / hpercent), int(y2 / hpercent), int(x2 / hpercent), int(y1 / hpercent))

    ####CROPPING PART#####
    cropped_img = img.crop(area)
    cropped_img.save(listFolder[int(selectFolder)] + "/" + listLabel[int(selectFolder)] + str(numberTotalImagePerLabel[int(selectFolder)]) + '.png')  # test bug here
    ######################


def middleClick(event):
    global numberPicture, photo, photo2, img, rectangle, numberRectangle, numberImagePerLabel
    numberPicture += 1
    if numberPicture < len(listPictures):

        imageDisplay()

        cadre.delete(aff)
        cadre.create_image(0, 0, anchor=NW, image=photo2)
        rectangle = cadre.create_rectangle(0, 0, 0, 0)
        numberRectangle = 0
        numberImagePerLabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Removing old rectangles
        for j in range(0, 8, 1):
            for i in rectangleList[j]:
                cadre.delete(i)
        ########################

    else:
        chaine.configure(text="No More pictures")
        showwarning('Warning', 'No More pictures')


##########################
##########################
##########################
def rightClick(event):
    global rectangleList, numberRectangle, totalRectangle
    if numberImagePerLabel[int(selectFolder)] > 0:
        chaine.configure(text="Erasing frame number =" + str(numberRectangle))
        cadre.delete(rectangleList[int(selectFolder)][len(rectangleList[int(selectFolder)]) - 1])
        del rectangleList[int(selectFolder)][len(rectangleList[int(selectFolder)]) - 1]
        os.remove(listFolder[int(selectFolder)] + "/" + listLabel[int(selectFolder)] + str(numberTotalImagePerLabel[int(selectFolder)]) + '.png')
        numberRectangle -= 1
        totalRectangle -= 1
        numberImagePerLabel[int(selectFolder)] = numberImagePerLabel[int(selectFolder)] - 1
        numberTotalImagePerLabel[int(selectFolder)] = numberTotalImagePerLabel[int(selectFolder)] - 1


    else:
        chaine.configure(text="Nothing to erase")


def imageDisplay():
    global numberPicture, photo, photo2, img, rectangle, hpercent

    # photo = PhotoImage(file=listPictures[numberPicture])
    im = Image.open(listPictures[numberPicture])  # test test test
    photo = PhotoImage(im)

    ###DISPLAY RESIZE MODULE###
    baseheight = (int(fen.winfo_screenheight() * 0.85))  # size of the height of the screen
    ############ A MOFIFIER PLUS TARD  ^^^^^^^^
    img = Image.open(listPictures[numberPicture])
    hpercent = ((baseheight / float(img.size[1])))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img2 = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    ###########################

    ############ A MOFIFIER PLUS TARD
    img2.save("temporaryFile.png")
    # photo2 = PhotoImage(file="image32bis.png")
    photo2 = PhotoImage(file="temporaryFile.png")
    ############ A MOFIFIER PLUS TARD


def folderSelectKey(event):
    global selectFolder, listFolder, listLabel, labelDisplay

    key = event.keysym
    selectFolder = int(key)

    if key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0":
        selectFolder = event.keysym
        if listFolder[int(key)] == "nope":
            toDo = "Select the destination folder of label number " + str(selectFolder)
            listFolder[int(key)] = askdirectory(title=toDo, initialdir='C:/Users/%s')
            listLabel[int(key)] = os.path.basename(listFolder[int(key)])
            labelDisplay = labelDisplay + " Key" + key + "= " + listLabel[int(key)] + " ;"
            chaineLabels.configure(text=labelDisplay)

    chaine.configure(text="Number of frames:" + str(numberRectangle + 1) + " Selected folder: " + listLabel[int(selectFolder)])


##########################
##########################
##########################
##########################
##########################
##########################


fen = Tk()
fen.title('Very Fast Multiple Cropping Tool')

# Ask for directory
showwarning('Instructions', 'Enter the image folder')
inputDirectory = askdirectory(initialdir='C:/Users/%s')
showwarning('Instructions', 'Enter the destination folder')
outputDirectory = askdirectory(initialdir='C:/Users/%s')

# Set Directory list and display
listFolder[0] = outputDirectory
listLabel[0] = os.path.basename(listFolder[0])
labelDisplay = "Key0= " + listLabel[0] + " ;"

# =================

# list images in the forlder
listPictures = sorted(glob.glob(inputDirectory + '/*.png'))
listPictures2 = sorted(glob.glob(inputDirectory + '/*.jpg'))
listPictures3 = sorted(glob.glob(inputDirectory + '/*.tif'))

listPictures = listPictures + listPictures2 + listPictures3

###
if len(listPictures) > 0:
    imageDisplay()
    cadre = Canvas(fen, width=photo2.width(), height=photo2.height(), bg="light yellow")

    w, h = photo2.width(), photo2.height() + 40
    fen.geometry("%dx%d+0+0" % (w, h))

    aff = cadre.create_image(0, 0, anchor=NW, image=photo2)  # BUG
    cadre.bind("<Button-1>", leftClick)
    cadre.bind("<B1-Motion>", holdLeftClick)
    cadre.bind("<ButtonRelease-1>", releaseLeftClick)
    cadre.bind("<Button-2>", middleClick)
    cadre.bind("<ButtonRelease-3> ", rightClick)
    cadre.focus_set()
    cadre.bind("<Key>", folderSelectKey)
    cadre.pack()
    chaineLabels = Label(fen)
    chaine = Label(fen)
    chaineLabels.configure(text=labelDisplay)
    chaineLabels.pack()
    chaine.pack()
    rectangle = cadre.create_rectangle(0, 0, 0, 0)
    oval = cadre.create_oval(0, 0, 0, 0)
    fen.mainloop()
    os.remove("temporaryFile.png")
else:
    showwarning('Error', 'There are no images in the folder')
    fen.destroy()