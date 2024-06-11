
from backpack import Backpack

if __name__ == "__main__":

    backpack = Backpack('items.csv', sep=';')
    backpack.pack_and_print_summary(3, "force")
        
    
    