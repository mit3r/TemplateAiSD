

def load_items_from(file_path: str, sep: str = ';'):
    with open(file_path, 'r') as file:

        items = []
        for line in file.readlines()[1:]:
            if not line.strip():
                continue

            (name, value, weight) = line.strip().split(sep)
            items += [tuple([name.strip(), float(value), float(weight)])]
        return items    
    
def print_items(items: list[tuple[str, float, float]]):

    max_str_len = [
        max([len(item[0]) for item in items]),
        int(max([len(str(item[1])) for item in items])),
        int(max([len(str(item[2])) for item in items]))
    ]

    description = ['Name', 'Value', 'Weight']
    for i, d in enumerate(description):
        max_str_len[i] = max(max_str_len[i], len(d))


    print("  ".join([f'{d:<{l}}' for d, l in zip(description, max_str_len)]))

    for item in items:
        print("  ".join([
            f'{item[0]:<{max_str_len[0]}}', 
            f'{item[1]:>{max_str_len[1]}}',
            f'{item[2]:>{max_str_len[2]}}'
        ]))

def int_to_bool_list(n, length):
    return [n & (1 << i) > 0 for i in range(length)]

def brute_force_pack(items, weightLimit):
    
    max_index = -1
    max_value = 0
    max_weight = 0

    for index in range(1, 2**len(items)):
        # konkretny i-ty wybór przedmiotów

        total_value = 0
        total_weight = 0

        for j, inside in enumerate(int_to_bool_list(index, len(items))):
            if inside:
                total_value += items[j][1]
                total_weight += items[j][2]

        if total_value > max_value and total_weight <= weightLimit:
            max_index = index
            max_value = total_value
            max_weight = total_weight

        print([1 if b else 0 for b in int_to_bool_list(index, len(items))], f"{total_value:.3f}", f"{total_weight:.3f}")
    
    if max_index == -1:
        return []
    
    print(f"{max_weight:.3f}")
    result = []
    for j, inside in enumerate(int_to_bool_list(max_index, len(items))):
        if inside:
            result.append(items[j])

    return result
            

def dynamic_programming_pack(items, max_weight):
    pass