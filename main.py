import os

def main():
    image_path = "THE GLOBAL CHRONICLE.jpg"
    if os.path.exists(image_path):
        print(f"Gambar berita {image_path} berhasil diverifikasi.")
    else:
        print("Gambar tidak ditemukan.")

if __name__ == "__main__":
    main()
