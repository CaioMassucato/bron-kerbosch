DOLPHINS = [
]

def list_string_to_int(list):
    temp = []
    for element in list:
        temp.append([int(string_val) for string_val in element])
    return temp
        