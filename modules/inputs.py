from modules.utils import StringToDate

def Confirm(msg):
    while True:
        value = input(msg + ' (Y/N): ')
        if (value in ['Y', 'y']) or (value in ['N', 'n']):
            break
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

def InputDate(prompt):
    _, value = PromptLoop(
        msg=prompt,
        until=ValidateDate,
        err='Tanggal tidak valid! Format: DD/MM/YYYY',
        bag=True
    )

    return value

def InputInt(prompt, min, max):
    def ErrMsg(value, bag):
        if bag is None:
            print('Bukan angka yang valid!')
        else:
            print(f'Angka harus di antara {min} - {max}.')

    _, value = PromptLoop(
        msg=prompt,
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
