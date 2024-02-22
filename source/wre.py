import cv2

# Загрузка изображения
img = cv2.imread('VSEbel')

# Преобразование изображения в цветовое пространство HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Присвоение синего цвета путем изменения значения канала Hue (оттенок)
hsv_img[:, :, 0] = 120  # Значение для синего цвета в HSV

# Преобразование обратно в цветовое пространство BGR
blue_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

# Отображение исходного и измененного изображений
cv2.imshow('Original Image', img)
cv2.imshow('Blue Image', blue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
