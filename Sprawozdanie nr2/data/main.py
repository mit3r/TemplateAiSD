import argparse
from inputEnums import nodes, insert, action
from AVL import AVL
from BST import BST
import gc

if not gc.isenabled():
    gc.enable()

commands = ("help", 'print', 'remove', 'delete', 'export', 'rebalance', 'exit')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Demonstration of AVL and BST trees.")
    parser.add_argument("--AVL", action="store_const", const="avl", dest="tree_type", help="Use AVLTree")
    parser.add_argument("--BST", action="store_const", const="bst", dest="tree_type", help="Use BSTTree")
    args = parser.parse_args()
    print(args)
    if args.tree_type == 'avl':
        tree = AVL(input_data=input(insert))
    elif args.tree_type == 'bst':
        tree = BST(input_data=input(insert))

    else:
        print("Please specify tree type.")
        exit(1)