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

graph =             {v[0]:[v[1],v[3]],
                    v[1]:[v[0],v[2]],
                    v[2]:[v[1],v[3], v[4]],
                    v[3]:[v[0],v[2]],
                    v[4]:[v[2],v[5], v[6]],
                    v[5]:[v[4],v[6]],
                    v[6]:[v[4],v[5], v[7]],
                    v[7]:[v[6]]}

def find_u_from_v(G,u,v):
    Q = list()
    marked = list()

    marked.append(u)
    Q.append(u)

    while Q:
        c = Q.pop(0)
        for n in G[c]:
            if n == v: #from starting point u we found v
                return True
            else:
                if n not in marked:
                    marked.append(n)
                    Q.append(n)
    return False


def get_bridges(G,u):
    Q = list()
    marked = list()
    bridges = list()

    marked.append(u)
    Q.append(u)

    while Q:
        c = Q.pop(0)
        for n in G[c]:

            G[c].remove(n)
            G[n].remove(c)

            if find_u_from_v(G, n, c) == False:

                bridges.append([c,n])

            G[c].append(n)
            G[n].append(c)
            G[c].sort()
            G[n].sort()

            if n not in marked:
                marked.append(n)
                Q.append(n)

    return bridges


print( get_bridges(graph, v[0]) )
        





