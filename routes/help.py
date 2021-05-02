# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

from modules.store import GetCurrentUser

def DisplayHelp():
    user = GetCurrentUser() #masih belum ada fungsi buat mencari role nya
    if user is not None:
        if user['role'] == "Admin" :
            print("""
  register       - untuk melakukan registrasi baru
  login          - untuk melakukan login ke dalam sistem
  carirarity     - untuk menampilkan gadget berdasarkan rarity
  caritahun      - untuk menampilkan gadget berdasarkan kategori tahun
  tambahitem     - untuk melakukan penambahan item
  hapusitem      - untuk menghapus item dalam database
  ubahjumlah     - untuk menambahkan atau membuang sejumlah gadget
  riwayatpinjam  - untuk menampilkan sejumlah riwayat peminjaman terbaru
  riwayatkembali - untuk menampilkan sejumlah riwayat pengembalian gadget terbaru
  riwayatambil   - untuk menampilkan sejumlah riwajat pengambilan consumable terbaru
  save           - menyimpan data ke dalam file setelah dilakukan perubahan
  help           - menampilkan panduan penggunaan sistem
  exit           - keluar dari aplikasi
            """)
        elif user['role'] == "User":
            print("""
  login      - untuk melakukan login ke dalam sistem
  carirarity - untuk menampilkan gadget berdasarkan rarity
  caritahun  - untuk menampilkan gadget berdasarkan kategori tahun
  pinjam     - untuk melakukan peminjaman gadget yang tersedia
  kembalikan - untuk melakukan pengembalian gadget yang tersedia
  minta      - untuk meminta consumable yang tersedia
  gacha      - untuk meningkatkan rarity consumable
  save       - menyimpan data ke dalam file setelah dilakukan perubahan
  help       - menampilkan panduan penggunaan sistem
  exit       - keluar dari aplikasi
            """)
    else:
        print("""
  login - untuk melakukan login ke dalam sistem
  help  - menampilkan panduan penggunaan sistem
  exit  - keluar dari aplikasi
        """)
