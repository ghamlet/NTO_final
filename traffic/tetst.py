import cv2


config_path = "Traffic-Sign-Dataset-YOLOv4-Tiny/cfg/yolov4-tiny-custom-traffic.cfg"  
weights_path = "Traffic-Sign-Dataset-YOLOv4-Tiny/backup/yolov4-tiny-custom-traffic_last.weights"

with open("Traffic-Sign-Dataset-YOLOv4-Tiny/data/obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]


net = cv2.dnn.readNetFromDarknet(config_path, weights_path)


yolo_model = cv2.dnn.DetectionModel(net)
yolo_model.setInputParams(size= (608,608), scale= 1/255, swapRB=True)

video = cv2.VideoCapture(0)


while True:
    ret, frame = video.read()
    if not ret:
        break



    class_ids, scores, boxes = yolo_model.detect(frame, 0.2, 0.2)
    for id in class_ids:
        print(classes[id])

    for box in boxes:
        (x,y,w,h) = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)
    cv2.waitKey(1) 