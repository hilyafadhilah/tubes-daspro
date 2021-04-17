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
