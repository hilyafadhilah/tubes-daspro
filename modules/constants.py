from routes import history, return_gadget, borrow_gadget, change_stock, consume save, exit, help

routes = [
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
    }
]

collectionsSchema = {
    'user': {
        'id': 'int',
        'username': 'string',
        'nama': 'string',
        'alamat': 'string',
        'password': 'string',
        'role': ['Admin', 'User']
    },
    'gadget': {
        'id': 'string',
        'nama': 'string',
        'deskripsi': 'string',
        'jumlah': 'int',
        'rarity': ['C', 'B', 'A', 'S'],
        'tahun_ditemukan': 'int'
    },
    'consumable': {
        'id': 'string',
        'nama': 'string',
        'deskripsi': 'string',
        'jumlah': 'int',
        'rarity': ['C', 'B', 'A', 'S']
    },
    'consumable_history': {
        'id': 'int',
        'id_pengambil': 'int',
        'id_consumable': 'string',
        'tanggal_pengambilan': 'date',
        'jumlah': 'int'
    },
    'gadget_borrow_history': {
        'id': 'int',
        'id_peminjam': 'int',
        'id_gadget': 'string',
        'tanggal_peminjaman': 'date',
        'jumlah': 'int',
        'is_returned': {
            'T': True,
            'F': False
        }
    },
    'gadget_return_history': {
        'id': 'int',
        'id_peminjaman': 'int',
        'tanggal_pengembalian': 'date',
        'jumlah': 'int'
    }
}
