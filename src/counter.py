class Counter(object):
    '''This class counts the number of cliques and recursive calls made to find those cliques.'''
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []
 
    def calls_count(self):
        self.cnt += 1
 
    def save_clique(self, clique):
        self.cliques.append(clique)
 
    def print_cliques(self):
        print(self.name)
        print('Number of Recursive calls: %s' % self.cnt)
        for i, clique in enumerate(self.cliques):
            print('%d: %s' % (i, clique)," -> %d - Vertices" % len(clique))