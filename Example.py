#from mcx import mcx
import cv2
import numpy as np



    #img_np = np.frombuffer(image, dtype=np.uint8)
    #img = cv2.imdecode(img_np, -1) #convert bytes to image OPENCV KluchBel
img=cv2.imread('/home/user/Pictures/89')

red = cv2.inRange(img, (121,123,191),(255,255,255))
red_sum = np.sum(red)

orange = cv2.inRange(img, (165,25,153),(255,255,255))
orange_sum=np.sum(orange)

green = cv2.inRange(img, (60, 60, 0),(102, 255, 255))
green_sum =np.sum(green)

grey = cv2.inRange(img, (0, 0, 31),(193, 125,83 ))
grey_sum = np.sum(grey)

print(red_sum)
print(orange_sum)
print(green_sum)
print(grey_sum)


if red_sum > orange_sum and red_sum > green_sum and red_sum > grey_sum:
    print('Oгнетушитель')
if green_sum > orange_sum and green_sum > grey_sum and green_sum > red_sum:
    print('Aптечка')
if orange_sum > green_sum and orange_sum > grey_sum and orange_sum > red_sum:
    print('Ремонт')
if grey_sum > orange_sum and grey_sum > green_sum and grey_sum > red_sum:
    print('Машина')


#else  
    #mask = cv2.inRange(img, lower_red, upper_red)
    #filtered_image = cv2.bitwise_and(img, img, mask=mask) #filtered image by red 