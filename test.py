import cv2


config_path = "traffic/cfg/yolov4-tiny-obj.cfg"  
weights_path = "traffic/backup/yolov4-tiny-obj_final.weights"
classes = ["people"]

def find_people(frame):
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)


yolo_model = cv2.dnn.DetectionModel(net)
yolo_model.setInputParams(size= (416,416), scale= 1/255, swapRB=True)

# video = cv2.VideoCapture("traffic/video_2024-02-23_02-28-20.mp4")
video= cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break



    class_ids, scores, boxes = yolo_model.detect(frame, 0.2, 0.2)

    if len(class_ids):
        print("fghj")


    for id in class_ids:
        print(classes[id])

    for box in boxes:
        (x,y,w,h) = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)
    cv2.waitKey(1) 