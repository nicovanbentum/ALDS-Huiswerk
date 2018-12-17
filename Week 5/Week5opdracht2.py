class Vertex:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):         # voor afdrukken
        return str(self.data)
    
    def __lt__(self, other):    # voor sorteren
        return self.data < other.data

v = [Vertex(i) for i in range(8)]

#########################
#       HUISWERK        #
#########################

Graph_cycles =      {v[0]:[v[4],v[5]],
                    v[1]:[v[4],v[5], v[6]],
                    v[2]:[v[4],v[5],v[6]],
                    v[4]:[v[0], v[1], v[5]],
                    v[5]:[v[0],v[1],v[2], v[4]],
                    v[6]:[v[1],v[2]]}

Graph_no_cycles = {v[0]:[v[4],v[5]],
                    v[1]:[v[4],v[6]],
                    v[2]:[v[5]],
                    v[3]:[v[7]],
                    v[4]:[v[0], v[1]],
                    v[5]:[v[0],v[2]],
                    v[6]:[v[1]],
                    v[7]:[v[3]]}

def has_cycles(G, s):
    Q = list()
    marked = list()

    Q.append(s)
    marked.append(s)

    while Q:
        current = Q.pop(0)
        for v in G[current]:
            if v not in marked:
                Q.append(v)
                marked.append(v)
            else:
                if current not in G[v]:
                    return True

    return False

print(has_cycles(Graph_cycles, v[1]))
print(has_cycles(Graph_no_cycles, v[1]))
        





