# my_list = [3,6,8,9,3,11]
my_list = ["a"]
def find_min(element):
    """TODO: complete for Step 1"""
    for i in element:
        if not isinstance(i, int) :
            return -1
        elif len(element) == 1: 
            return element[0] 
        else: 
            tot_v = find_min(element[1:]) 
            min_n = element[0] 
            if tot_v < min_n: 
                min_n = tot_v 
            return min_n

    return -1

print(find_min(my_list))
print()

my_list_2 = [1,2,3,4,5]
def sum_all(element):
    """TODO: complete for Step 2"""
    for i in element:
        if not isinstance(i, int):
            return -1
        elif len(element) == 1:
            return element[0]
        else:
            return element[0] + sum_all(element[1:])

    return -1

print(sum_all(my_list_2))
print()

def find_possible_strings(character_set, n):
    prefix = ""
    set_list = []
    if character_set == [] :
        return []
    else:
        for i in range(len(character_set)):
            if not isinstance(character_set[i], str):
                return set_list
    
    set_list = possible_strings(character_set, prefix, set_list, n) #call function ""=leaves the prefix empty to take in values
    return set_list

def possible_strings(character_set, prefix, set_list, n):
    if n == 0:
        set_list.append(prefix)
    else:
        for i in range(len(character_set)):
            nPrefix = prefix + character_set[i] #add characters to new prefix
            possible_strings(character_set, nPrefix, set_list, n-1)
            
    return set_list
    

print(find_possible_strings(['x', 'y'], 3))

