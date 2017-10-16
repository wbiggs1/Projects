"""
Forms a graph from a list of edges.
A graph is in the form of a dictionary of vertices each with a corresponding
list of vertices it is adjacent to.
"""

# input is a list of tuples

def form_graph(l):
    graph = {}
    for edge in l:
        v0 = edge[0]
        v1 = edge[1]
        if v0 in list(graph.keys()):
            graph[v0].append(v1)
        else:
            graph[v0] = [v1]
        if v1 in list(graph.keys()):
            graph[v1].append(v0)
        else:
            graph[v1] = [v0]
    return graph
        
def shell():
    print ("Enter a list of edges, written in the form (1,2),(2,3),..., that you wish to form into a graph or enter quit to exit")
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
            print(form_graph(l))

# This stops from running when I import it           
if __name__ == '__main__':
    shell()
