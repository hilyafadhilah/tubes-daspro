# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/constants
# Berisi konstanta general program

# KAMUS UTAMA

# TIPE DATA
#   Tipe dari baris-baris di database

# type UserData : <
#   username : string;
#   nama : string;
#   alamat : string;
#   password : string;
#   role : “Admin” | “User”
# >

# type GadgetData : <
#   id : string;
#   nama : string;
#   deskripsi : string;
#   jumlah : integer;
#   rarity : ‘C’ | ‘B’ | ‘A’ | ‘S’;
#   tahun_ditemukan : integer
# >

# type ConsumableData : <
#   id : string;
#   nama : string;
#   deskripsi : string;
#   jumlah : integer;
#   rarity : ‘C’ | ‘B’ | ‘A’ | ‘S’
# >

# type ConsumableHistoryData : <
#   id : integer;
#   id_pengambil : integer;
#   id_consumable : string;
#   tanggal_pengambilan : Datetime;
#   jumlah : integer
# >

# type BorrowHistoryData : <
#   id : integer;
#   id_peminjam : integer;
#   id_gadget : string;
#   tanggal_peminjaman : Datetime;
#   jumlah : integer;
#   is_returned : integer
# >

# type ReturnHistoryData : <
#   id : integer;
#   id_peminjaman : integer;
#   tanggal_pengembalian : Datetime;
#   jumlah : integer
# >

# type EntryData :
#   UserData | GadgetData | ConsumableData |
#   ConsumableHistoryData | BorrowHistoryData | ReturnHistoryData

# SKEMA DATA
#   Pemetaan nama tabel dan tipe kolom database

# type DataType : “string” | “int” | list of string
# type FieldType : < FieldName : string; FieldType : DataType >
# type CollectionsSchema : list of <
#   CollectionName : string;
#   Schema : list of FieldType
# >

# constant collectionsSchema : CollectionsSchema

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

# type GachaPoints : dict of integer
# constant baseGachaPoints : GachaPoints
#   Poin awal dari gacha

baseGachaPoints = {
    'C': 80,
    'B': 50,
    'A': 25,
    'S': 10
}

# type GachaPointsBoost : dict of GachaPoints
# constant pointsBoost : GachaPointsBoost
#   Tambahan poin dari item terhadap poin gacha
#   Key : Rarity item, Value : Tambahan poin untuk tiap point rarity

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
