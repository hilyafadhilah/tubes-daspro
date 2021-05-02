from modules.store import FindOne, InsertOne, DeleteOne
from modules.inputs import Confirm

#ALGORITMA
#ifAdmin
def isRarity(rarity):       #Fungsi menerima input char untuk menentukan bahwa input adalah valid dan sesuai kriteria.
    return rarity in ['C', 'B', 'A', 'S']

def isID(ID): #0= id tidak valid, 1= ID tidak ada di database, 2= ID ada di database
    if len(ID) < 0 or ID[0] not in "CG":
        return 0, None
    else:
        if ID[0] == 'C':
            tipe = 'consumable'
        elif ID[0] == 'G':
            tipe = 'gadget'

        exist = FindOne(tipe, ID)

        if exist is None:
            return 1, tipe
        else:
            return 2, exist
    
def TambahItemRoute():    
    ID = str(input("Masukan ID: "))
    valid, tipe = isID(ID)

    if valid == 0:
        print("Gagal menambahkan item karena ID tidak valid.")
    elif valid == 2:
        print("Gagal menambahkan item karena ID sudah ada")
    else:
        nama = str(input("Masukkan Nama: "))
        deskripsi = str(input("Masukkan Deskripsi: "))
        jumlah = int(input("Masukkan Jumlah: "))
        rarity = str(input("Masukkan Rarity: "))

        if not isRarity(rarity):
            print("Input rarity tidak valid.")
        else:
            value = {
                'id':ID,
                'nama': nama,
                'deskripsi': deskripsi,
                'jumlah': jumlah,
                'rarity': rarity
            }

            if (tipe == 'gadget'):
                tahun = int(input("Masukkan tahun ditemukan: "))
                value['tahun_ditemukan'] = tahun
            
            InsertOne(tipe, value)
            print("Item berhasil ditambahkan ke database.")

#ALGORITMA
#Admin
def HapusItemRoute():
    #hasil data belum diarahkan ke dalam file penyimpanan
    ID = str(input("Masukkan ID item: "))
    valid, item = isID(ID) #apakah ID ada di file penyimpanan atau tidak
    if valid == 0:
        print("ID tidak valid.")
    elif valid == 1:
        #Bila tida ada
        print("Tidak ada item dengan ID tersebut.")
    else:
        #Bila ada
        if Confirm("Apakan Anda yakin ingin menghapus "+str(item['nama'])+"?"):
            if (ID[0]=='G'):
                DeleteOne('gadget', ID)
            elif (ID[0]=='C'):
                DeleteOne('consumable', ID)

            print("Item telah berhasil dihapus dari database.")
