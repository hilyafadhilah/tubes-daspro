from modules.constants import collectionsSchema, routes
from modules.args import ParseArgs, GetDirname
from modules.load import LoadAll
from modules.store import InitStore
from modules.view import MatchRoute

ParseArgs()
InitStore(LoadAll(collectionsSchema, dirname=GetDirname()))

while True:
    command = input('>>> ')
    route = MatchRoute(routes, command)

    if route != None:
        route['func']()
