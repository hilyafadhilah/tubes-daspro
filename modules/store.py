# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/args
# { Modul manajemen data }

# KAMUS UTAMA

# type CollectionData of T : <
#   Name : string;
#   Data : list of T
# >
# type CollectionsData : list of CollectionData of EntryData

#   _data : CollectionsData
#   _user : UserData

# DEKLARASI SUBPROGRAM
from modules.utils import ListFind, ListFindIndex, ListFilter

_data = {}
_user = None

# procedure InitStore (data : CollectionsData)
def InitStore(data):
# Mengisi nilai data ke dalam store
#   I.S. Variabel global _data terdefinisi
#   F.S. Variabel _data diubah nilainya sesuai masukan 

# ALGORITMA SUBPROGRAM
    global _data
    _data = data

# function GetCollection (name : string) --> CollectionData | null
def GetCollection(name):
# Mengambil collection / kumpulan data tertentu dari store
#   I.S. Variabel global _data terdefinisi
#        Masukan: nama collection
#   F.S. Keluaran: data dari collection tersebut 

# ALGORITMA SUBPROGRAM
    return _data[name][:] if name in _data else None

# function FindOne (collection : string, id : int | string) --> EntryData | None
def FindOne(collection, entryId):
# Mencari satu entri dari collection dengan ID tertentu
#   I.S. Variabel global _data terdefinisi
#        Masukan: nama collection, ID data yg dicari
#   F.S. Keluaran: entry data yg dicari atau null 

# ALGORITMA SUBPROGRAM
    return ListFind(_data[collection][:], match=lambda x, i: x['id'] == entryId)

# function FindBy (collection : string, criteria : dict of any) --> list of EntryData
def FindBy(collection, criteria):
# Mencari kumpulan entri dari collection yang memenuhi kriteria
#   I.S. Variabel global _data terdefinisi
#        Masukan: nama collection, kriteria pencarian
#   F.S. Keluaran: list entry yg memenuhi kriteria 

# KAMUS LOKAL
#   IsMatch : (entry : EntryData, idx : int) --> bool
#   { Mencocokkan data berdasarkan kriteria FindBy }

# ALGORITMA SUBPROGRAM
    # function IsMatch (entry : EntryData, idx : int) --> bool
    def IsMatch(entry, idx):
        # Mencocokkan data berdasarkan kriteria FindBy
        #   I.S. Variabel criteria diasumsikan terdefinisi
        #        Masukan: entry data, index entry dalam list
        #   F.S. Keluaran: boolean apakah entry memenuhi kriteria 

        # ALGORITMA SUBPROGRAM
        for col in criteria:
            if entry[col] != criteria[col]:
                return False
        return True

    return ListFilter(_data[collection][:], match=IsMatch)

# function UpdateOne (
#   collection : string,
#   entryId : integer | string,
#   value : dict of any
# ) --> EntryData | None
def UpdateOne(collection, entryId, value):
    # Mengubah data pada suatu entri dengan ID tertentu pada collection
    #   I.S. Variabel global _data terdefinisi
    #        Masukan: nama collection, ID entry, perubahan data
    #   F.S. Keluaran: data entry tersebut 

    # KAMUS LOKAL
    #   idx : integer

    # ALGORITMA SUBPROGRAM
    global _data

    index = ListFindIndex(_data[collection], match=lambda x, i: x['id'] == entryId)

    if index is not None:
        _data[collection][index].update(value)
        return _data[collection][index]

    return None

# function DeleteOne (
#   collection : string,
#   entryId : integer | string
# ) --> EntryData | None
def DeleteOne(collection, entryId):
    # Menghapus data pada suatu entri dengan ID tertentu pada collection
    #   I.S. Variabel global _data terdefinisi
    #        Masukan: nama collection, ID entry
    #   F.S. Keluaran: data entry yg baru dihapus, null jika tidak ditemukan 

    # KAMUS LOKAL
    #   idx : integer
    #   value : EntryData

    # ALGORITMA SUBPROGRAM
    global _data

    index = ListFindIndex(_data[collection], match=lambda x, i: x['id'] == entryId)

    if index is not None:
        return _data[collection].pop(index)

    return None

# function InsertOne (
#   collection : string,
#   output value : EntryData,
#   autoId : bool = False
# ) --> int | string
def InsertOne(collection, value, autoId = False):
    # Menambahkan entri pada collection tertentu
    #   Apabila autoId diaktifkan, akan men-generate ID integer secara otomatis
    #   dan meng-override nilai ID pada value
    #   Mengembalikan nilai ID dari entri yang baru ditambahkan
    #   I.S. Variabel global _data terdefinisi
    #       Masukan: nama collection, entry yg ditambahkan, pilihan autoId
    #   F.S. Keluaran: ID entry yang baru saja ditambahkan 

    # ALGORITMA SUBPROGRAM
    global _data

    if autoId:
        value['id'] = NextInsertId(collection)

    _data[collection].append(value)
    return value['id']

# function NextInsertId (collection : string) --> int
def NextInsertId(collection):
    # Mengkalkulasi nilai ID bertipe integer yang belum ada di dalam collection
    #   I.S. Variabel global _data terdefinisi
    #        Masukan: nama collection
    #   F.S. Keluaran: ID integer yg belum ada di collection 
    # ALGORITMA SUBPROGRAM
    return max(_data[collection], key=lambda x: x['id'])['id'] + 1

def TakeData():
    return _data

def SetCurrentUser(user):
    global _user
    _user = user

def GetCurrentUser():
    return _user
