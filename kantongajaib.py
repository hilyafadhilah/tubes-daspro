# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Program kantongajaib
# Inventarisasi kantong ajaib Doremonangis
#   I.S.    Masukan: Nama folder yang berisi file CSV
#   F.S.    File CSV baru/diubah, apabila melakukan penyimpanan 

# KAMUS UTAMA
#   command : string
#   cont : boolean

# DEKLRASI SUBPROGRAM

from modules.constants import collectionsSchema
from modules.args import ParseArgs, GetDirname
from modules.load import LoadAll
from modules.store import InitStore
from modules.routing import Enroute
from modules.view import ClearScreen, Welcome, Goodbye
from routes.routes import routesMapping

# ALGORITMA PROGRAM UTAMA

try:
    ParseArgs()
    InitStore(LoadAll(collectionsSchema, dirname=GetDirname()))

    ClearScreen()
    Welcome()

    while True:
        command = input('>>> ')
        cont = Enroute(routesMapping, command)

        if cont is False:
            Goodbye()
            break
except KeyboardInterrupt:
    print('\n\n Keluar dari program.')
    exit()
