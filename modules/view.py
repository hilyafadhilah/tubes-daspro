from modules.utils import ListFind

def MatchRoute(routes, cmd):
    return ListFind(routes, match=lambda r, i, c: r['cmd'] == c, args=[cmd])

def Confirm(msg):
    value = input(msg + ' (Y/N): ')
    return value in 'Yy'

def ShowEachEntry(entries, display = print, displayArgs = {}, jump = 5):
    total = len(entries)
    start = 0
    count = jump if jump <= total else total

    showNext = True

    while showNext:
        print('')

        for i in range(start, start + count):
            display(entries[i], **displayArgs)

        if count == 1:
            print(f"Menampilkan entri {start + 1} dari {total}.")
        else:
            print(f"Menampilkan entri {start + 1} - {start + count} dari {total}.")

        start = start + count

        if jump > (total - start):
            count = total - start

        if start >= total:
            showNext = False
        else:
            showNext = Confirm(f"Tampilkan {count} entri selanjutnya?")
