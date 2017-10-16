"""
Forms list of edges from graph.
"""

def form_edges(g):
    l = []
    for v in list(g.keys()):
        for u in g[v]:
            if (u,v) in l:
                pass
            else:
                l.append((v,u))
    return l
