from modules.store import GetCollection, FindOne
from modules.view import ShowEachEntry
from modules.utils import DateToString

def AbstractHistoryRoute(collection, sortColumn, display):
    histories = GetCollection(collection)
    histories.sort(key=lambda k: k[sortColumn], reverse=True)
    ShowEachEntry(histories, display=display)

def ConsumableHistoryRoute():
    AbstractHistoryRoute(
        collection='consumable_history',
        sortColumn='tanggal_pengambilan',
        display=ShowConsumableHistory
    )

def BorrowHistoryRoute():
    AbstractHistoryRoute(
        collection='gadget_borrow_history',
        sortColumn='tanggal_peminjaman',
        display=ShowBorrowHistory
    )

def ReturnHistoryRoute():
    AbstractHistoryRoute(
        collection='gadget_return_history',
        sortColumn='tanggal_pengembalian',
        display=ShowReturnHistory
    )

def ShowConsumableHistory(history):
    user = FindOne('user', history['id_pengambil'])
    consumable = FindOne('consumable', history['id_consumable'])

    print(
        f"ID Pengambilan      : {history['id']}\n" +
        f"Nama Pengambil      : {user['nama']}\n" +
        f"Nama Consumable     : {consumable['nama']}\n" +
        f"Tanggal Pengambilan : {DateToString(history['tanggal_pengambilan'])}\n" +
        f"Jumlah              : {history['jumlah']}\n"
    )

def ShowBorrowHistory(history):
    user = FindOne('user', history['id_peminjam'])
    gadget = FindOne('gadget', history['id_gadget'])

    print(
        f"ID Peminjaman      : {history['id']}\n" +
        f"Nama Peminjam      : {user['nama']}\n" +
        f"Nama Gadget        : {gadget['nama']}\n" +
        f"Tanggal Peminjaman : {DateToString(history['tanggal_peminjaman'])}\n" +
        f"Jumlah             : {history['jumlah']}\n"
    )

def ShowReturnHistory(history):
    borrow = FindOne('gadget_borrow_history', history['id_peminjaman'])
    user = FindOne('user', borrow['id_peminjam'])
    gadget = FindOne('gadget', borrow['id_gadget'])

    print(
        f"ID Pengembalian      : {history['id']}\n" +
        f"Nama Peminjam        : {user['nama']}\n" +
        f"Nama Gadget          : {gadget['nama']}\n" +
        f"Tanggal Pengembalian : {DateToString(history['tanggal_pengembalian'])}\n" +
        f"Jumlah               : {history['jumlah']}\n"
    )
