import cv2 as cv
import os
import time
from deepface import DeepFace

# Inisialisasi classifier wajah menggunakan Haarcascade dari OpenCV
def initialize_face_cascade():
    return cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fungsi untuk menangkap frame dari kamera
def capture_frame(cam):
    ret, frame = cam.read()
    if not ret:
        return None  # Jika frame tidak berhasil ditangkap, kembalikan None
    return frame  # Kembalikan frame jika berhasil

# Fungsi untuk mendeteksi wajah dalam frame
def detect_faces(face_cascade, frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Konversi frame ke grayscale
    return face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )  # Deteksi wajah dalam frame

# Fungsi untuk memproses wajah yang terdeteksi
def process_faces(faces, frame, folder_name, detected_face):
    for (x, y, w, h) in faces:
        # Gambar kotak di sekitar wajah yang terdeteksi
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Ekstrak wajah dan simpan sementara sebagai file
        face_roi = frame[y:y+h, x:x+w]
        temp_img_path = 'temp.jpg'
        cv.imwrite(temp_img_path, face_roi)
        
        # Gunakan DeepFace untuk pencocokan wajah
        recognition = DeepFace.find(
            img_path=temp_img_path, db_path=folder_name, enforce_detection=False, threshold= 0.6
        )
        
        # Hapus file sementara setelah digunakan
        os.remove(temp_img_path)
        
        # Ambil hasil pencocokan
        recognition_df = recognition[0]
        if len(recognition_df) > 0:
            # Ambil identitas dari hasil pencocokan
            identity = recognition_df.loc[0, 'identity']
            # Proses splitting untuk mengambil nama dari file foto
            path_parts = identity.split("\\")
            file_parts = path_parts[-1].split('.')
            extracted_name = file_parts[0]
            if extracted_name not in detected_face:
                print(f"Wajah cocok ditemukan: {extracted_name}")
                detected_face.append(extracted_name)  # Tambahkan identitas ke daftar
            else:
                print(f"Wajah sudah dikenali sebagai: {extracted_name}")
        else:
            print("Tidak ada hasil pencocokan.")

# Fungsi utama
def main():
    folder_name = 'faces data'  # Path folder data wajah
    face_cascade = initialize_face_cascade()  # Inisialisasi deteksi wajah
    cam = cv.VideoCapture(0)  # Buka kamera
    last_checked_time = time.time()  # Waktu terakhir pencocokan wajah
    detected_face = []  # Daftar wajah yang telah dikenali

    while True:
        frame = capture_frame(cam)  # Tangkap frame dari kamera
        if frame is None:
            print('Frame tidak berhasil ditangkap')
            break
        
        faces = detect_faces(face_cascade, frame)  # Deteksi wajah dalam frame
        current_time = time.time()

        # Proses wajah setiap 1 detik
        if current_time - last_checked_time >= 1:
            process_faces(faces, frame, folder_name, detected_face)
            last_checked_time = current_time  # Perbarui waktu terakhir pencocokan

        # Tampilkan frame dengan kotak wajah
        cv.imshow('Face Detection', frame)
        
        # Keluar jika tombol 'd' ditekan
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    cam.release()  # Lepaskan kamera
    cv.destroyAllWindows()  # Tutup semua jendela
    # Tampilkan daftar wajah yang dikenali
    if len(detected_face) > 0:
        print(f'list nama yang sudah terdeteksi: {detected_face}')
    else:
        print('Tidak ada wajah yang terdeteksi')  

# Jalankan program
if __name__ == "__main__":
    main()
