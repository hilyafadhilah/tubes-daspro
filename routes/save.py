import os
from modules.save_mod import FindFolder, MakeFolder, RemakeFile
from modules.store import _data

def Save():
    save_folder = input("Masukkan nama folder penyimpanan : ")
    Path = os.getcwd()
    print("\nSaving...")
    if (FindFolder(save_folder, Path) == False):
        MakeFolder(save_folder, Path)

    RemakeFile(_data, save_folder, Path)