from modules.store import FindBy, GetCollection
from modules.utils import ListFilter
from modules.view import PrintHeader, ShowEachEntry

def CariRarityRoute():
    rarity = input("Masukkan rarity: ")

    if rarity in ['C', 'B', 'A', 'S']:
        items = FindBy('gadget', { 'rarity': rarity })
        PrintHeader('Hasil Pencarian')
        ShowEachEntry(items, PrintItem)
    else:
        print("Rarity tidak valid.")

def CariTahunRoute():
    tahun = int(input("Masukkan tahun: "))
    kategori= input("Masukkan kategori: ")

    #Misalkan pencarian tahun sebagai berikut
    #Belum dilakukan pengecekan masing masing file
    if (kategori == "="):#gadget terbit pada tahun
        match=lambda x: x['tahun_ditemukan']== tahun
    elif (kategori == ">"):#gadget terbit setelah tahun
        match=lambda x: x['tahun_ditemukan'] > tahun
    elif (kategori == "<"):#gadget terbit sebelum tahun
        match=lambda x: x['tahun_ditemukan'] < tahun
    elif (kategori == ">="):#gadget terbit setelah pada tahun
        match=lambda x: x['tahun_ditemukan'] >= tahun
    elif (kategori == "<="):#gadget terbit sebelum pada tahun
        match=lambda x: x['tahun_ditemukan'] <= tahun
    else:
        match=None

    if match is not None:
        gadgets = GetCollection('gadget')
        items = ListFilter(gadgets, match)
        ShowEachEntry(items, PrintItem)
    else:
        print("Kategori tidak valid.")

def PrintItem(idx, gadget):
    print(
        f"ID              : {gadget['id']}\n"
        f"Nama            : {gadget['nama']}\n" +
        f"Deskripsi       : {gadget['deskripsi']}\n" +
        f"Jumlah          : {gadget['jumlah']}\n" +
        f"Rarity          : {gadget['rarity']}\n" +
        f"Tahun ditemukan : {gadget['tahun_ditemukan']}\n"
    )
