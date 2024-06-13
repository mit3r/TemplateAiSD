
from backpack import Backpack

import argparse

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Pack items in a backpack')

    parser.add_argument("file", type=str, help="File with the items to pack")


    parser.add_argument("limit", type=int, help="Max weight of the backpack")
    parser.add_argument("method", type=str, help="Method to pack the backpack",
                        choices=['force', 'dynamic'])

    args = parser.parse_args()

    backpack = Backpack(args.file, sep=';')    
    backpack.pack_and_print_summary(args.limit, args.method)
    
