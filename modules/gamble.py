import time
import math
from modules.gacha_constants import baseGachaPoints, pointsBoost
from modules.utils import ListFilter

def Random():
    m = 2 ** 32
    a = 22695477
    c = 1

    time.sleep(0.001)

    xn = time.time()
    n = int(xn) % 16807

    for i in range(n):
        xn = (a * xn + c) % m
    
    return xn / m

def RandomInt(min, max):
    return min + math.floor(Random() * (max - min))

def InitGachaPoints(items):
    global baseGachaPoints

    avlbl = list(set(map(lambda x: x['rarity'], items)))
    pnts = {}

    for r in baseGachaPoints:
        if r in avlbl:
            pnts[r] = baseGachaPoints[r]

    return pnts

def CalculateItemBoost(gachaPnts, item, qty):
    global pointsBoost

    boost = {}
    ir = item['rarity']

    if ir in pointsBoost:
        for br in pointsBoost[ir]:
            factor = RandomInt(1, qty)
            boost[br] = pointsBoost[ir][br] * factor

    return boost

def AddBoost(gachaPnts, boost):
    pnts = {}

    for br in gachaPnts:
        pnts[br] = gachaPnts[br]
        if br in boost:
            pnts[br] += boost[br]

    return pnts

def NormalizeGachaPoints(gachaPnts):
    pnts = {}
    low = min(gachaPnts.values())

    for r in gachaPnts:
        pnts[r] = gachaPnts[r]
        if low < 0:
            pnts[r] += abs(low)

    return pnts

def RollGacha(gachaPnts, items):
    pnts = NormalizeGachaPoints(gachaPnts)
    total = sum(pnts.values())
    high = max(pnts.values())

    rand = RandomInt(0, high)

    for r in pnts:
        if rand < pnts[r]:
            rarity = r
            break
        rand -= pnts[r]

    pool = ListFilter(items, lambda x, i: x['rarity'] == rarity)
    idx = RandomInt(0, len(pool) - 1)
    item = pool[idx]

    qty = 1 + RandomInt(0, total / pnts[rarity])

    return { 'item': pool[idx], 'qty': qty }
