# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/inputs
#   Berisi subprogram yang berhubungan dengan input dan validasi da

# DEKLARASI SUBPROGRAM
from modules.utils import StringToDate

# INPUT

# function Confirm (msg : string) --> bool
def Confirm(msg):
    # Menampilkan pesan msg untuk meminta konfirmasi pengguna
    #   I.S. Masukan: pesan prompt
    #   F.S. Keluaran: konfirmasi dari pengguna dalam boolean 

    # KAMUS LOKAL
    #   value : string

    # ALGORITMA SUBPROGRAM
    while True:
        value = input(msg + ' (Y/N): ')
        if (value in ['Y', 'y']) or (value in ['N', 'n']):
            break
    return value in 'Yy'

# function PromptLoop (
#   msg : string,
#   until : (inp : string) --> any | (inp : string) --> [any, any],
#   err : string | (inp: string, bag : any),
#   bag : bool = false
# ) --> string
def PromptLoop(msg, until, err = 'Invalid.', bag = False):
    # Meminta masukan dari pengguna secara iteratif hingga inputnya valid,
    #   yaitu nilai true dari fungsi until. Apabila tidak, menampilkan error err.
    #   Apabila bag tidak terdefinisi, maka err (apabila bertipe prosedur) diasumsikan
    #      menerima nilai masukan dan return value dari fungsi until.
    #          I.S. Masukan: pesan prompt, fungsi validasi, error handling
    #          F.S. Keluaran: string hasil input yang tervalidasi
    #   Apabila bag bernilai true, maka fungsi until diasumsikan mengembalikan dua nilai
    #      (nilai validitas dan “tas” utk data tambahan)
    #      dan err (apabila bertipe prosedur) diasumsikan menerima dua nilai
    #      (nilai masukan dan “tas”)
    #          I.S. Masukan: pesan prompt, fungsi validasi, error handling, boolean bag
    #          F.S. Keluaran: string hasil input yang tervalidasi, bag penyimpan data

    # KAMUS LOKAL
    #   inp : string
    #   bg : any

    # ALGORITMA SUBPROGRAM
    while True:
        inp = input(msg)

        if bag is True:
            valid, bg = until(inp)
        else:
            valid = bg = until(inp)

        if valid is True:
            break

        if callable(err):
            err(inp, bg)
        else:
            print(err)

    if bag is True:
        return inp, bg
    else:
        return inp

def InputDate(prompt):
    _, value = PromptLoop(
        msg=prompt,
        until=ValidateDate,
        err='Tanggal tidak valid! Format: DD/MM/YYYY',
        bag=True
    )

    return value

# function InputInt (prompt : string, min : int, max : int) --> int
def InputInt(prompt, min, max):
    # Meminta masukan pengguna bertipe integer, memvalidasi, dan
    #   mengembalikan nilainya bertipe integer
    #   I.S. Masukan: pesan prompt
    #   F.S. Keluaran: input bertipe integer tervalidasi

    # KAMUS LOKAL
    #   ErrMsg : (value : string, bag : any)
    #   value : int

    # ALGORITMA SUBPROGRAM
    def ErrMsg(value, bag):
        if bag is None:
            print('Bukan angka yang valid!')
        else:
            print(f'Angka harus di antara {min} - {max}.')

    _, value = PromptLoop(
        msg=prompt,
        until=GetNumericValidator(min, max),
        err=ErrMsg,
        bag=True
    )

    return value

# VALIDATION

# function ValidateDate (inp : string) --> [boolean, Datetime | null]
def ValidateDate(inp):
    # Fungsi validasi utk dimasukkan ke fungsi PromptLoop() sbg parameter until
    #   memeriksa apakah nilai input adalah tanggal yang valid dan
    #   mengembalikan nilai yang sudah diubah ke tipe Datetime jika valid
    #   I.S. Masukan: input string
    #   F.S. Keluaran: validitas string, nilai value

    # KAMUS LOKAL
    #   value : Datetime

    # ALGORITMA SUBPROGRAM
    try:
        value = StringToDate(inp)
        return True, value
    except ValueError:
        return False, None

# function GetNumericValidator (
#   min : integer | None = None,
#   max : integer | None = None
# ) --> (
#   (inp : string) --> [bool, any]
# )
def GetNumericValidator(min = None, max = None):
    # Fungsi yang menghasilkan fungsi validasi
    #   utk dimasukkan ke fungsi PromptLoop() sbg parameter until
    #   memeriksa apakah nilai input adalah integer yang valid
    #   dan berada pada batas yg ditentukan, kemudian
    #   mengembalikan nilai tambahan -1 jika nilainya di bawah minimum
    #   atau 1 jika nilainya di atas maximum, atau nilai yang sudah
    #   diubah ke integer jika valid
    #   I.S. Masukan : nilai minimum dan maksimum (jika ada)
    #   F.S. Keluaran : fungsi validasi untuk dipakai pada PromptLoop() 

    # KAMUS LOKAL
    #   function validator : (inp : string) --> [bool, any]

    # ALGORITMA SUBPROGRAM
    def Validator(inp):
        try:
            value = int(inp)
            if min is not None and value < min:
                return False, -1
            elif max is not None and value > max:
                return False, 1
        except ValueError:
            return False, None
        return True, value
    
    return Validator
