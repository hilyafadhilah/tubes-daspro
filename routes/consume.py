# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

from modules.store import UpdateOne, InsertOne, FindOne, FindBy, GetCurrentUser
from modules.inputs import PromptLoop, InputDate, InputInt

def RequestConsumableRoute():
    userId = GetCurrentUser()['id'] # Belum ada fungsi untuk menentukan user/admin

    #Input dan validasi
    
    consumableId, consumable = PromptLoop(
        msg = 'Masukkan ID item : ',
        until = IsConsumableAvailable,
        err = PrintConsumableError,
        bag = True
    )

    #Menampilkan stok consumable yang tersedia

    print(f"Stok consumable {consumable['nama']} : {consumable['jumlah']}")

    #Input dan validasi consumable quantity dan tanggal pengambilan
    
    quantity = InputInt('Jumlah permintaan: ', min = 1, max=consumable['jumlah'])
    request_date = InputDate('Tanggal permintaan: ')
    
    # Update data
    
    UpdateOne('consumable', consumableId, {'jumlah': consumable['jumlah'] - quantity})

    InsertOne('consumable_history', autoId=True, value={
        'id_pengambil' : userId,
        'id_consumable' : consumableId,
        'tanggal_pengambilan' : request_date,
        'jumlah' : quantity
    })

    #Success
    print(f"Item {consumable['nama']} (x{quantity}) telah berhasil diammbil.")

def IsConsumableAvailable(consumableId):
    consumable = FindOne('consumable', consumableId)

    if consumable is None:
        # Gadget not found
        return False, None
    else:
        if consumable['jumlah'] ==  0:
            return False, consumable

    return True, consumable

def PrintConsumableError(consumeId, bag):
    if bag is None:
        print(f"Consumable dengan ID {consumeId} tidak ditemukan")
    else:
        print(
            f"Kamu sedang meminta {bag['nama']}.\n" +
            "Tidak bisa meminta consumable stok kosong"
        )
