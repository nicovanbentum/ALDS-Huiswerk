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

#differing degrees = not weak euler
graph =         {v[0]:[v[1], v[2]],
                 v[1]:[v[0], v[3]],
                 v[2]:[v[0], v[3]],
                 v[3]:[v[1], v[2], v[4], v[6]],
                 v[4]:[v[3], v[5], v[6], v[7]],
                 v[5]:[v[4], v[6]],
                 v[6]:[v[3], v[4], v[5], v[7]],
                 v[7]:[v[4], v[6]]
                 }

#same degrees = weak euler
graph2 =               {v[0]:[v[1], v[2]],
                       v[1]:[v[0], v[3]],
                       v[2]:[v[0], v[3]],
                       v[3]:[v[1], v[2]]
                 }




def is_weak_euler_graph(G, s):
    start_count = len(G[s])

    for value in G:
        count = len(G[value])
        if count != start_count:
            return False
    return True

print(is_weak_euler_graph(graph, v[0]))
print(is_weak_euler_graph(graph2, v[0]))

def find_u_from_v(G,u,v):
    if len(G[u]) == 0 or len(G[v]) == 0:
        return False
    
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

def is_bridge(G, u, v):
    ret = None

    G[u].remove(v)
    G[v].remove(u)
    if find_u_from_v(G, u, v) == True:
        ret = False
    else:
        ret = True
    G[u].append(v)
    G[v].append(u)
    G[u].sort()
    G[v].sort()

    return ret

def get_euler_circuit(G, s):
    return_list = list()
    Q = list()

    t = None

    Q.append(s)
    return_list.append(s)

    while Q:
        current = Q.pop(0)
        for child in G[current]:
                if len(Q) > 0:
                    continue

                if is_bridge(G, current, child):
                    if len(G[current]) == 1:
                        t = child
                    else:
                        continue
                else:
                    t = child
                
                
                Q.append(t)
                G[current].remove(t)
                G[t].remove(current)
                return_list.append(t)
                print(return_list)

    return return_list

print(get_euler_circuit(graph, v[0]))
        





