

def list_string_to_int(list):
    temp = []
    for element in list:
        temp.append([int(string_val) for string_val in element])
    return temp

def make_adj_list_without_keys(adj_dict):
    '''Makes adjacency list from an adjacency dictionary'''
    temp = [[]]
    
    for i in range(1, 62):
       temp.append(adj_dict[i])
    return temp

def pick_random(s):
    if s:
        elem = s.pop()
        s.add(elem)
        return elem