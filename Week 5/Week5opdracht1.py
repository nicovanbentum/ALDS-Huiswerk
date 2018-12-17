    
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

Graph_disconnected = {v[0]:[v[4],v[5]],
                    v[1]:[v[4],v[5], v[6]],
                    v[2]:[v[4],v[5],v[6]],
                    v[3]:[v[7]],
                    v[4]:[v[0], v[1], v[5]],
                    v[5]:[v[0],v[1],v[2], v[4]],
                    v[6]:[v[1],v[2]],
                    v[7]:[v[3]]}

Graph_connected = {v[0]:[v[4],v[5]],
                    v[1]:[v[4],v[5], v[6]],
                    v[2]:[v[4],v[5],v[6]],
                    v[4]:[v[0], v[1], v[5]],
                    v[5]:[v[0],v[1],v[2], v[4]],
                    v[6]:[v[1],v[2]]}

def is_connected(G, s):
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
    for v in G:
        if v not in marked:
            return False
    return True

if(__name__ == "__main__"):
    print("Is graph connected: " + str(is_connected(Graph_disconnected, v[1])))
    print("Is graph connected: " + str(is_connected(Graph_connected, v[1])))

        





