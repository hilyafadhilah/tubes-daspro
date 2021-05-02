from modules.utils import ListFind
from modules.store import GetCurrentUser
from modules.view import PrintHeader

def AuthorizeRoute(route, user):
    if user is None:
        if len(route['roles']) == 0:
            return True
    else:
        if user['role'] in route['roles']:
            return True
    return False

def Enroute(routes, cmd):
    user = GetCurrentUser()
    route = ListFind(routes, match=lambda r, i: r['cmd'].lower() == cmd.lower())

    if route is None:
        print(f"Tidak ada command '{cmd}'. Ketik 'help' untuk bantuan.")
    elif not AuthorizeRoute(route, user):
        print("Command tersebut tidak tersedia untuk kamu!")
    else:
        try:
            PrintHeader(route['cmd'].upper())
            route['func']()
        except KeyboardInterrupt:
            print(f'\n\nKeluar dari {cmd}.')

    print('')

    return cmd.lower() == 'exit'
