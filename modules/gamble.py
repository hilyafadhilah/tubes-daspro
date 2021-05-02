# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/gamble
#   Berisi subprogram untuk melakukan gacha, yaitu
#   meningkatkan rarity consumable secara gambling

# KAMUS UTAMA
#   type GachaRollResult : < item : ConsumableData, qty : integer >

# DEKLARASI SUBPROGRAM
import time
import math
from modules.constants import baseGachaPoints, pointsBoost
from modules.utils import ListFilter

# function Random () --> float
def Random():
    # Menghasilkan pseudorandom number antara 0 dan 1 dengan
    #   implementasi linear congruential generator (LCG)
    #   dengan konstanta borland dan nilai seed berupa time
    #   lihat https://en.wikipedia.org/wiki/Linear_congruential_generator
    #   I.S. Pemanggilan fungsi
    #   F.S. Keluaran: pseudorandom number antara 0 – 1

    # KAMUS LOKAL
    #   m, a, c, n : integer
    #   xn : float

    # ALGORITMA SUBPROGRAM
    m = 2 ** 32
    a = 22695477
    c = 1

    # karena seed berupa time, pastikan ada jeda
    # untuk setiap pemanggilan subprogram ini 
    time.sleep(0.001)

    xn = time.time()
    n = int(xn) % 16807

    for i in range(n):
        xn = (a * xn + c) % m
    
    return xn / m

# function RandomInt (min : integer, max : integer) --> integer
def RandomInt(min, max):
    # Menghasilkan integer pseudorandom menggunakan fungsi Random()
    #   I.S. Pemanggilan fungsi
    #   F.S. Keluaran: integer pseudorandom antara min – max

    # ALGORITMA SUBPROGRAM
    return min + math.floor(Random() * (max - min))

# function InitGachaPoints(items : CollectionData of ConsumableData) --> GachaPoints
def InitGachaPoints(items):
# Menginisialisasi poin gacha berdasarkan item yang ada
#   sehingga jika rarity X tidak ada di daftar item
#   maka rarity tersebut tidak terinisialisasi poinnya
#   I.S. Masukan: list consumable
#   F.S. Keluaran: gacha points inisial 


# KAMUS LOKAL
#   available : list of character
#   points : GachaPoints
#   rarity : string
#   pnts : integer

# ALGORITMA SUBPROGRAM
    global baseGachaPoints

    avlbl = list(set(map(lambda x: x['rarity'], items)))
    pnts = {}

    for r in baseGachaPoints:
        if r in avlbl:
            pnts[r] = baseGachaPoints[r]

    return pnts

# function CalculateItemBoost (item : ConsumableData, qty : integer) --> GachaPoints
def CalculateItemBoost(item, qty):
    # Mengkalkulasi boost (tambahan) gacha points dari suatu item
    #   dengan jumlah tertentu. Semakin banyak jumlah,
    #   semakin besar boost.
    #   I.S. Masukan: consumable, jumlahnya
    #   F.S. Keluaran: gacha points tambahan

    # KAMUS LOKAL
    #   boost : GachaPoints
    #   factor : int

    # ALGORITMA SUBPROGRAM
    global pointsBoost

    boost = {}
    ir = item['rarity']

    if ir in pointsBoost:
        for br in pointsBoost[ir]:
            factor = RandomInt(1, qty)
            boost[br] = pointsBoost[ir][br] * factor

    return boost

# function AddGachaPoints(gachaPnts : GachaPoints, boost : GachaPoints) --> GachaPoints
def AddGachaPoints(gachaPnts, boost):
    # Menambahkan boost ke dalam gacha points
    #   I.S. Masukan: poin saat ini, tambahan poin
    #   F.S. Keluaran: poin setelah ditambahkan

    # KAMUS LOKAL
    #   pnts : GachaPoints

    # ALGORITMA SUBPROGRAM
    pnts = {}

    for br in gachaPnts:
        pnts[br] = gachaPnts[br]
        if br in boost:
            pnts[br] += boost[br]

    return pnts

# function NormalizeGachaPoints(gachaPnts : GachaPoints) --> GachaPoints
def NormalizeGachaPoints(gachaPnts):
    # Menormalisasi nilai gacha points negatif sehingga nilai 0
    #   diletakkan pada nilai negatif terkecil, dan
    #   nilai lainnya relatif terhadap nilai tersebut
    #   I.S. Masukan: gacha points yang bisajadi mengandung nilai negatif
    #   F.S. Keluaran: gacha points yang pasti positif

    # KAMUS LOKAL
    #   pnts : GachaPoints
    #   low : integer
    #   rarity : string

    # ALGORITMA SUBPROGRAM
    pnts = {}
    low = min(gachaPnts.values())

    for r in gachaPnts:
        pnts[r] = gachaPnts[r]
        if low < 0:
            pnts[r] += abs(low)

    return pnts

# function RollGacha(
#   gachaPnts : GachaPoints,
#   items : CollectionData of ConsumableData
# ) --> GachaRollResult
def RollGacha(gachaPnts, items):
    # Melakukan roll gacha berdasarkan gacha points
    #   I.S. Masukan: gacha points, list consumable
    #   F.S. Keluaran: consumable yang didapatkan

    # KAMUS LOKAL
    #   pnts : GachaPoints
    #   total, high, rand, idx, qty : integer
    #   pool : CollectionData of ConsumableData
    #   item : ConsumableData

    # ALGORITMA SUBPROGRAM
    pnts = NormalizeGachaPoints(gachaPnts)
    total = sum(pnts.values())
    high = max(pnts.values())

    # Roll rarity
    rand = RandomInt(0, high)
    for r in pnts:
        if rand < pnts[r]:
            rarity = r
            break
        rand -= pnts[r]

    # Roll item yg raritynya sesuai
    pool = ListFilter(items, lambda x, i: x['rarity'] == rarity)
    idx = RandomInt(0, len(pool) - 1)
    item = pool[idx]

    # Roll jumlah item
    qty = 1 + RandomInt(0, total / pnts[rarity])

    return { 'item': pool[idx], 'qty': qty }
