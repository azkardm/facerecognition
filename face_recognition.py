from deepface import DeepFace

# Fungsi untuk mengenali wajah
def detectFace(image_path, database):
    # Proses pencocokan wajah
    recognition = DeepFace.find(
        image_path, database, enforce_detection=False
    )

    # Mengambil data yang paling cocok
    recognition_df = recognition[0]

    # Kondisi jika tidak ada wajah yang cocok
    if len(recognition_df) == 0:
        return "Wajah tidak terdaftar"
    
    # Kondisi jika ada wajah yang cocok
    else:
        identity = recognition_df.loc[0, 'identity']
        # Proses splitting (asumsi nama file = "folder_name\\name.jpg")
        folder_split = identity.split("\\")
        name_split = folder_split[-1].split('.')
        name = name_split[0]
        return f"Wajah terdeteksi sebagai {name}"

# Fungsi utama
def main():
    database = "faces data"     # Nama folder database
    temp_image = "temp.jpg"     # Nama file image yang ingin dikenali
    result = detectFace(temp_image, database)
    print(result)

# Jalankan program
if __name__ == "__main__":
    main()
