import os
from modules.inputs import Confirm

def ClearScreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def GetItemName(itemId, item):
    if item is not None:
        return item['nama']
    else:
        return f"[Deleted Item {itemId}]"

def PrintNumbered(entries, each = print, key = None):
    maxSpace = len(str(len(entries)))

    for i in range(len(entries)):
        spacing = maxSpace - len(str(i + 1))
        print(f"{' ' * spacing}{i + 1}. ", end='')

        if callable(key):
            each(key(entries[i]))
        else:
            each(entries[i])

def ShowEachEntry(entries, display = print, pageSize = 5):
    total = len(entries)
    start = 0
    count = pageSize if pageSize <= total else total

    showNext = True

    while showNext:
        print('')

        for i in range(start, start + count):
            display(i, entries[i])

        if count == 1:
            print(f"Menampilkan entri {start + 1} dari {total}.")
        else:
            print(f"Menampilkan entri {start + 1} - {start + count} dari {total}.")

        start += count

        if pageSize > (total - start):
            count = total - start

        if start >= total:
            showNext = False
        else:
            showNext = Confirm(f"Tampilkan {count} entri selanjutnya?")
