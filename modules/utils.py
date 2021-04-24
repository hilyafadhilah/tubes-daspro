import datetime

def SplitByChar(str, sep):
    result = []
    buf = ''

    for i in range(len(str)):
        if (str[i] == sep):
            result.append(buf)
            buf = ''
        else:
            buf = buf + str[i]
    result.append(buf)

    return result

def StringToDate(string):
    d, m, y = SplitByChar(string, '/')
    return datetime.datetime(int(y), int(m), int(d))

def DateToString(date):
    return date.strftime("%d/%m/%Y")

def ListFindIndex(lst, match, args = []):
    i = 0
    while i < len(lst):
        if match(lst[i], i, *args):
            return i
        i += 1
    return None

def ListFind(lst, match, args = []):
    idx = ListFindIndex(lst, match, args)
    return lst[idx] if idx is not None else None

def ListFilter(lst, match, args = []):
    result = []
    for i in range(len(lst)):
        if match(lst[i], i, *args):
            result.append(lst[i])
    return result
