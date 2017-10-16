"""
A program which will take as an input a graph and
output either a Eulerian path or a Eulerian cycle, or state that it is not
possible. A Eulerian Path starts at one node and traverses every edge of a
graph through every node and finishes at another node. A Eulerian cycle is
a eulerian Path that starts and finishes at the same node.
A graph contains a Eulerian cycle if and only if it is connected and every
vertex has even degree.
"""

from form_graph import form_graph
from form_edges import form_edges
from connected import is_connected

def is_Eulerian(graph):
    if is_connected(graph):
        test = 0
        for v in list(graph.keys()):
            neighbours = graph[v]
            if len(neighbours) % 2 == 0:
                pass
            else:
                test = 1
        if test == 0:
            return True
        else:
            return False
    else:
        return False

def is_bridge(e,l):
    # l must correspond to connected graph
    j = l.index(e)
    k = []
    for i in [x for x in range(len(l)) if x != j]:
        k.append(l[i])
    h = form_graph(k)
    if is_connected(h):
        return False
    else:
        return True


            
def fleury_step(g, edges, start_vertex):
    v = start_vertex
    if len(form_edges(g)) == 0:
        print("Done!")
    else:
        l = form_edges(g)
        i = 0
        test = 0
        while i < len(l):
            if v == l[i][0]:
                if not is_bridge(l[i], l):
                    edges.append(l[i])
                    v = l[i][1]
                    l.remove(l[i])
                    test = 1
                    break
            elif v == l[i][1]:
                l[i] = list(l[i])
                l[i][0], l[i][1] = l[i][1], l[i][0]
                l[i] = tuple(l[i])
                if not is_bridge(l[i], l):
                    edges.append(l[i])
                    v = l[i][1]
                    l.remove(l[i])
                    test = 1
                    break
            else:
                pass
            i += 1
        if test == 0:
            edges.append(l[0])
            l.remove(l[0])
        g = form_graph(l)
    return(g, edges, v) 



def fleury(g):
    edges = []
    v = list(g.keys())[0]
    l = form_edges(g)
    while g != {}:
        (g, edges, v) = fleury_step(g, edges, v)
    return edges
    
    
def Eulerian(g):
    if is_Eulerian(g):
        print("The graph is Eulerian!")
        return fleury(g)
    else:
        print("The graph is not Eulerian. :(")
        return

# Konigsburg Bridge Example
#G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
#print(Eulerian(G))

# testing an eulerian cycle
#G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
#print(Eulerian(G))

def shell():
    print ("Enter a list of edges, written in the form (1,2),(2,3),..., corresponding to the graph that you wish to seek for a Eulerian cycle through or enter quit to exit. The output is a list of the edges of a Eulerian cycle, or a statement that there isn't one.")
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
            print(Eulerian(form_graph(l)))

shell()

"""
g = {1:[2,3],2:[1,3],3:[1,2]}




print(fleury(g))



h = form_graph([])
print(is_connected(h))

"""    



