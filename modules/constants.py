from routes import history

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
]

collectionsSchema = {
    'user': {
        'id': 'int',
        'username': 'string',
        'nama': 'string',
        'alamat': 'string',
        'password': 'string',
        'role': 'string'
    },
    'gadget': {
        'id': 'string',
        'nama': 'string',
        'deskripsi': 'string',
        'jumlah': 'int',
        'rarity': 'string',
        'tahun_ditemukan': 'int'
    },
    'consumable': {
        'id': 'string',
        'nama': 'string',
        'deskripsi': 'string',
        'jumlah': 'int',
        'rarity': 'string'
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
        'jumlah': 'int'
    },
    'gadget_return_history': {
        'id': 'int',
        'id_peminjam': 'int',
        'id_gadget': 'string',
        'tanggal_pengembalian': 'date'
    }
}
