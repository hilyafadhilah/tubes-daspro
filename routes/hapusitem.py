#ALGORITMA
#Admin
def hapusitem():
    #hasil data belum diarahkan ke dalam file penyimpanan
    nama = "test"
    ID = str(input("Masukkan ID item: "))
    if (isID(ID,ID)==2):#apakah ID ada di file penyimpanan atau tidak
        #Bila ada
        print("Apakan Anda yakin ingin menghapus "+str(nama), end="")
        isHapus=str(input(" (Y/N)? "))
        if isHapus == "Y":
            print('\n')
            if (ID[0]=='G'):
                arr=FindBy('gadget',{'ID':ID})
                del arr[0]
                UpdateOne('gadget',ID,value=arr[0])
            elif (ID[0]=='C'):
                arr=FindBy('consumable',{'ID':ID})
                del arr[0]
                UpdateOne('consumable',ID,value=arr[0])

            print("Item telah berhasil dihapus dari database.")
    #Bila tida ada
    elif(isID(ID,ID)==1):
        print("\n")
        print("Tidak ada item dengan ID tersebut.")