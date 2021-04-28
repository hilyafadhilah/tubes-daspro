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
