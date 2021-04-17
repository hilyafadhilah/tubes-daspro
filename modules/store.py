_data = {}

def InitStore(data):
    global _data
    _data = data

def GetCollection(name):
    global _data
    return _data[name]

def FindOne(collection, entryId):
    global _data

    for entry in _data[collection]:
        if entry['id'] == entryId:
            return entry
    return None

def FindOneIndex(collection, entryId):
    global _data

    i = 0
    while i < len(_data[collection]):
        if _data[collection][i]['id'] == entryId:
            return i
    return None

def UpdateOne(collection, entryId, value):
    global _data

    index = FindOneIndex(collection, entryId)

    if index != None:
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
