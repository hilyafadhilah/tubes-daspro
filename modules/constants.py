from routes import history, borrow_gadget, return_gadget

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
