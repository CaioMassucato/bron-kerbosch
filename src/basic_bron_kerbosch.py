from telnetlib import DO
from igraph import *
from utils.utils import *
from counter import Counter

vertices_num = 0
dolphins = []
edges = []
nodes = 0

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
    #make_adj_list(dolphins)

def make_adj_list(list):
    '''Makes adjacency list based on dolphins list'''
    
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

def basic_bron_kerbosch(adj_list, clique, candidates, excluded, reporter):
    '''Bronker Bosch Algorithm without pivoting'''
    
    reporter.inc_count()
    if not candidates and not excluded:
        reporter.record(clique)
        return
 
    for vertice in list(candidates):
        
        new_candidates = candidates.intersection(adj_list[vertice])
        new_excluded = excluded.intersection(adj_list[vertice])
        basic_bron_kerbosch(adj_list, clique + [vertice], new_candidates, new_excluded, reporter)
        candidates.remove(vertice)
        excluded.add(vertice)

def pivoting_bron_kerbosch(adj_list, clique, candidates, excluded, reporter):
    '''Bron–Kerbosch algorithm with pivot'''
    reporter.inc_count()
    if not candidates and not excluded:
        reporter.record(clique)
        return
 
    pivot = pick_random(candidates) or pick_random(excluded)
    for vertice in list(candidates.difference(adj_list[pivot])):
        new_candidates = candidates.intersection(adj_list[vertice])
        new_excluded = excluded.intersection(adj_list[vertice])
        pivoting_bron_kerbosch(adj_list, clique + [vertice], new_candidates, new_excluded, reporter)
        candidates.remove(vertice)
        excluded.add(vertice)

def main():
    global dolphins
    global nodes
    
    graph_data = get_data()
    dolphins = graph_data
    
    adj_dict = make_adj_list(dolphins)
    adj_list = make_adj_list_without_keys(adj_dict)
    nodes = set(range(1, len(adj_list)))
    
    report = Counter('## %s' % basic_bron_kerbosch.__doc__)
    basic_bron_kerbosch(adj_list, [], set(nodes), set(), report)
    report.print_report()
    
    report = Counter('## %s' % pivoting_bron_kerbosch.__doc__)
    pivoting_bron_kerbosch(adj_list, [], set(nodes), set(), report)
    report.print_report()

main()
