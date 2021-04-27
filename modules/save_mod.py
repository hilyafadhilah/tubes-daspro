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
    for i in (data.keys()):
        key = []
        file = open(path + "\\" + folder + "\\" + i + ".csv", 'w')
        for j in (data[i][1]).keys():
            key.append(j)
        file.write(';'. join(key))
        file.write('\n')
        for k in (data[i]):
            line = [] 
            for l in (k.values()):
                line.append(str(l))
            file.write(';'. join(line))
            file.write('\n')
        file.close()

