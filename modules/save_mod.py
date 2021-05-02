import os

def FindFolder(folder, path):
    found = False
    for dirpath, dirnames, filenames in os.walk(path):
        for i in (dirnames):
            if(i == folder):
                found = True
    return found

def MakeFolder(folder, path):
    os.makedirs(path + "\\" + folder)

def RemakeFile(data, folder, path):
    data = DateToStringCsv(data)
    for name in (data):
        file = open(os.path.join(path, folder, name) + ".csv", 'w')
        fields = collectionsSchema[name].keys()
        file.write(';'.join(fields))
        file.write('\n')
        for row in data[name]:
            line = list(map(lambda f: str(row[f]), fields))
        file.write(';'. join(line))
        file.write('\n')
        file.close()
        
def DateToStringCsv(data):
    SchemaWithDate= ["consumable_history", "gadget_borrow_history", "gadget_return_history"]
    for schema in SchemaWithDate:
        if schema == "consumable_history":
            atribut = "tanggal_pengambilan"
        elif schema == "gadget_borrow_history":
            atribut = "tanggal_peminjaman"
        elif schema == "gadget_return_history":
            atribut = "tanggal_pengembalian"
        
        for DataWithDate in data[schema]:
            data[schema][DataWithDate['id']][atribut] = DateToString(DataWithDate[atribut])
    
    return data
