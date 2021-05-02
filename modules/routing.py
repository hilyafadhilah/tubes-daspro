from modules.utils import ListFind
from modules.store import GetCurrentUser
from modules.view import PrintHeader

def Enroute(routes, cmd):
    user = GetCurrentUser()
    route = ListFind(routes, match=lambda r, i: r['cmd'].lower() == cmd.lower())

    #if (len(route['roles']) == 0) or ((user is not None) and (user['role'] in route['roles'])):
    #    PrintHeader(route['cmd'].upper())
    #    route['func']()
    #else:
    #    print("Command tersebut tidak tersedia untuk kamu!")

    if route is None:
        print(f"Tidak ada command '{cmd}'. Ketik 'help' untuk bantuan.")
    else:
        PrintHeader(route['cmd'].upper())
        route['func']()

    print('')

    return cmd != 'exit'
