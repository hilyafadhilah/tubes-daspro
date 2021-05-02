from modules.store import FindBy, SetCurrentUser, InsertOne
from modules.hash import hashing

# ALGORITMA
# Fungsi belum membuka menu utama
def LoginRoute():
    uname = input("Masukkan username: ")
    passwd = input("Masukkan password: ") 

    user = FindBy('user', { 'username': uname, 'password': hashing(passwd) })

    # Bila Benar
    if len(user) > 0:
        #file penyimpanan username dipanggil untuk membandingkan username
        print("Halo "+str(uname)+"! Selamat datang di kantong Ajaib.")
        SetCurrentUser(user[0])
    else:
        #Bila Username dan Password tidak benar
        print("Gagal login.")

#ALGORITMA
def RegisterRoute():
    nama= input("Masukkan nama: ")
    username= input("Masukkan username: ")
    password= input("Masukkan password: ")
    alamat= input("Masukkan alamat: ")

    #Akan dilakukan pengecekan username sehingga tidak terjadi
    # Duplikasi.
    # Bila benar dilakukan pengisian data ke 'user.csv' .
    if (len(FindBy('user', {'username':username}))==0):
        InsertOne('user', {'nama':nama, 
        'username': username,
        'password': password, 
        'alamat': alamat,
        'role': 'User'
        },autoId=True)
        print(f"User {username} telah berhasil didaftarkan ke Kantong Ajaib.")
