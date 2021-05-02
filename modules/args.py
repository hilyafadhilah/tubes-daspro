# Nama      : TBIF1210-08-07
# Tanggal   : 2021-05-03

# Module modules/args
# { Modul utility command line argument parsing }

# KAMUS UTAMA
#   _dirname : string  
_dirname = None

# DEKLARASI SUBPROGRAM
import argparse

# procedure ParseArgs ()
def ParseArgs():
    # Melakukan parsing command line arguments
    #   I.S.  variabel _dirname terdefinisi sebagai variabel global
    #   F.S.  variabel _dirname nilainya menjadi sesuai input argumen 

    # KAMUS LOKAL
    #   parser : ArgumentParser

    # ALGORITMA SUBPROGRAM
    global _dirname

    parser = argparse.ArgumentParser(description='Inventarisasi kantong ajaib Doremonangis',)
    parser.add_argument('dirname', help='Path direktori tempat file data disimpan')

    args = parser.parse_args()
    _dirname = args.dirname

# function GetDirname () --> string
def GetDirname():
    # Mengembalikan nilai nama folder hasil input
    #   I.S. variabel _dirname terdefinisi sbg variabel global
    #   F.S. Keluaran: string nilai _dirname 
    # ALGORITMA SUBPROGRAM
    global _dirname
    return _dirname
