import cv2
import time

# Start webcam
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate index if multiple webcams are connected

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Wait for 5 seconds before capturing
start_time = time.time()
while time.time() - start_time < 5:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the captured frame
    cv2.imshow('Webcam Capture', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
