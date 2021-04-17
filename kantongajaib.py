from modules.constants import collections, commands
from modules.args import ParseArgs
from modules.load import LoadAll
from modules.store import InitStore

args = ParseArgs()
dirname = args.dirname

InitStore(LoadAll(collections, dirname))

while True:
    command = input('>>> ')

    if command in commands:
        commands[command]()
