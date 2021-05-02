#ALGORITMA
#ifAdmin
#isGadget belum mengvalidasi bila id sudah ada atau belum
#hasil data belum diarahkan ke dalam file penyimpanan
def isRarity(rarity):       #Fungsi menerima input char untuk menentukan bahwa input adalah valid dan sesuai kriteria.
    if (rarity == "C"):
        isValid = True
    elif (rarity == "B"):
        isValid = True
    elif (rarity == "A"):
        isValid = True
    elif (rarity == "S"):
        isValid = True
    else:
        isValid = False
    return isValid

def isID(x,ID):
    if (x[0]=="G"):
        if (len(FindBy('gadget', {'ID':ID})==0)):   #Bila ID gadget tidak ada di database, maka valid untuk ditambahkan
            isID1=1                                 #0= id tidak valid, 1= ID tidak ada di database, 2= ID ada di database
        else:
            isID1=2
    elif (x[0]=="C"):
        if (len(FindBy('consumable', {'ID':ID})==0)):
            isID1 = 1
        else :
            isID1 = 2
    else:
        isID1 = 0
    return isID1   
    
def tambahitem():    
    ID = str(input("Masukan ID: "))
    if (isID(ID,ID)==1) :
        print('\n')
        nama = str(input("Masukkan Nama: "))
        deskripsi = str(input("Masukkan Deskripsi: "))
        jumlah = int(input("Masukkan Jumlah: "))
        rarity = str(input("Masukkan Rarity: "))
        isRarity(rarity)

        if isRarity(rarity): 
            if (ID[0] == ("G")):
                tahun = str(input("Masukkan tahun ditemukan: "))
                insertone('gadget', value={        #Fungsi insertone memasukkan nilai-nilai ke dalam database
                'id':ID,
                'nama': nama,
                'deskripsi': deskripsi,
                'jumlah': jumlah,
                'rarity': rarity,
                'tahun_ditemukan': tahun
                },autoID=False)
            elif (ID[0] == "C") :
                insertone('gadget', value={        #Fungsi insertone memasukkan nilai-nilai ke dalam database
                'ID':ID,
                'nama': nama,
                'deskripsi': deskripsi,
                'jumlah': jumlah,
                'rarity': rarity
                },autoID=False)
            else:
                print ("EROR")
            print("Item berhasil ditambahkan ke database.")
        else:
            print("Input rarety tidak valid")
    elif (isID(ID, ID)==2):
        print('\n')
        print("Gagal menambahkan item karena ID sudah ada")
    elif (isID(ID,ID)==0):
        print("\n")
        print("Gagal menambahkan item karena ID tidak valid.")