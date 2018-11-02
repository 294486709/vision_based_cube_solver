import cv2
from PIL import Image
from PIL import ImageEnhance
import numpy as np


def pict3(path,de):
    img = cv2.imread(path)
    cutted = img[70:125, 225:280]
    cutted = cv2.resize(cutted, (60, 60), interpolation=cv2.INTER_CUBIC)
    #cutted = cv2.cvtColor(cutted, cv2.COLOR_BGR2HSV)
    #cv2.imshow('1',cutted)
    #cv2.waitKey(0)
    if de == 0:
        pass
    elif de ==1:
        cutted = np.rot90(cutted)
    elif de == 2:
        cutted = np.rot90(cutted,2)
    elif de ==3:
        cutted = np.rot90(cutted,3)
    path = 'p'+path
    cv2.imwrite(path,cutted)
    image = Image.open(path)
    imageb = ImageEnhance.Brightness(image)
    brightness = 3
    brighted = imageb.enhance(brightness)
    brighted.save(path)


def pict2(path,de):
    img = cv2.imread(path)
    cutted = img[75:132, 200:257]
    cutted = cv2.resize(cutted, (60, 60), interpolation=cv2.INTER_CUBIC)
    #cutted = cv2.cvtColor(cutted, cv2.COLOR_BGR2HSV)
    #cv2.imshow('1',cutted)
    #cv2.waitKey(0)
    if de == 0:
        pass
    elif de ==1:
        cutted = np.rot90(cutted)
    elif de == 2:
        cutted = np.rot90(cutted,2)
    elif de ==3:
        cutted = np.rot90(cutted,3)
    path = 'p'+path
    cv2.imwrite(path,cutted)
    image = Image.open(path)
    imageb = ImageEnhance.Brightness(image)
    brightness = 3
    brighted = imageb.enhance(brightness)
    brighted.save(path)


def pict1(path,de):
    img = cv2.imread(path)
    cutted = img[48:105, 173:230]
    cutted = cv2.resize(cutted, (60, 60), interpolation=cv2.INTER_CUBIC)
    path = 'p'+path
    if de == 0:
        pass
    elif de ==1:
        cutted = np.rot90(cutted)
    elif de == 2:
        cutted = np.rot90(cutted,2)
    elif de ==3:
        cutted = np.rot90(cutted,3)
    cv2.imwrite(path,cutted)
    image = Image.open(path)
    imageb = ImageEnhance.Brightness(image)
    brightness = 3
    brighted = imageb.enhance(brightness)
    brighted.save(path)


if __name__ =='__main__':
    path1 = 'side1.jpg'
    path2 = 'side2.jpg'
    path3 = 'side3.jpg'
    path4 = 'side4.jpg'
    path5 = 'side5.jpg'
    path6 = 'side6.jpg'
    pict1(path1,1)
    pict1(path4,0)
    pict2(path2,1)
    pict2(path5,2)
    pict3(path3,3)
    pict3(path6,0)

