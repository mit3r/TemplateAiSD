from math import log10
from typing import Union, Literal

Item = tuple[str, int, int]
Method = Union[Literal["force"], Literal["dynamic"]]

def int_to_bool_list(n, length):
    return [n & (1 << i) > 0 for i in range(length)]

class Backpack():

    def __init__(self, file_path: str, sep: str = ';'):
        self.items: Item = []
        with open(file_path, 'r') as file:
            for line in file.readlines()[1:]:
                if not line.strip():
                    continue

                (name, value, weight) = line.strip().split(sep)
                self.items += [tuple([name.strip(), int(value), int(weight)])] 

    def pack_by_brute_force(self, weightLimit: int) -> list[Item]:
        max_index = -1
        max_value = 0

        for index in range(1, 2**len(self.items)):
            total_value = 0
            total_weight = 0

            for j, inside in enumerate(int_to_bool_list(index, len(self.items))):
                if inside:
                    total_value += self.items[j][1]
                    total_weight += self.items[j][2]

            if total_value > max_value and total_weight <= weightLimit:
                max_index = index
                max_value = total_value
        
        if max_index == -1:
            return []
        
        result = []
        for j, inside in enumerate(int_to_bool_list(max_index, len(self.items))):
            if inside:
                result.append(self.items[j])

        return result  

    def pack_by_dynamic_algorithm(self, weightLimit: int):
        matrix = []
        for i in range(len(self.items)+1):
            matrix += [[0 for _ in range(weightLimit+1)]]

        def V(i: int, j: int):
            if i == 0 or j == 0:
                matrix[i][j] = 0
                return 0
                
            vi = self.items[i-1][1]
            wi = self.items[i-1][2]

            if wi > j:
                matrix[i][j] = V(i-1, j)
            else:
                matrix[i][j] = max(V(i-1, j), V(i-1, j - wi) + vi)
            
            return matrix[i][j]
            
        i = len(self.items)+1
        j = weightLimit
        V(i, j)

        # find items
        result = []
        while (i := i - 1):
            if matrix[i][j] != matrix[i-1][j]:
                result.append(self.items[i-1])
                j -= self.items[i-1][2]

        return result
    
    @staticmethod
    def print_items(items: list[Item]):

        max_col_len = [
            max(*[len(item[0]) for item in items], len('Name')),
            max(*[len(str(item[1])) for item in items], len('Value')),
            max(*[len(str(item[2])) for item in items], len('Weight'))
        ]

        strings = ['Name', 'Value', 'Weight']
        print("  ".join([f'{d:<{l}}' for d, l in zip(strings, max_col_len)]))

        for item in items:
            print("  ".join([
                f'{item[0]:<{max_col_len[0]}}', 
                f'{item[1]:>{max_col_len[1]}}',
                f'{item[2]:>{max_col_len[2]}}'
            ]))

    @staticmethod
    def print_summary(items: list[Item]):

        total_value = sum([i[1] for i in items])
        total_weight = sum([i[2] for i in items])

        max_col_len = [
            max(*[len(item[0]) for item in items], len('Name')),
            max(*[len(str(item[1])) for item in items], int(log10(total_value)) + 1, len('Value')),
            max(*[len(str(item[2])) for item in items], int(log10(total_weight)) + 1, len('Weight'))
        ]

        strings = ["Total", total_value, total_weight]
        print("  ".join([f'{d:>{l}}' for d, l in zip(strings, max_col_len)]))
    
    def pack_and_print_summary(self,  weightLimit: int, method: Method = "force"):

        res: list[Item] = []
        match method:
            case "force":
                res = self.pack_by_brute_force(weightLimit);
            case "dynamic":
                res = self.pack_by_dynamic_algorithm(weightLimit);
            case _:
                raise ValueError("Invalid method");
            
        print("Backpack content:")
        self.print_items(res)
        self.print_summary(res)
        
    