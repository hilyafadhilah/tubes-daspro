import os
from modules.save_mod import FindFolder, MakeFolder, RemakeFile
from modules.store import TakeData

def SaveRoute():
    save_folder = input("Masukkan nama folder penyimpanan : ")
    Path = os.getcwd()
    print("\nSaving...")
    if not FindFolder(save_folder, Path):
        MakeFolder(save_folder, Path)

    RemakeFile(TakeData(), save_folder, Path)
    print("Penyimpanan berhasil dilakukan")
