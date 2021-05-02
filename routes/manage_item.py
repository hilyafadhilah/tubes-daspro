# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

from modules.store import FindOne, InsertOne, DeleteOne
from modules.inputs import Confirm

#ALGORITMA
#ifAdmin
def isRarity(rarity):       #Fungsi menerima input char untuk menentukan bahwa input adalah valid dan sesuai kriteria.
    return rarity in ['C', 'B', 'A', 'S']

def isID(id): #0= id tidak valid, 1= id tidak ada di database, 2= id ada di database
    if len(id) < 0 or id[0] not in "CG":
        return 0, None
    else:
        if id[0] == 'C':
            tipe = 'consumable'
        elif id[0] == 'G':
            tipe = 'gadget'

        exist = FindOne(tipe, id)

        if exist is None:
            return 1, tipe
        else:
            return 2, exist
    
def TambahItemRoute():    
    id = str(input("Masukan id: "))
    valid, tipe = isID(id)

    if valid == 0:
        print("Gagal menambahkan item karena id tidak valid.")
    elif valid == 2:
        print("Gagal menambahkan item karena id sudah ada")
    else:
        nama = str(input("Masukkan Nama: "))
        deskripsi = str(input("Masukkan Deskripsi: "))
        jumlah = int(input("Masukkan Jumlah: "))
        rarity = str(input("Masukkan Rarity: "))

        if not isRarity(rarity):
            print("Input rarity tidak valid.")
        else:
            value = {
                'id':id,
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
    id = str(input("Masukkan id item: "))
    valid, item = isID(id) #apakah id ada di file penyimpanan atau tidak
    if valid == 0:
        print("id tidak valid.")
    elif valid == 1:
        #Bila tida ada
        print("Tidak ada item dengan id tersebut.")
    else:
        #Bila ada
        if Confirm("Apakan Anda yakin ingin menghapus "+str(item['nama'])+"?"):
            if (id[0]=='G'):
                DeleteOne('gadget', id)
            elif (id[0]=='C'):
                DeleteOne('consumable', id)

            print("Item telah berhasil dihapus dari database.")
