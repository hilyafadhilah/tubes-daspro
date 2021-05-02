# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/load
#   Berisi subprogram untuk membaca data dari file dan
#   mengkonversinya menjadi tipe yang bersesuaian

# DEKLARASI SUBPROGRAM
import os.path
from modules.utils import SplitByChar, StringToDate

# function LoadAll(schema : CollectionsSchema, dirname : string) --> CollectionsData
def LoadAll(schema, dirname):
    # Membaca seluruh file CSV dari direktori dirname berdasarkan schema
    #   I.S. Masukan: skema data, nama direktori
    #   F.S. Keluaran: seluruh data yg sudah dikonversi 

    # KAMUS LOKAL
    #   data : CollectionsData
    #   colls : list of string
    #   fname : string

    # ALGORITMA SUBPROGRAM
    data = {}

    for collection in schema:
        fname = os.path.join(dirname, collection + '.csv')
        data[collection] = ConvertLoadedData(schema[collection], LoadCsv(fname))

    return data

# function LoadCsv (filename : string) --> list of dict of string
def LoadCsv(filename):
    # Membaca data dari file CSV berseparator “;”
    #   Mengembalikan hasilnya dalam array berisi dictionary
    #   dengan key nama field dan value nilainya bertipe string.
    #   I.S. Masukan: nama file CSV
    #   F.S. Keluaran: data dari file CSV (masih bertipe string) 

    # KAMUS LOKAL
    #   data : list of dict of string
    #   f : File
    #   table : list of list of string
    #   line : string
    #   row : dict of string

    # ALGORITMA SUBPROGRAM
    data = []

    if os.path.exists(filename):
        table = []

        f = open(filename, 'r')
        for line in f:
            table.append(SplitByChar(line.rstrip(), ';'))
        f.close()

        cols = table[0]

        for i in range(1, len(table)):
            row = {}
            for j in range(len(cols)):
                row[cols[j]] = table[i][j]
            data.append(row)
    
    return data

# function ConvertLoadedData of T (
#   schema : CollectionSchema of T,
#   data : list of dict of string
# ) --> CollectionData of T
def ConvertLoadedData(columnTypes, data):
    # Mengkonversikan data hasil load menjadi tipe sesuai schema-nya.
    #   I.S. Masukan: skema sebuah koleksi, data koleksi tersebut
    #   F.S. Keluaran: data yang telah dikonversi berdasarkan schema 

    # KAMUS LOKAL
    #   result : CollectionData of T
    #   fields : list of string
    #   row : dict of any
    #   typ : DataType
    #   value : string

    # ALGORITMA SUBPROGRAM
    result = []

    for raw in data:
        row = {}
        for col in columnTypes:
            if col not in raw:
                row[col] = None
            else:
                if columnTypes[col] == 'int':
                    row[col] = int(raw[col])
                elif columnTypes[col] == 'float':
                    row[col] = float(raw[col])
                elif columnTypes[col] == 'date':
                    row[col] = StringToDate(raw[col])
                elif type(columnTypes[col]) == list:
                    if raw[col] in columnTypes[col]:
                        row[col] = raw[col]
                    else:
                        row[col] = None
                else:
                    row[col] = raw[col]
        result.append(row)

    return result
