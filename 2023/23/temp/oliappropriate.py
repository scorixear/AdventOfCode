import aocd
import networkx as nx

data = aocd.get_data(day=23, year=2023).split("\n")
n, m = len(data), len(data[0])

def tadd(a,b): return (a[0]+b[0], a[1]+b[1])
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
slopes = [".><",".<>",".v^",".^v"]

M = {(i,j):c for i,line in enumerate(data) for j, c in enumerate(line)}
S = (0,next(i for i,c in enumerate(data[0]) if c=='.'))
E = (n-1,next(i for i,c in enumerate(data[-1]) if c=='.'))

visited = {S}
stack = [(S,i) for i,di in enumerate(dirs) if tadd(S,di) in M and M[tadd(S,di)] in '.<>^v']
graphs = [nx.DiGraph(), nx.Graph()]
while len(stack):
    start,direction = stack.pop()
    prev, cpos, le = start, tadd(start,dirs[direction]), 1
    visited.add(cpos)
    way = slopes[direction].index(M[cpos])
    ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
            for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    while len(ndirs) == 2:
        direction = next(di for di,_ in ndirs if prev != tadd(cpos,dirs[di]))
        prev, cpos, le = cpos, tadd(cpos,dirs[direction]), le+1
        way |= slopes[direction].index(M[cpos])
        visited.add(cpos)
        ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
                for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    if way == 1: graphs[0].add_edge(start, cpos, cost=le)
    else: graphs[0].add_edge(cpos, start, cost=le)
    graphs[1].add_edge(start, cpos, cost=le)

    for di in [di2 for di2,vis in ndirs if not(vis)]: stack.append((cpos,di))

for i,graph in enumerate(graphs,1):
    res = max(nx.path_weight(graph, path, "cost") for path in nx.all_simple_paths(graph, S, E))
    print("Part%d: %d" % (i,res))