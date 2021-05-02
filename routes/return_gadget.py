from modules.store import FindOne, FindBy, UpdateOne, InsertOne, GetCurrentUser
from modules.inputs import PromptLoop, GetNumericValidator, InputInt, InputDate
from modules.view import PrintNumbered, GetItemName

def ReturnGadgetRoute():
    userId = GetCurrentUser()['id']

    # 1. Fetch list of unreturned items and display it

    borrows = FindBy('gadget_borrow_history', { 'id_peminjam': userId, 'is_returned': 'F' })
    PrintNumbered(borrows, each=ShowEachBorrow)

    # 2. Input and validate selected item

    idx = InputInt('Masukkan nomor peminjaman: ', min=1, max=len(borrows)) - 1

    # 3. Input and validate return qty and date

    borrow = borrows[idx]
    maxReturnQty = GetUnreturnedQty(borrow)

    qty = InputInt('Jumlah pengembalian: ', min=1, max=maxReturnQty)
    date = InputDate('Tanggal pengembalian: ')

    # 4. Update data store accordingly

    InsertOne('gadget_return_history', autoId=True, value={
        'id_peminjaman': borrow['id'],
        'tanggal_pengembalian': date,
        'jumlah': qty
    })

    if qty == maxReturnQty:
        # Return all, this item is no longer in borrowed state by the user
        UpdateOne('gadget_borrow_history', borrow['id'], { 'is_returned': 'T' })

    gadget = FindOne('gadget', borrow['id_gadget'])
    name = GetItemName(borrow['id_gadget'], gadget)

    if gadget is not None:
        UpdateOne('gadget', borrow['id_gadget'], { 'jumlah': gadget['jumlah'] + qty })
    else:
        # A deleted item is being returned
        InsertOne('gadget', {
            'id': borrow['id_gadget'],
            'nama': name,
            'deskripsi': None,
            'jumlah': qty,
            'rarity': None,
            'tahun_ditemukan': None
        })

    # 5. Success

    print(f"Item {name} (x{qty}) berhasil dikembalikan.")

def GetUnreturnedQty(borrow):
    # Count the number of unreturned items for this particular borrowing
    returned = FindBy('gadget_return_history', { 'id_peminjaman': borrow['id'] })
    return borrow['jumlah'] - sum(r['jumlah'] for r in returned)

def ShowEachBorrow(borrow):
    # Display each borrow entry
    gadget = FindOne('gadget', borrow['id_gadget'])
    name = GetItemName(borrow['id_gadget'], gadget)
    unreturnedQty = GetUnreturnedQty(borrow)

    print(f"{name} (x{unreturnedQty})")
