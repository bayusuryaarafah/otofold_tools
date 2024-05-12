import os

def create_folders(path, folder_name, num_folders):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        
        for i in range(1, num_folders + 1):
            folder_path = os.path.join(path, f"{folder_name}_{i}")
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}_{i}' berhasil dibuat di '{path}'.")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    path = input("Masukkan path tempat folder akan dibuat: ")
    folder_name = input("Masukkan nama folder: ")
    num_folders = int(input("Masukkan jumlah folder yang akan dibuat: "))

    create_folders(path, folder_name, num_folders)