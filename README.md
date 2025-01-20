# Face Recognition with DeepFace
This project demonstrates a simple face recognition system using the DeepFace library. The system is designed to identify a face from an input image by comparing it with a set of pre-stored images in a database.

## Requirements
To run this project, you need to install:
- Python 3.x
- DeepFace library
- Pandas library

## Folder Structure
- faces data/: This folder contains the database of images against which the input image will be compared.
- temp.jpg: This is the input image file whose face will be recognized.
- face_recognition.py: The main script containing the face recognition logic.

## Usage
1. Place the images of known individuals in the "faces data/" folder. Each image file should be named using the format "name.jpg".
2. Place the image you want to recognize as "temp.jpg" in the root directory.
3. Run the face_recognition.py script
4. The program will display the name of the person if the face is recognized, or "Wajah tidak terdaftar" if the face is not found in the database.

## Notes
1. Ensure that the images in the "faces data/" folder are clear and properly labeled.
2. The enforce_detection=False parameter in DeepFace.find() allows the function to process images even if a face is not detected by the default face detector.
