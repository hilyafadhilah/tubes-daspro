# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module routes/routes
#   Berisi konstanta routesMapping untuk kebutuhan mapping command ke rute

# KAMUS UTAMA
from routes import user, cari, manage_item, history, return_gadget, borrow_gadget, change_stock, consume, save, exit, help, gacha

# type RouteMapping : <
#   cmd : string;
#   func : Callable;
#   roles : array [1..2] of “Admin” | “User”
# >

# constant routesMapping : list of RouteMapping 

routesMapping = [
    {
        'cmd': 'register',
        'func': user.RegisterRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'login',
        'func': user.LoginRoute,
        'roles': []
    },
    {
        'cmd': 'carirarity',
        'func': cari.CariRarityRoute,
        'roles': ['Admin', 'User']
    },
    {
        'cmd': 'caritahun',
        'func': cari.CariTahunRoute,
        'roles': ['Admin', 'User']
    },
    {
        'cmd': 'tambahitem',
        'func': manage_item.TambahItemRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'hapusitem',
        'func': manage_item.HapusItemRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'riwayatambil',
        'func': history.ConsumableHistoryRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'riwayatpinjam',
        'func': history.BorrowHistoryRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'riwayatkembali',
        'func': history.ReturnHistoryRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'pinjam',
        'func': borrow_gadget.BorrowGadgetRoute,
        'roles': ['User']
    },
    {
        'cmd': 'kembali',
        'func': return_gadget.ReturnGadgetRoute,
        'roles': ['User']
    },
    {
        'cmd': 'minta',
        'func': consume.RequestConsumableRoute,
        'roles': ['User']
    },
    {
        'cmd': 'ubahjumlah',
        'func': change_stock.ChangeStockRoute,
        'roles': ['Admin']
    },
    {
        'cmd' : 'save',
        'func' : save.SaveRoute,
        'roles' : ['Admin', 'User']
    },
    {
        'cmd' : 'help',
        'func' : help.DisplayHelp,
        'roles' : []
    },
    {
        'cmd': 'exit',
        'func': exit.ExitRoute,
        'roles': []
    },
    {
        'cmd': 'gacha',
        'func': gacha.GachaRoute,
        'roles': ['User']
    }
]
