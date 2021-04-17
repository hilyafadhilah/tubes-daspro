import argparse

def ParseArgs():
    # @TODO: Add description, help, and error mesesage
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('dirname', help='')
    return parser.parse_args()
