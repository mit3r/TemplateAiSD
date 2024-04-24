import argparse
from src.inputEnums import insert, remove, action
from AVL.AVLTree import AVL
from BST.BSTree import BST
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
        # tree = AVL(input_data=input(insert))
        tree = AVL(input_data=input(insert))
    elif args.tree_type == 'bst':
        # tree = BST(input_data=input(insert))
        tree = BST(input_data="2,1,5,3,10,14,123")

    else:
        print("Please specify tree type.")
        exit(1)
    print("Tree created. Use 'help' to see available commands.")

    while True:
        command = input(action).lower()
        if command not in commands:
            print("Invalid command.")
            continue
        if command == 'help':
            print("Help \t Show this message\n")
            print("Print \t Print the tree usin In-order, Pre-order, Post-order\n")
            print("Remove \t Remove elements of the tree\n")
            print("Delete \t Delete whole tree\n")
            print("Export \t Export the tree to tickzpicture\n")
            print("Rebalance \t Rebalance the tree\n")
            print("Exit \t Exits the program (same as ctrl+D)\n")

        elif command == 'print':
            tree.print_tree(tree.root)

        elif command == 'remove':
            tree.delete_nodes(input(remove))
            tree.display()

        elif command == 'delete':
            tree.delete_all_tree(tree.root)
            tree.display()

        elif command == 'export':
            tree.export_tree()

        elif command == 'rebalance':
            tree.balance()
            tree.display()

        elif command == 'exit':
            exit(0)
        else:
            print("Invalid command.")
            continue


        