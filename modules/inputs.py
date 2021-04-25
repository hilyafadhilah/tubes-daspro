from modules.utils import StringToDate

def Confirm(msg):
    value = input(msg + ' (Y/N): ')
    return value in 'Yy'

def PromptLoop(msg, until, err = 'Invalid.', bag = False):
    while True:
        inp = input(msg)

        if bag is True:
            valid, bg = until(inp)
        else:
            valid = bg = until(inp)

        if valid is True:
            break

        if callable(err):
            err(inp, bg)
        else:
            print(err)

    if bag is True:
        return inp, bg
    else:
        return inp

def InputDate(name):
    _, value = PromptLoop(
        msg=f'Tanggal {name}: ',
        until=ValidateDate,
        err='Tanggal tidak valid! Format: DD/MM/YYYY',
        bag=True
    )

    return value

def InputQty(name, min, max):
    def ErrMsg(value, bag):
        if bag is None:
            print('Bukan angka yang valid!')
        elif bag == 1:
            print('Terlalu banyak!')
        elif bag == -1:
            print('Terlalu sedikit!')

    _, value = PromptLoop(
        msg=f'Jumlah {name}: ',
        until=GetNumericValidator(min, max),
        err=ErrMsg,
        bag=True
    )

    return value

# Validation

def ValidateDate(inp):
    try:
        value = StringToDate(inp)
        return True, value
    except ValueError:
        return False, None

def GetNumericValidator(min = None, max = None):
    def Validator(inp):
        try:
            value = int(inp)
            if min is not None and value < min:
                return False, -1
            elif max is not None and value > max:
                return False, 1
        except ValueError:
            return False, None
        return True, value
    
    return Validator
