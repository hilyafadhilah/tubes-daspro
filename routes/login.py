#ALGORITMA
#Fungsi belum membuka menu utama
def login():
    print("Masukan username: ")
    isUsername= str(input())
    isPassword= str(input())   
    FindBy('username',{'username': isUsername})
    FindBy('password',{'password': isPassword})
    #Bila Benar
    if (isUsername == username) and (password == isPassword):    #file penyimpanan username dipanggil untuk membandingkan username
        print("Halo "+str(isUsername)+"! Selamat datang di kantong Ajaib.")
    else:                                                           #Bila Username dan Password tidak benar
        print("")

login()