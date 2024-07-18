from ultralytics import YOLO
import cv2
model=YOLO('yolov8n.pt')
video='video (1).mp4'
cap=cv2.VideoCapture(video)
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter('tracking.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while cap.isOpened():
    succuess,frame=cap.read()
    if succuess:
        results=model.track(frame,persist=True)
        annotaed_frame=results[0].plot()
        out.write(annotaed_frame)
    else:
        break
cap.release()
cap.release()