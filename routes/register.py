#ALGORITMA
def register():
    nama= str(input("Masukkan nama: "))
    username= str(input("Masukkan username: "))
    password= str(input("Masukkan password: "))
    alamat= str(input("Masukkan alamat: "))
#Akan dilakukan pengecekan username sehingga tidak terjadi
# Duplikasi.
# Bila benar dilakukan pengisian data ke 'user.csv' .
if (len(FindBy('user', {'username':Username})==0)):
    InsertOne('user', {'nama':nama, 
    'username': username,
    'password': password, 
    'alamat': alamat,
    'role': 'User'
    },autoId=True)