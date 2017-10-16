"""
Check if a finite graph is connected, using the breadth first search algoritm
"""
from form_graph import form_graph

def BFS(graph, h, v):
    if h == {}:
        h[v] = [0,0] # h gives how far a vertex u is from v, and it's predecessor
    else:
        pass
    for u in graph[v]:
        if u in list(h.keys()):
            pass
        else:
            h[u] = [1 + h[v][0], v]
            v = u
            BFS(graph, h, v)
    return h
"""
If h is the same length as g then every vertex is finitely many steps from v
so the graph is connected. Otherwise, you can't get to v.
"""


def is_connected(graph):
    if graph == {}:
        return True
    elif len(graph) == len(BFS(graph, {}, list(graph.keys())[0])):
        return True
    else:
        return False


def shell():
    print ("Enter a list of edges, written in the form (1,2),(2,3),..., that you wish to check correspond to a connected graph or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        test = 0
        l = entry.split(')')
        l.remove('') #Remove the extra emtpy string we get in the list
        for i in range(len(l)):
            l[i] = l[i].replace('(','')
            l[i] = l[i].replace(',','')
            l[i] = l[i].replace(' ','') #Remove any spaces
            l[i] = tuple(l[i])
            if len(l[i]) != 2:
                test = 1
        if entry == "quit":
            break
        if test == 1:
            print("Please enter a list of edges, written in the form (1,2),(2,3),...")
        else:
            g = form_graph(l)
            print(BFS(g, {}, list(g.keys())[0]))
            print(is_connected(g))


# This stops from running when I import it           
if __name__ == '__main__':
    shell()




