from modules.store import FindOne, FindBy, UpdateOne, InsertOne
from modules.inputs import PromptLoop, GetNumericValidator, InputQty, InputDate
from modules.view import PrintNumbered, GetItemName

def ReturnGadgetRoute():
    userId = 1 # @TODO: get current user

    # 1. Fetch list of unreturned items and display it

    borrows = FindBy('gadget_borrow_history', { 'id_peminjam': userId, 'is_returned': False })
    PrintNumbered(borrows, each=ShowEachBorrow)

    # 2. Input and validate selected item

    idx = InputBorrowIndex(len(borrows))

    # 3. Input and validate return qty and date

    borrow = borrows[idx]
    maxReturnQty = GetUnreturnedQty(borrow)

    qty = InputQty('pengembalian', min=1, max=maxReturnQty)
    date = InputDate('pengembalian')

    # 4. Update data store accordingly

    InsertOne('gadget_return_history', autoId=True, value={
        'id_peminjaman': borrow['id'],
        'tanggal_pengembalian': date,
        'jumlah': qty
    })

    if qty == maxReturnQty:
        # Return all, this item is no longer in borrowed state by the user
        UpdateOne('gadget_borrow_history', borrow['id'], { 'is_returned': True })

    gadget = FindOne('gadget', borrow['id_gadget'])

    if gadget is not None:
        UpdateOne('gadget', borrow['id_gadget'], { 'jumlah': gadget['jumlah'] + qty })
    else:
        # A deleted item is being returned
        InsertOne('gadget', value={
            'id': borrow['id_gadget'],
            'jumlah': qty,
            'nama': None,
            'deskripsi': None,
            'rarity': None,
            'tahun_ditemukan': None
        })

    # 5. Success

    name = GetItemName(borrow['id_gadget'], gadget)
    print(f"Item {name} (x{qty}) berhasil dikembalikan.")

def InputBorrowIndex(count):
    # Input and validate borrow index
    _, inp = PromptLoop(
        msg='Masukkan nomor peminjaman: ',
        until=GetNumericValidator(min=1, max=count),
        err=PrintIndexError,
        bag=True
    )

    return inp - 1

def PrintIndexError(inp, bag):
    # Output error message when index input is invalid
    if bag is None:
        print('Bukan angka yang valid!')
    else:
        print(f'Nomor peminjaman {inp} tidak ada.')

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
