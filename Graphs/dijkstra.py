"""
Use Dijkstra's Algorithm to find the shortest route between two vertices in
a graph.
"""
from form_graph import form_graph
from form_edges import form_edges
from connected import is_connected

class Vertices():
    vertex_list = []
    def __init__(self, name, dist, prev):
        Vertices.vertex_list.append(self)
        self.name = name
        self.dist = dist
        self.prev = prev
    def __str__(self):
        return "Vertex: {} || Dist: {} || Prev: {}".format(self.name, self.dist, self.prev)

def dijkstra_step(g, v, dist):
    # unknown vertices set
    l = []
    for u in g[v]:
        if any(i.name == u for i in Vertices.vertex_list):
            pass
        else:
            l.append(u)
            Vertices('%s' %u, int('%s' %dist) + 1, '%s' %v)
            g[u].remove(v)
    del g[v]
    return l

def dijkstra(g,start, end):
    Vertices(start,0,0)
    count = 0
    l = [start]
    done = []
    Q = []
    while g != {}:
        k = []
        for i in l:
            if i in list(g.keys()):
                if i not in done:
                    done.append(i)
                    l2 = dijkstra_step(g, i, count)
                    for j in l2:
                        k.append(j)
        l = k
        count += 1
    for i in Vertices.vertex_list:
        if str(i.name) == str(end):
            distance = i.dist
    if end in list(g.keys()):
        return "These two vertices are not connected!"
    else:
        return distance
    
#Connected Check
#g = {1:[2,5], 2:[1,3], 3:[2], 4:[7,8], 5:[1,6], 6:[5,8], 7:[4], 8:[4,6]}
#print(dijkstra(g,3,7))

#Disconnected check
#g = {1:[], 2:[]}
#print(dijkstra(g,1,2))

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
            start = input("Enter the starting vertex\n>>> ")
            if start in list(g.keys()):
                end = input("Enter the end vertex\n>>> ")
                if end in list(g.keys()):
                    print(dijkstra(g, start, end))
                else:
                    print("This vertex is not in the graph!")
            else:
                print("This vertex is not in the graph!")
            
            


# This stops from running when I import it           
if __name__ == '__main__':
    shell()

