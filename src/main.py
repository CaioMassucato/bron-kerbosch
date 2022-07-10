from utils.utils import *
from counter import Counter

vertices_num = 0
dolphins = []
edges = []
nodes = 0

def basic_bron_kerbosch(adj_list, clique, candidates, excluded, counter):
    '''Bronker Bosch Algorithm without pivoting'''
    
    # Countes the number of iterations and appends clique to list
    counter.calls_count()
    if not candidates and not excluded:
        counter.save_clique(clique)
        return
 
    # Recursively removes vertices from candidates and adds to excluded
    for vertice in list(candidates):
        
        new_candidates = candidates.intersection(adj_list[vertice])
        new_excluded = excluded.intersection(adj_list[vertice])
        basic_bron_kerbosch(adj_list, clique + [vertice], new_candidates, new_excluded, counter)
        candidates.remove(vertice)
        excluded.add(vertice)

def pivoting_bron_kerbosch(adj_list, clique, candidates, excluded, counter):
    '''Bron–Kerbosch algorithm with pivoting'''
    
    # Countes the number of iterations and appends clique to list
    counter.calls_count()
    if not candidates and not excluded:
        counter.save_clique(clique)
        return
 
    # Picks the pivot from candidates or excluded
    pivot = pick_random(candidates) or pick_random(excluded)
    
    # Recursively removes vertices from candidates and adds to excluded
    for vertice in list(candidates.difference(adj_list[pivot])):
        new_candidates = candidates.intersection(adj_list[vertice])
        new_excluded = excluded.intersection(adj_list[vertice])
        pivoting_bron_kerbosch(adj_list, clique + [vertice], new_candidates, new_excluded, counter)
        candidates.remove(vertice)
        excluded.add(vertice)

def main():
    global dolphins
    global nodes
    
    # Gets data from dolphins.txt file
    graph_data = get_data()
    dolphins = graph_data
    
    # Builds adjacency list
    adj_dict = make_adj_list(dolphins)
    adj_list = make_adj_list_without_keys(adj_dict)
    nodes = set(range(1, len(adj_list)))
    clusttering = clustering_coeff(adj_list)
    
    print("Average Clusttering Coefficient: ", clusttering)
    print()
    
    # Calls Bron Kerbosch w/o Pivoting
    report = Counter('## %s' % basic_bron_kerbosch.__doc__)
    basic_bron_kerbosch(adj_list, [], set(nodes), set(), report)
    report.print_cliques()
    print()
    
    # Calls Bron Kerbosch with Pivoting
    report = Counter('## %s' % pivoting_bron_kerbosch.__doc__)
    pivoting_bron_kerbosch(adj_list, [], set(nodes), set(), report)
    report.print_cliques()

main()
