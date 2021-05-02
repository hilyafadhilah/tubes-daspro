#ALGORITMA
#hasil data belum diarahkan ke dalam file penyimpanan
def FindByYear():
    tahun = int (input("Masukkan tahun: "))
    kategori= str (input("Masukkan kategori:"))

    print("\n Hasil pencarian \n")

    #Misalkan pencarian tahun sebagai berikut
    #Belum dilakukan pengecekan masing masing file
    if (kategori == "="):#gadget terbit pada tahun
        ListFilter('gadget', match=lambda x: x['tahun_ditemukan']== tahun)
    elif (kategori == ">"):#gadget terbit setelah tahun
        ListFilter('gadget', match=lambda x: x['tahun_ditemukan'] > tahun)
    elif (kategori == "<"):#gadget terbit sebelum tahun
        ListFilter('gadget', match=lambda x: x['tahun_ditemukan'] < tahun)
    elif (kategori == ">="):#gadget terbit setelah pada tahun
        ListFilter('gadget', match=lambda x: x['tahun_ditemukan'] >= tahun)
    elif (kategori == "<="):#gadget terbit sebelum pada tahun
        ListFilter('gadget', match=lambda x: x['tahun_ditemukan'] <= tahun)
    
ShowEachEntry(gadget_by_year,display=FindByYear,pageSize=2)