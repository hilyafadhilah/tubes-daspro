# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

import os
from modules.constants import collectionsSchema
from modules.save_mod import FindFolder, MakeFolder, RemakeFile
from modules.store import TakeData

def SaveRoute():
    saveFolder = input("Masukkan nama folder penyimpanan : ")
    path = os.getcwd()
    print("\nSaving...")
    if not FindFolder(saveFolder, path):
        MakeFolder(saveFolder, path)

    RemakeFile(TakeData(), saveFolder, path, collectionsSchema)
    print("Penyimpanan berhasil dilakukan")
