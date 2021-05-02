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
        'is_returned': ['T', 'F']
    },
    'gadget_return_history': {
        'id': 'int',
        'id_peminjaman': 'int',
        'tanggal_pengembalian': 'date',
        'jumlah': 'int'
    }
}

# GACHA

baseGachaPoints = {
    'C': 80,
    'B': 50,
    'A': 25,
    'S': 10
}

pointsBoost = {
    'C': {
        'C': 0,
        'B': 1,
        'A': 0,
        'S': 0
    },
    'B': {
        'C': -1,
        'B': 0,
        'A': 1,
        'S': 0
    },
    'A': {
        'C': -2,
        'B': -1,
        'A': 0,
        'S': 1
    },
    'S': {
        'C': -3,
        'B': -2,
        'A': 0,
        'S': 2
    },
}
