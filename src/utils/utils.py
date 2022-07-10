

from mimetypes import common_types
from unittest import skip


def list_string_to_int(list):
    temp = []
    for element in list:
        temp.append([int(string_val) for string_val in element])
    return temp

def make_adj_list_without_keys(adj_dict):
    '''Makes adjacency list from an adjacency dictionary'''
    temp = [[]]
    
    for i in range(1, 63):
       temp.append(adj_dict[i])
    return temp

def pick_random(s):
    if s:
        elem = s.pop()
        s.add(elem)
        return elem
    
def make_adj_list(list):
    '''Makes adjacency dictionary based on dolphins list'''
    
    adj_list = dict()
    # For each pair in dolphins list
    for vertice_pair in list:
        
        # Get all adjacents for the first element in each pair
        for index in range(1):
            if(vertice_pair[index] not in adj_list):
                adj_list[vertice_pair[index]] = [vertice_pair[index+1]]
            else:
                adj_list[vertice_pair[index]].append([vertice_pair[index+1]].pop())
                
        # Get all adjacents for the second element in each pair      
        for index in range(1):
            if(vertice_pair[index+1] not in adj_list):
                adj_list[vertice_pair[index+1]] = [vertice_pair[index]]
            else:
                adj_list[vertice_pair[index+1]].append([vertice_pair[index]].pop())
                
    return adj_list


def get_data():
    '''Get data from dolphins.txt file and appends it to a list'''
    
    global edges
    global vertices_num
    
    # Opens file and read lines
    file = open("../dolphins.txt", "r")
    lines = file.readlines()
    
    # Append each line as a list element
    temp_list = []
    for line in lines:
        temp_line = line[0:].strip().split(" ")
        temp_list.append(temp_line)
    
    dolphins = list_string_to_int(temp_list)
    vertices_num = dolphins[0][0]
    dolphins.pop(0)
    edges = dolphins
    return dolphins

def clustering_coeff(adj_list):
    '''Calculates Local and Global Clusttering Coefficients'''
    
    # Local Clusttering Coefficient can be calculated as follow:
    # number of pairs of V's neighboors who are neighboors
    # Divided by the number of pairs of V's neighboors
    # Global Clusttering is the Avrg of the local clusttering
    
    local_clusttering = {}
    
    # For each adjacency list of each vertice
    for vertice, neighboors in enumerate(adj_list):
        if(vertice == 0):
            continue
        # Degree of the vertice (V's neighboors)
        degree = len(neighboors)
        
        # Number of pairs of the vertice's neighboors
        pairs_of_neighbooors = (degree*(degree-1))/2
        
        # Number of pairs of V's neighboors who are neighboors
        #aqui vou ter que achar todos os amigos de V que sao amigos
        common_friends = 0
        for friend in neighboors:
            for element in adj_list[friend]:
                if element in neighboors:
                    common_friends+=1
        
        # If there are no common friends
        if(common_friends == 0):
            local_clusttering[vertice] = 0
            continue
        
        # Local Clusttering formula
        local_clusttering[vertice] = pairs_of_neighbooors/common_friends
    
    # Global Clusttering is the Avrg of the local clustterings
    global_clusttering = sum(local_clusttering)/len(local_clusttering)
    
    return global_clusttering