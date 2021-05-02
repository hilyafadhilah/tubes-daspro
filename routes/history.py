from modules.store import GetCollection, FindOne
from modules.view import ShowEachEntry, GetItemName
from modules.utils import DateToString

def ShowHistoryList(collection, sortColumn, display):
    histories = GetCollection(collection)
    histories.sort(key=lambda k: k[sortColumn], reverse=True)
    ShowEachEntry(histories, display=display)

def ConsumableHistoryRoute():
    ShowHistoryList(
        collection='consumable_history',
        sortColumn='tanggal_pengambilan',
        display=ShowConsumableHistory
    )

def BorrowHistoryRoute():
    ShowHistoryList(
        collection='gadget_borrow_history',
        sortColumn='tanggal_peminjaman',
        display=ShowBorrowHistory
    )

def ReturnHistoryRoute():
    ShowHistoryList(
        collection='gadget_return_history',
        sortColumn='tanggal_pengembalian',
        display=ShowReturnHistory
    )

def ShowConsumableHistory(idx, history):
    user = FindOne('user', history['id_pengambil'])
    consumable = FindOne('consumable', history['id_consumable'])
    itemName = GetItemName(history['id_consumable'], consumable)

    print(
        f"[{idx + 1}]\n" +
        f"ID Pengambilan      : {history['id']}\n" +
        f"Nama Pengambil      : {user['nama']}\n" +
        f"Nama Consumable     : {itemName}\n" +
        f"Tanggal Pengambilan : {DateToString(history['tanggal_pengambilan'])}\n" +
        f"Jumlah              : {history['jumlah']}\n"
    )

def ShowBorrowHistory(idx, history):
    user = FindOne('user', history['id_peminjam'])
    gadget = FindOne('gadget', history['id_gadget'])
    itemName = GetItemName(history['id_gadget'], gadget)

    print(
        f"[{idx + 1}]\n" +
        f"ID Peminjaman      : {history['id']}\n" +
        f"Nama Peminjam      : {user['nama']}\n" +
        f"Nama Gadget        : {itemName}\n" +
        f"Tanggal Peminjaman : {DateToString(history['tanggal_peminjaman'])}\n" +
        f"Jumlah             : {history['jumlah']}\n"
    )

def ShowReturnHistory(idx, history):
    borrow = FindOne('gadget_borrow_history', history['id_peminjaman'])
    user = FindOne('user', borrow['id_peminjam'])
    gadget = FindOne('gadget', borrow['id_gadget'])
    itemName = GetItemName(borrow['id_gadget'], gadget)

    print(
        f"[{idx + 1}]\n" +
        f"ID Pengembalian      : {history['id']}\n" +
        f"Nama Peminjam        : {user['nama']}\n" +
        f"Nama Gadget          : {itemName}\n" +
        f"Tanggal Pengembalian : {DateToString(history['tanggal_pengembalian'])}\n" +
        f"Jumlah               : {history['jumlah']}\n"
    )
