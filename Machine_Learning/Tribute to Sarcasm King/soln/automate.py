from pwn import *
import cv2
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://aetherius-ml.iitmandi.co.in/")

sift = cv2.xfeatures2d.SIFT_create()
template = cv2.imread('chandler.jpg')       #cropped image to create chandler.jpg
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
keypoints_1, descriptors_1 = sift.detectAndCompute(template,None)

def detect(img):
    im_h,im_w=img.shape[:2]                                                 #splits image into quadrants
    (cX, cY) = (im_w // 2, im_h // 2)
    topLeft = img[0:cY, 0:cX]
    topRight = img[0:cY, cX:im_w]
    bottomLeft = img[cY:im_h, 0:cX]
    bottomRight = img[cY:im_h, cX:im_w]

    arr=[]
    res = dict(map(lambda i,j : (j,i) , \
                (topRight,topLeft,bottomLeft,bottomRight),\
                ('topRight','topLeft','bottomLeft','bottomRight')))
    j=0
    for i in res:
        res[i] = cv2.cvtColor(res[i], cv2.COLOR_BGR2GRAY)
        keypoints_2, descriptors_2 = sift.detectAndCompute(res[i],None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descriptors_1,descriptors_2, k=2)

        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.1*n.distance:
                good.append([m])

        # cv2.drawMatchesKnn expects a list of lists as matches.
        img3 = cv2.drawMatchesKnn(template, keypoints_1, res[i], keypoints_2,good,None,flags=0)
        j+=1
        if len(good)>0:
            arr.append(j)
        else:pass
        cv2.imwrite(i+'.jpg',img3)
    print(arr)
    return arr

while True:
    if 'aetherius' in driver.page_source:   #checks for flag
        print(driver.page_source)
        break
    img=driver.find_element(By.TAG_NAME,'img').get_attribute('src')
    print(img)
    data = requests.get(img).content                                        #downloads image
    with open ('output.jpg', 'wb') as f:
        f.write(data)
    img=cv2.imread('output.jpg')
    arr=detect(img)                                                         #detects quadrants
    inp,submit=driver.find_elements(By.TAG_NAME,'input')
    inp.send_keys(str(arr))
    submit.submit()
