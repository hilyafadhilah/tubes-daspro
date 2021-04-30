from modules.store import FindOne, FindBy, UpdateOne, InsertOne

#Masih butuh fungsi untuk role nya juga
def AddConsumableRoute():
    item_id = input("Masukkan ID : ")

    # Check item type according to id
    if item_id[0] == 'C':
        item_type = 'consumable'
    elif item_id[0] == 'G':
        item_type = 'gadget'

    if not ValidId(item_type, item_id):
        print("Tidak ada item dengan ID tersebut!")
    else:
        quantity = int(input("Masukkan Jumlah : "))
        if quantity < 0 :
            BuangItem(item_type, item_id, quantity)
        elif quantity > 0 :
            TambahItem(item_type, item_id, quantity)

def ValidId(tipe, id):
    if FindOne(tipe, id) is None :
        return False
    else:
        return True

def BuangItem(tipe, id, qty):
    item = FindOne(tipe, id)
    if int(item['jumlah']) + qty < 0:
        print(f"{qty} {item['nama']} gagal dibuang karena stok kurang. Stok sekarang: {item['jumlah']} (<{qty})")
    else :
        UpdateOne(tipe, id, {'jumlah' : str(int(item['jumlah']) - qty)})
        print(f"{qty} {item['nama']} berhasil dibuang. Stok sekarang : {int(item['jumlah']) - qty}")

def TambahItem(tipe, id, qty):
    item = FindOne(tipe, id)
    UpdateOne(tipe, id, {'jumlah' : str(int(item['jumlah']) + qty)})
    print(f"{qty} {item['nama']} berhasil ditambahkan. Stok sekarang : {int(item['jumlah']) + qty}")