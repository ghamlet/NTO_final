import cv2
import numpy as np

image_path = 'VSEbel'
img = cv2.imread(image_path)

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Пороговая обработка для выделения объектов
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Нахождение контуров
# contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Подсчет количества контуров
# num_contours = len(contours)


# num_contours = contours(image_path)
cv2.imshow("frame", img)
cv2.imshow("thresh", thresh)
#print(f"Количество контуров на изображении: {num_contours}")
cv2.waitKey(0)
