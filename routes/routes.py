from routes import user, cari, manage_item, history, return_gadget, borrow_gadget, change_stock, consume, save, exit, help, gacha

routes = [
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
        'roles' : ['Admin', 'User']
    },
    {
        'cmd': 'exit',
        'func': exit.ExitRoute,
        'roles': ['Admin']
    },
    {
        'cmd': 'gacha',
        'func': gacha.GachaRoute,
        'roles': ['User']
    }
]
