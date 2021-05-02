from modules.store import GetCollection, FindOne, InsertOne, UpdateOne, GetCurrentUser
from modules.utils import ListFilter
from modules.gamble import Random, InitGachaPoints, CalculateItemBoost, AddGachaPoints, RollGacha
from modules.view import Confirm, PrintNumbered, PrintHeader
from modules.inputs import PromptLoop, InputDate, InputInt

# procedure GachaRoute()
def GachaRoute():
    # Melakukan peningkatan rarity consumable secara gambling
    # 	I.S. Data awal consumable
    # 	F.S. Consumable yang digunakan berkurang jumlahnya,
    # 	     Consumable yang didapatkan bertambah jumlahnya,
    # 	     Riwayat pengambilan consumable bertambah

    # KAMUS LOKAL
    # 	points, boost : GachaPoints
    # 	consumes : list of < idx : integer, qty : integer >
    # 	idx, qty : integer
    # 	result : GachaResult

    # ALGORITMA SUBPROGRAM
    consumables = GetCollection('consumable')

    if len(consumables) == 0:
        print("Tidak ada consumable. Tidak dapat melakukan gacha.")
    else:
        points = InitGachaPoints(consumables)
        consumes = []

        cont = True
        while cont:
            PrintHeader('INVENTORY')
            PrintNumbered(consumables, ShowEachConsumable)
            print('')

            idx = InputConsumableIndex(consumables)
            qty = InputInt('Jumlah yang digunakan: ', min=1, max=consumables[idx]['jumlah'])

            consumables[idx]['jumlah'] -= qty
            consumes.append((idx, qty))

            print(f"{consumables[idx]['nama']} (x{qty}) ditambahkan!\n")

            # boost
            boost = CalculateItemBoost(consumables[idx], qty)

            PrintGachaPoints(points, boost)
            points = AddGachaPoints(points, boost)

            if not Confirm('Tambahkan item lagi?'):
                cont = False

        date = InputDate('Masukkan tanggal roll gacha: ')

        PrintHeader('Rolling Gacha...')
        result = RollGacha(points, consumables)

        print(
            f"Selamat, kamu mendapatkan {result['item']['nama']} " +
            f"(Rarity {result['item']['rarity']}) (x{result['qty']})!"
        )

        # Masukkan ke data
        userId = GetCurrentUser()['id']

        for idx, qty in consumes:
            UpdateOne('consumable', consumables[idx]['id'], {
                'jumlah': consumables[idx]['jumlah']
            })

            InsertOne('consumable_history', autoId=True, value={
                'id_pengambil': userId,
                'id_consumable': consumables[idx]['id'],
                'tanggal_pengambilan': date,
                'jumlah': qty
            })

        UpdateOne('consumable', result['item']['id'], {
            'jumlah': result['item']['jumlah'] + result['qty']
        })

def InputConsumableIndex(items):
    def IsValidConsumable(inp):
        try:
            idx = int(inp) - 1
            if idx < 0:
                return False, -1
            elif idx >= len(items):
                return False, 1
            elif items[idx]['jumlah'] < 1:
                return False, items[idx]
        except ValueError:
            return False, None
        return True, idx

    def ErrMsg(inp, bag):
        if bag is None:
            print('Bukan nomor yang valid!')
        elif bag == 1 or bag == -1:
            print(f'Nomor harus di antara 1 - {len(items)}.')
        else:
            print(f"Stok item {bag['nama']} sudah habis!")

    _, value = PromptLoop(
        msg='Pilih consumable yang ingin digunakan: ',
        until=IsValidConsumable,
        err=ErrMsg,
        bag=True
    )

    return value

def ShowEachConsumable(consumable):
    print(
        consumable['nama'],
        f"(Rarity {consumable['rarity']})",
        f"({consumable['jumlah']})"
    )

def PrintGachaPoints(pnts, boost = None):
    cur = AddGachaPoints(pnts, boost)

    print('Point gacha kamu:')
    for rarity in pnts:
        new = ''

        if rarity in boost:
            if boost[rarity] > 0:
                new = f" (+{boost[rarity]})"
            elif boost[rarity] < 0:
                new = f" ({boost[rarity]})"

        print(f" Rarity {rarity} : {cur[rarity]}{new}")
    print('')
