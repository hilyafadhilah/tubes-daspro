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

    if cmd != 'exit':
        if route is None:
            print(f"Tidak ada command '{cmd}'. Ketik 'help' untuk bantuan.")
        else:
            try:
                PrintHeader(route['cmd'].upper())
                route['func']()
            except KeyboardInterrupt:
                print(f'\n\nKeluar dari {cmd}.')

        print('')
        return True

    return False
