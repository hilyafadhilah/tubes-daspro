# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/view
#   Berisi subprogram yang berhubungan dengan antarmuka pengguna

# DEKLARASI SUBPROGRAM
import os
from time import sleep
from modules.inputs import Confirm

# procedure ClearScreen ()
def ClearScreen():
    # Membersihkan layar terminal
    #   I.S. Layar terminal berisi output sebelumnya
    #   F.S. Layar terminal kosong
    # ALGORITMA SUBPROGRAM
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# procedure PrintDelayed (msg : string)
def PrintDelayed(msg):
    # Menampilkan pesan msg dengan penundaan satu detik
    #   I.S. Tidak ada pesan
    #   F.S. Pesan ditampilkan setelah satu detik
    # ALGORITMA SUBPROGRAM
    sleep(1)
    print(msg)

# procedure PrintBanner ()
def PrintBanner():
    # Menampilkan banner program
    #   I.S. Tidak ada banner
    #   F.S. Banner ditampilkan setelah satu detik 
    # ALGORITMA SUBPROGRAM
    PrintDelayed(
"""
________________________________________________________________________________
    _    _                                          __                          
    /  ,'                                           / |        ,         ,   /  
---/_.'------__----__--_/_----__----__----__-------/__|------------__-------/__-
  /  \     /   ) /   ) /    /   ) /   ) /   )     /   |      /   /   ) /   /   )
_/____\___(___(_/___/_(_ __(___/_/___/_(___/_____/____|_____/___(___(_/___(___/_
                                          /                /                    
                                      (_ /             (_ / 
"""
    )

# procedure Welcome ()
def Welcome():
    # Menampilkan pesan sambutan program
    #   I.S. Tidak ada pesan sambutan
    #   F.S. Pesan sambutan ditampilkan 
    # ALGORITMA SUBPROGRAM
    PrintBanner()
    PrintDelayed(" Selamat datang di Kantong Ajaib Doremonangis.")
    PrintDelayed(" Masukkan command. Ketik 'help' untuk bantuan.\n")

# procedure Goodbye ()
def Goodbye():
    # Menampilkan pesan penutup program
    #   I.S. Tidak ada pesan penutup
    #   F.S. Pesan penutup ditampilkan 
    # ALGORITMA SUBPROGRAM
    PrintHeader("Selamat Tinggal!", True)
    PrintBanner()

# procedure PrintHeader (title : string, delayed : boolean = false)
def PrintHeader(title, delayed = False):
    # Menampilkan header dengan panjang fixed
    #   I.S. Tidak ada header
    #   F.S. Header dioutput 

    # KAMUS LOKAL
    #   n : int

    # ALGORITMA SUBPROGRAM
    n = (60 - len(title) - 4) // 2

    if n > 0:
        header = f"\n {'=' * n} {title} {'=' * n}\n"
    else:
        header = '\n' + title + '\n'

    if delayed:
        PrintDelayed(header)
    else:
        print(header)

def GetItemName(itemId, item):
    if item is not None:
        return item['nama']
    else:
        return f"[Deleted Item {itemId}]"

# procedure PrintNumbered (
#   entries : list of T,
#   each : (el : T, ...) = print,
#   key : (el : T, ...) | None = None
# )
def PrintNumbered(entries, each = print, key = None):
    # Menampilkan data sebagai daftar bernomor
    #   I.S. Masukan: list data, fungsi utk setiap data, fungsi akses data
    #   F.S. Data ditampilkan dengan nomor terurut di sebelah kirinya 

    # KAMUS LOKAL
    #   maxSpace, spacing : int

    # ALGORITMA SUBPROGRAM
    if len(entries) == 0:
        print("Tidak ada entri.")
    else:
        maxSpace = len(str(len(entries)))

        for i in range(len(entries)):
            spacing = maxSpace - len(str(i + 1))
            print(f"{' ' * spacing}{i + 1}. ", end='')

            if callable(key):
                each(key(entries[i]))
            else:
                each(entries[i])

# procedure ShowEachEntry (
#   entries : list of T,
#   display : (idx : integer, el : T) = output,
#   pageSize : integer = 5
# )
def ShowEachEntry(entries, display = print, pageSize = 5):
    # Menampilkan data dengan pagination
    #   I.S. Masukan: list data, fungsi utk tampilan setiap data, ukuran page
    #   F.S. Data ditampilkan dengan pagination 

    # KAMUS LOKAL
    #   total, start, count : int
    #   showNext : bool

    # ALGORITMA SUBPROGRAM
    total = len(entries)

    if total == 0:
        print("Tidak ada entri.")
    else:
        start = 0
        count = pageSize if pageSize <= total else total

        showNext = True

        while showNext:
            print('')

            for i in range(start, start + count):
                display(i, entries[i])

            if count == 1:
                print(f"Menampilkan entri {start + 1} dari {total}.")
            else:
                print(f"Menampilkan entri {start + 1} - {start + count} dari {total}.")

            start += count

            if pageSize > (total - start):
                count = total - start

            if start >= total:
                showNext = False
            else:
                showNext = Confirm(f"Tampilkan {count} entri selanjutnya?")
