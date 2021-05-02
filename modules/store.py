from modules.utils import ListFind, ListFindIndex, ListFilter

_data = {}
_user = None

def InitStore(data):
    global _data
    _data = data

def GetCollection(name):
    global _data
    return _data[name] if name in _data else None

def FindOne(collection, entryId):
    global _data
    return ListFind(_data[collection], match=lambda x, i, d: x['id'] == d, args=[entryId])

def FindBy(collection, criteria):
    global _data

    def IsMatch(entry, idx):
        for col in criteria:
            if entry[col] != criteria[col]:
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

def DeleteOne(collection, entryId):
    global _data

    index = ListFindIndex(_data[collection], match=lambda x, i, d: x['id'] == d, args=[entryId])

    if index is not None:
        return _data[collection].pop(index)

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

def TakeData():
    global _data
    return _data

def SetCurrentUser(user):
    global _user
    _user = user

def GetCurrentUser():
    global _user
    return _user
