from modules.utils import ListFind

def MatchRoute(routes, cmd):
    return ListFind(routes, match=lambda r, i, c: r['cmd'] == c, args=[cmd])
