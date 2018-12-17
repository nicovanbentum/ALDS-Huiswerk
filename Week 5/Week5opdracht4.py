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

graph_strong = {v[0]:[v[1]],
                v[1]:[v[2]],
                v[2]:[v[0]]
}

graph =         {v[0]:[v[1]],
                 v[1]:[],
                 v[2]:[v[0],v[1]]
}

def is_strongly_connected_alternative(G):   #this would make more sense than the assignment, 
                                            #if a vertex has no outgoing edges the graph is obviously not strongly connected
    for v in G:
        if not G[v]:
            return False
    return True

print(is_strongly_connected_alternative(graph_strong))
print(is_strongly_connected_alternative(graph))

########actual assignment############

def can_reach_all(G, s): #helper function to check if you're able to visit every node from a given node
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
        if v not in marked: #if the graph has a vertex that's not in the visited vertices
            return False
    return True

def is_strongly_connected(G):
    final_answer = can_reach_all(G, v[2])

    new_graph = {}

    for key in G:
        new_graph[key] = list()
    for key in G:
        for value in G[key]:
            new_graph[value].append(key)

    final_answer = can_reach_all(new_graph, v[2])    
    return final_answer


print(is_strongly_connected(graph_strong))
print(is_strongly_connected(graph))

        





