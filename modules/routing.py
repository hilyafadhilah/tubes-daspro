# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/routing
#   Berisi subprogram untuk keperluan pencocokan command
#   masukan user dengan rute yang harus diambil

# DEKLARASI SUBPROGRAM
from modules.utils import ListFind
from modules.store import GetCurrentUser
from modules.view import PrintHeader

# function IsRouteAuthorized (
#   route : RouteMapping,
#   user : UserData | None
# ) --> boolean
def IsRouteAuthorized(route, user):
    # Memeriksa apakah user memiliki otorisasi untuk mengakses route
    #   I.S. Masukan: rute, user
    #   F.S. Keluaran: boolean apakah user terotorisasi 
    # ALGORITMA SUBPROGRAM
    if len(route['roles']) == 0:
            return True
    if (user is not None) and (user['role'] in route['roles']):
            return True
    return False

def Enroute(routes, cmd):
    # Melakukan pengarahan rute pengguna
    #   I.S. Masukan: list rute, command oleh pengguna
    #   F.S. User diarahkan ke rute yang dipilihnya, jika mempunyai akses
    #        Jika rute tidak ada atau tidak memiliki akses, tampilkan error
    #        Keluaran: boolean apakah user meminta keluar 

    # KAMUS LOKAL
    #   user : UserData | None
    #   route : RouteMapping

    # ALGORITMA SUBPROGRAM
    user = GetCurrentUser()
    route = ListFind(routes, match=lambda r, i: r['cmd'].lower() == cmd.lower())

    if route is None:
        print(f"Tidak ada command '{cmd}'. Ketik 'help' untuk bantuan.")
    elif not IsRouteAuthorized(route, user):
        print("Command tersebut tidak tersedia untuk kamu!")
    else:
        try:
            PrintHeader(route['cmd'].upper())
            route['func']()
        except KeyboardInterrupt:
            print(f'\n\nKeluar dari {cmd}.')

    print('')

    return cmd.lower() != 'exit'
