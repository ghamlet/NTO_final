import cv2

cap = cv2.VideoCapture("video_2024-02-23_00-47-07.mp4")
while True:
    res, image = cap.read()

    bin = 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(blurred, 10, 100)

    cv2.imshow("Original image", image)
    cv2.imshow("Edged image", edged)
    cv2.waitKey(10)


    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_copy = image.copy()
    # draw the contours on a copy of the original image
    cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
    print(len(contours), "objects were found in this image.")

    cv2.imshow("Edged image", edged)
    cv2.imshow("contours", image_copy)
    cv2.waitKey(10)