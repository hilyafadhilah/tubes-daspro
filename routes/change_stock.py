# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

from modules.store import FindOne, FindBy, UpdateOne

#Masih butuh fungsi untuk role nya juga
def ChangeStockRoute():
    itemId = input("Masukkan ID : ")
    if itemId == '' or itemId[0] not in "CG":
        print("ID tidak valid")
    else:
        if itemId[0] == 'C':
            tipe = 'consumable'
        else:
            tipe = 'gadget'
        qty = int(input("Masukkan jumlah : "))
        item = FindOne(tipe, itemId)

        if item is None:
            print("Tidak ada item dengan ID tersebut!")
        else:
            if qty < 0 :
                BuangItem(tipe, item, qty)
            elif qty > 0:
                TambahItem(tipe, item, qty)
            else:
                print(f"Tidak ada barang yang ditambahkan. Stok sekarang : {item['jumlah']}")

def BuangItem(tipe, item, qty):
    if int(item['jumlah']) + qty < 0:
        print(f"{(-1)*qty} {item['nama']} gagal dibuang karena stok kurang. Stok sekarang: {item['jumlah']} (<{qty})")
    else :
        newQty = item['jumlah'] + qty
        UpdateOne(tipe, item['id'], {'jumlah' : newQty})
        print(f"{(-1)*qty} {item['nama']} berhasil dibuang. Stok sekarang : {newQty}")

def TambahItem(tipe, item, qty):
    newQty = item['jumlah'] + qty
    UpdateOne(tipe, item['id'], {'jumlah' : newQty})
    print(f"{qty} {item['nama']} berhasil ditambahkan. Stok sekarang : {newQty}")
