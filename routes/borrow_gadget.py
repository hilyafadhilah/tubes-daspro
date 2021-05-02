# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module routes/borrow_gadget
#   Berisi prosedur fitur peminjaman gadget

# DEKLARASI SUBPROGRAM
from modules.store import FindOne, FindBy, UpdateOne, InsertOne, GetCurrentUser
from modules.inputs import PromptLoop, InputDate, InputInt

# procedure BorrowGadgetRoute()
def BorrowGadgetRoute():
    # Rute peminjaman gadget
    #   I.S. Masukan: ID gadget yang dipinjam, jumlah, tanggal
    #   F.S. Data jumlah barang diupdate, riwayat peminjaman bertambah
    #        Keluaran: pesan berhasil

    # ALGORITMA SUBPROGRAM
    userId = GetCurrentUser()['id']

    # 1. Input and validate Gadget ID

    gadgetId, gadget = PromptLoop(
        msg='ID gadget: ',
        until=IsGadgetBorrowable,
        err=PrintBorrowableError,
        bag=True
    )

    # 2. Show available stock for that item

    print(f"Stok gadget {gadget['nama']}: {gadget['jumlah']}")

    # 3. Input and validate item qty and date of borrowing

    qty = InputInt('Jumlah peminjaman: ', min=1, max=gadget['jumlah'])
    date = InputDate('Tanggal peminjaman: ')

    # 4. Update data correspondingly

    UpdateOne('gadget', gadgetId, { 'jumlah': gadget['jumlah'] - qty })

    InsertOne('gadget_borrow_history', autoId=True, value={
        'id_peminjam' : userId,
        'id_gadget': gadgetId,
        'tanggal_peminjaman': date,
        'jumlah': qty,
        'is_returned': 'F'
    })

    # 5. Success

    print(f"Gadget {gadget['nama']} (x{qty}) berhasil dipinjam.")

def IsGadgetBorrowable(gadgetId):
    # Check if item with ID gadgetId is borrowable:
    #   The item exists and is not in borrowed state by the user

    userId = GetCurrentUser()['id']
    gadget = FindOne('gadget', gadgetId)

    if gadget is None:
        # Gadget not found
        return False, None
    elif gadget['jumlah'] == 0:
        return 0, gadget
    else:
        # Check if there's unreturned items
        unreturned = FindBy('gadget_borrow_history', {
            'id_peminjam': userId,
            'id_gadget': gadgetId,
            'is_returned': 'F'
        })

        if len(unreturned) > 0:
            # If the program is used consistently, there should only
            # be one unreturned item
            return False, gadget

    return True, gadget

def PrintBorrowableError(gadgetId, bag):
    # Outputs error based on the return value of IsGadgetBorrowable
    if bag is None:
        print(f"Gadget dengan ID {gadgetId} tidak ditemukan.")
    elif bag['jumlah'] == 0:
        print(f"Stok item {bag['nama']} sudah habis!")
    else:
        print(
            f"Kamu sedang meminjam {bag['nama']}.\n" +
            "Tidak bisa meminjam gadget yang sedang dipinjam."
        )
