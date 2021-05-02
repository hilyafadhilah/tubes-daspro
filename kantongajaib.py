from modules.constants import collectionsSchema
from modules.args import ParseArgs, GetDirname
from modules.load import LoadAll
from modules.store import InitStore
from modules.routing import Enroute
from modules.view import ClearScreen, Welcome
from routes.routes import routes

ParseArgs()
InitStore(LoadAll(collectionsSchema, dirname=GetDirname()))

ClearScreen()
#Welcome()

while True:
    command = input('>>> ')
    cont = Enroute(routes, command)

    if cont is False:
        break
