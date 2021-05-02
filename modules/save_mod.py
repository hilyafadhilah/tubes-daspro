# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

import os
from modules.utils import DateToString

def FindFolder(folder, path):
    found = False
    for dirpath, dirnames, filenames in os.walk(path):
        for i in (dirnames):
            if(i == folder):
                found = True
    return found

def MakeFolder(folder, path):
    os.makedirs(path + "\\" + folder)

def RemakeFile(data, folder, path, schema):
    copy = DateToStringCsv(CopyData(data))
    for name in copy:
        file = open(os.path.join(path, folder, name) + ".csv", 'w')
        fields = schema[name].keys()
        file.write(';'.join(fields))
        file.write('\n')
        for row in copy[name]:
            line = list(map(lambda f: str(row[f]), fields))
            file.write(';'. join(line))
            file.write('\n')
        file.close()

def CopyData(data):
    copy = {}
    for name in data:
        copy[name] = []
        for row in data[name]:
            rowCopy = {}
            for col in row:
                rowCopy[col] = row[col]
            copy[name].append(rowCopy)
    return copy

def DateToStringCsv(data):
    SchemaWithDate= ["consumable_history", "gadget_borrow_history", "gadget_return_history"]
    for schema in SchemaWithDate:
        if schema == "consumable_history":
            atribut = "tanggal_pengambilan"
        elif schema == "gadget_borrow_history":
            atribut = "tanggal_peminjaman"
        elif schema == "gadget_return_history":
            atribut = "tanggal_pengembalian"

        for i in range(len(data[schema])):
            data[schema][i][atribut] = DateToString(data[schema][i][atribut])
    
    return data
