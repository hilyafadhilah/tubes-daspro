import os.path
from modules.utils import SplitByChar, StringToDate

def LoadAll(schema, dirname):
    data = {}

    for collection in schema:
        fname = os.path.join(dirname, collection + '.csv')
        data[collection] = ConvertLoadedData(schema[collection], LoadCsv(fname))

    return data

def LoadCsv(filename):
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

def ConvertLoadedData(columnTypes, data):
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
