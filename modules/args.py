import argparse

_dirname = None

def ParseArgs():
    global _dirname

    parser = argparse.ArgumentParser(description='Inventarisasi kantong ajaib Doremonangis',)
    parser.add_argument('dirname', help='Path direktori tempat file data disimpan')

    args = parser.parse_args()
    _dirname = args.dirname

def GetDirname():
    global _dirname
    return _dirname
