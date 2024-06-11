
from utils import load_items_from, print_items, brute_force_pack

import math

if __name__ == "__main__":

    items = load_items_from('items.csv', sep=';')

    print_items(items)

    print(brute_force_pack(items, 3))
        

    