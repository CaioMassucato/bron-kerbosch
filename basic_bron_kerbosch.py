from telnetlib import DO
from igraph import *
from utils import DOLPHINS, list_string_to_int

vertex_num = 0

def get_data():
    '''Get data from dolphins.txt file and appends it to a list'''
    
    # Opens file and read lines
    file = open("dolphins.txt", "r")
    lines = file.readlines()
    
    # Append each line as a list element
    temp_list = []
    for line in lines:
        temp_line = line[0:].strip().split(" ")
        temp_list.append(temp_line)
    
    DOLPHINS = list_string_to_int(temp_list)
    vertex_num = DOLPHINS[0][0]
    DOLPHINS.pop(0)
    make_adj_list(DOLPHINS)

def make_adj_list(list):
    '''Makes adjacency list based on DOLPHINS list'''
    
    adj_list = dict()
    # For each pair in DOLPHINS list
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
    print(adj_list)
                
                
        

get_data()
