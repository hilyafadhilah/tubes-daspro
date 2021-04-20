import argparse

_dirname = None

def ParseArgs():
    global _dirname

    # @TODO: Add description, help, and error mesesage
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('dirname', help='')

    args = parser.parse_args()
    _dirname = args.dirname

def GetDirname():
    global _dirname
    return _dirname
