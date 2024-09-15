import cv2
import numpy as np
import time

# Open video capture
cam = cv2.VideoCapture(0)
path = "haarcascade_frontalface_default.xml"
# Load the face detector
face_detector = cv2.CascadeClassifier(path)

frame = True
while frame:
    # Capture frame-by-frame
    val, im = cam.read()
    im_new = cv2.resize(im, (512, 512))
    # Convert the color (BGR) into grayscale
    gray_im = cv2.cvtColor(im_new, cv2.COLOR_BGR2GRAY)
    # Run the classifier on the image
    faces = face_detector.detectMultiScale(gray_im, scaleFactor=1.1, minNeighbors=10)
    
    # Draw bounding boxes around the detected faces
    for (dx, dy, w, h) in faces:
        cv2.rectangle(im_new, (dx, dy), (dx+w, dy+h), (255,0,0), 2)

    # Display the total number of users at the top left corner
    total_users = len(faces)
    cv2.putText(im_new, f"Total Faces: {total_users}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    # Display the resulting frame
    cv2.imshow('camera live feed', im_new)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        frame = False
        break

# Release the capture and close windows
cam.release()
cv2.destroyAllWindows()