from modules.constants import collectionsSchema, routes
from modules.args import ParseArgs, GetDirname
from modules.load import LoadAll
from modules.store import InitStore
from modules.routing import MatchRoute
from modules.view import ClearScreen

ParseArgs()
InitStore(LoadAll(collectionsSchema, dirname=GetDirname()))

ClearScreen()

while True:
    command = input('>>> ')
    route = MatchRoute(routes, command)

    if route is not None:
        route['func']()
        if command == "exit":
            break
