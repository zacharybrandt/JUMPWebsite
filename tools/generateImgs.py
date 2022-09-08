from distutils.command.sdist import sdist
from glob import glob
from bs4 import BeautifulSoup
import cv2
import random


def get(year):
    imgDir = glob("../assets/images/dump/"+year+"/*")

    html = BeautifulSoup("<!--Autogenerated HTML-->", 'html.parser')
    portraits = []
    landscapes = []
    images = []
    for j in imgDir:
        img = html.new_tag('img')
        im = cv2.imread(j)
        h,w,_ = im.shape
        portrait = True if h  > w else False
        img['class'] = 'p' if portrait else 'l'
        img['src'] = j
        img['alt'] = "Picture from JUMP's " + year + " season"
            
        if portrait:
            portraits.append(img)
        else:
            landscapes.append(img)
        
    pIn = len(portraits)//2+1
    lIn = len(landscapes)//2

    first = portraits[0:pIn] + (landscapes[0:lIn])
    second = portraits[pIn:] + (landscapes[lIn:])
    for i in [first, second]:
        random.shuffle(i)
        col = html.new_tag("div")
        col['class'] = 'col'
        for j in i:
            col.append(j)
        html.append(col)
    
    with open('../templates/' + year+ 'media.html', 'w') as f:
        f.write(str(html.prettify()))

for i in ["2020", "2021", "2022"]:
    get(i)
