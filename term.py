import cv2
import time
import os  # Add this import for handling file paths

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

# Release the webcam before using it again
cap.release()

# Convert the captured frame to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale frames side by side
cv2.imshow('Original Frame', frame)
cv2.imshow('Grayscale Frame', gray_frame)

# Wait for a key press and then close the image windows
cv2.waitKey(0)

# Close OpenCV windows
cv2.destroyAllWindows()
