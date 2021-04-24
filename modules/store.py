from modules.utils import ListFind, ListFindIndex, ListFilter

_data = {}

def InitStore(data):
    global _data
    _data = data

def GetCollection(name):
    global _data
    return _data[name]

def FindOne(collection, entryId):
    global _data
    return ListFind(_data[collection], match=lambda x, i, d: x['id'] == d, args=[entryId])

def FindBy(collection, match):
    global _data

    def IsMatch(entry, idx):
        for col in match:
            if entry[col] != match[col]:
                return False
        return True

    return ListFilter(_data[collection], match=IsMatch)

def UpdateOne(collection, entryId, value):
    global _data

    index = ListFindIndex(_data[collection], match=lambda x, i, d: x['id'] == d, args=[entryId])

    if index is not None:
        _data[collection][index].update(value)
        return _data[collection][index]

    return None

def InsertOne(collection, value, autoId = False):
    global _data

    if autoId:
        value['id'] = NextInsertId(collection)

    _data[collection].append(value)
    return value['id']

def NextInsertId(collection):
    global _data
    return max(_data[collection], key=lambda x: x['id'])['id'] + 1
