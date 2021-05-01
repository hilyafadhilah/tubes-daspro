from modules.store import FindOne, FindBy, UpdateOne

#Masih butuh fungsi untuk role nya juga
def ChangeStockRoute():
    item_id = input("Masukkan ID : ")
    if item_id == '' or item_id[0] not in "CG":
        print("ID tidak valid")
    else:
        if item_id[0] == 'C':
            tipe = 'consumable'
        else:
            tipe = 'gadget'
        qty = int(input("Masukkan jumlah : "))
        item = FindOne(tipe, item_id)

        if item is None:
            print("Tidak ada item dengan ID tersebut!")
        else:
            if qty < 0 :
                BuangItem(tipe, item, qty)
            elif qty > 0:
                TambahItem(tipe, item, qty)
            else:
                print(f"Tidak ada barang yang ditambahkan. Stok sekarang : {item['jumlah']}")

def ValidId(tipe, id):
    return FindOne(tipe,id) is not None

def BuangItem(tipe, item, qty):
    if int(item['jumlah']) + qty < 0:
        print(f"{qty} {item['nama']} gagal dibuang karena stok kurang. Stok sekarang: {item['jumlah']} (<{qty})")
    else :
        UpdateOne(tipe, id, {'jumlah' : str(int(item['jumlah']) - qty)})
        print(f"{qty} {item['nama']} berhasil dibuang. Stok sekarang : {int(item['jumlah']) - qty}")

def TambahItem(tipe, item, qty):
    UpdateOne(tipe, id, {'jumlah' : str(int(item['jumlah']) + qty)})
    print(f"{qty} {item['nama']} berhasil ditambahkan. Stok sekarang : {int(item['jumlah']) + qty}")