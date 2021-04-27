def DisplayHelp():
    access = input("Admin/User : ") #masih belum ada fungsi buat mencari role nya
    print("============= HELP ============")
    if(access == "Admin"):
        print("""
        registrasi - untuk melakukan registrasi baru
        login - untuk melakukan login ke dalam sistem
        cariraritiy - untuk menampilkan gadget berdasarkan rarity
        caritahun - untuk menampilkan gadget berdasarkan kategori tahun
        tambahitem - untuk melakukan penambahan item
        hapusitem - untuk menghapus item dalam database
        ubahjumlah - untuk menambahkan atau membuang sejumlah gadget
        riwayatpinjam - untuk menampilkan sejumlah riwayat peminjaman terbaru
        riwayatkembali - untuk menampilkan sejumlah riwayat pengembalian gadget terbaru
        riwayatambil - untuk menampilkan sejumlah riwajat pengambilan consumable terbaru
        save - menyimpan data ke dalam file setelah dilakukan perubahan
        help - menampilkan panduan penggunaan sistem
        exit - keluar dari aplikasi
        """)
    elif (access == "User"):
        print("""
        login - untuk melakukan login ke dalam sistem
        cariraritiy - untuk menampilkan gadget berdasarkan rarity
        caritahun - untuk menampilkan gadget berdasarkan kategori tahun
        pinjam - untuk melakukan peminjaman gadget yang tersedia
        kembalikan - untuk melakukan pengembalian gadget yang tersedia
        minta - untuk meminta consumable yang tersedia
        save - menyimpan data ke dalam file setelah dilakukan perubahan
        help - menampilkan panduan penggunaan sistem
        exit - keluar dari aplikasi
        """)