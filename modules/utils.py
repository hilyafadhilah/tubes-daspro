# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/utils
#   Berisi subprogram utilitas general yang berlingkup kecil
#   dan bertujuan membantu subprogram lainnya

# DEKLARASI SUBPROGRAM
from datetime import datetime

# function SplitByChar (str : string, sep : character) --> list of string
def SplitByChar(str, sep):
    # Memecah string berdasarkan satu karakter separator
    #   kemudian disusun kembali dalam array
    #   I.S. Masukan: string dan separator
    #   F.S. Keluaran: array berisi 

    # KAMUS LOKAL
    #   result : list of string
    #   buf : string

    # ALGORITMA SUBPROGRAM
    result = []
    buf = ''

    for i in range(len(str)):
        if (str[i] == sep):
            result.append(buf)
            buf = ''
        else:
            buf = buf + str[i]
    result.append(buf)

    return result

# function StringToDate (str : string) --> Datetime
def StringToDate(string):
    # Mengkonversi string format DD/MM/YYYY ke tipe Datetime
    #   I.S. Masukan: string dalam format DD/MM/YYYY
    #   F.S. Keluaran: datetime sesuai masukan 
    # ALGORITMA SUBPROGRAM
    return datetime.strptime(string, '%d/%m/%Y')

# function DateToString (date : Datetime) --> string
def DateToString(date):
    # Mengkonversi tipe Datetime ke string format DD/MM/YYYY
    #   I.S. Masukan: data datetime
    #   F.S. Keluaran: string dalam format DD/MM/YYYY sesuai masukan 
    # ALGORITMA SUBPROGRAM
    return date.strftime("%d/%m/%Y")

# function ListFindIndex (
#   lst : list of T,
#   match : (el : T, idx : integer) --> boolean
# ) --> integer
def ListFindIndex(lst, match):
    # Mencari index dari elemen pertama pada list lst
    #   yang bernilai true jika dimasukkan ke fungsi match
    #   I.S. Masukan: list item, fungsi matching
    #   F.S. Keluaran: index dari elemen yg cocok

    # KAMUS LOKAL
    #   i : int

    # ALGORITMA SUBPROGRAM
    i = 0
    while i < len(lst):
        if match(lst[i], i):
            return i
        i += 1
    return None

# function ListFind (
#   lst : list of T,
#   match : (el : T, idx : integer) --> boolean
# ) --> T
def ListFind(lst, match):
    # Mencari elemen pertama pada list lst
    #   yang bernilai true jika dimasukkan ke fungsi match 
    #   I.S. Masukan: list item, fungsi matching
    #   F.S. Keluaran: elemen yg cocok 

    # KAMUS LOKAL
    #   idx : int

    # ALGORITMA SUBPROGRAM
    idx = ListFindIndex(lst, match)
    return lst[idx] if idx is not None else None

# function ListFilter (
#   lst : list of T,
#   match : (el : T, idx : integer) --> boolean
# ) --> list of T
def ListFilter(lst, match):
    # Mencari seluruh elemen pada list lst
    #   yang bernilai true jika dimasukkan ke fungsi match
    #   I.S. Masukan: list item, fungsi matching
    #   F.S. Keluaran: list berisi elemen yg cocok

    # KAMUS LOKAL
    #   result : list of T

    # ALGORITMA SUBPROGRAM
    result = []
    for i in range(len(lst)):
        if match(lst[i], i):
            result.append(lst[i])
    return result
