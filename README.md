# Face Recognition System
This project uses OpenCV and DeepFace for real-time face detection and recognition from a live camera feed.

## Requirements
- Python 3.x
- OpenCV
- DeepFace
- Haarcascade XML file (included in OpenCV)

## Features
- Real-Time Face Detection: Uses OpenCV's Haarcascade to detect faces in real-time.
- Face Recognition: Uses DeepFace to recognize detected faces by comparing them with a database.
- Temporary File Handling: Extracted faces are temporarily saved as temp.jpg for recognition and deleted after use.

## Program Flow
1. Camera setup
   - The program currently uses the default camera index (0) but can be configured to use a different index if necessary. Update the line cv.VideoCapture(0) to another number if the default camera isn't the correct one.
2. Face detection
3. Processing detected face
   - Draw a rectangle around the face
   - Crop the face from the frame and save it as temporary file
4. Face recognition
   - The program compares the temporary cropped face (temp.jpg) with known faces stored in the folder_name directory. The matching process uses DeepFace to find the closest match based on a similarity threshold        (defaulted to 0.5).
   - If a match is found:
     - The identity of the person is displayed in the console.
     - The face is added to a list of recognized faces to prevent repeated recognition.
   - If no match is found, it will indicate that no matching face was detected.
5. The program processes the faces every 1 second, ensuring efficient performance while keeping the recognition process timely.
6. The program will stop once the 'd' key is pressed
7. Final output
   - When the program terminates, it will display a list of recognized faces in the console. If no faces were detected, it will print a message stating that no faces were found during the session.

## Potential Improvements
1. Handling multiple faces in 1 frame
   - When many faces are detected in one frame, the program takes longer because each face is processed sequentially, and face matching takes considerable time, especially if a large number of faces are detected.
2. Threshold
   - The program currently uses a fixed threshold (threshold=0.6) in DeepFace for face matching. However, this value may not be suitable for all cases.
3. Better face database management
   - If the faces data folder contains a large number of face images, the matching process can become very slow. This is especially problematic when the number of images that need to be matched continues to grow.
4. Face processing interval
   - The program currently processes faces every 1 second. This interval can be adjusted depending on the use case or system performance.
     
