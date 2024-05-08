import sys


import fileinput


c = sys.argv[1]

match c:
    case '--user-provided':
        print("up")
    case '--generate':
        print("g")

    case _:
        print("There is no such option")
        exit(1)


nums = []

files_list = sys.argv[2:]

if(len(files_list)):
    file = fileinput.input(files=files_list)

    with file as f:
        for line in f:
            nums.append(int(line))
    
else:
    nodes = input("nodes>")

    for i in range(int(nodes)):
        nums += [input(f"{i+1}>")]


print(nums)