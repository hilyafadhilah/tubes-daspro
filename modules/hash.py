# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

def Hashing(msg):
    MsgList = list(msg)
    #Spasi dimasukkan sebagai karakter
    code = "qE1~ YMUR2\"`hNIdPzi%^t@(Ao:=CQ,nx4S[7mHFye#aT6+v)DfKL$r?bkOGB>}!9_wV']jcp5JZ&Xl|\\8sg<{3.u*W-0/"
    pswd = Encrypt(MsgList, code)
    return pswd


def Encrypt(msg, code):
    encrypt = []
    IdxAwal = 0
    IdxAkhir = 0
    
    for i in range (len(msg)):
        FindIdx = 0
        while True:
            if msg[i] == code[FindIdx]:
                NilaiAwal = FindIdx + 1
                break
            else:
                FindIdx += 1
        
        IdxAwal += 1
        IdxAkhir += IdxAwal
        NilaiAkhir = NilaiAwal + IdxAkhir
        hasil = (NilaiAkhir-1)%94
        encrypt.append(code[hasil])
    
    return "".join(encrypt)
