import cv2

# Load the pre-trained face detection model (Haar cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default webcam
video_cap = cv2.VideoCapture(0)

while True:
    ret, frame = video_cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Video Live", frame)

    # Break loop when 'a' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('a'):
        break

# Release the capture and destroy windows
video_cap.release()
cv2.destroyAllWindows()



# video_cap = cv2.VideoCapture(0)
# while True :
#     ret,video_data = video_cap.read()
#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
#     video_cap.release()


    
    
    

