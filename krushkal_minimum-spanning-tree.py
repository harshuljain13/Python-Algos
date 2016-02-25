from collections import defaultdict

graph = defaultdict(list)
edges_list = list()
id_dict  = dict()

def root(temp_node):
    print id_dict
    while(id_dict[temp_node] != temp_node):
        temp_node = id_dict[id_dict[temp_node]]
    return temp_node
    
def union(node,adjnode):
    p = root(node)
    q = root(adjnode)
    id_dict[p] = id_dict[q]

def krushkal(graph):
    
    minimum_cost = 0

    for node in graph:
        id_dict[node]=node

    for edge in edges_list:
        weight = int(edge[0])
        node = edge[1]
        adjnode = edge[2]
        if root(node) != root(adjnode):
            minimum_cost += weight
            union(node,adjnode)
    
    print minimum_cost
            
def main():
    nodes,edges = map(int,raw_input().split())
    for count in range(edges):
        v1,v2,w = raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
        edges_list.append((w,v1,v2))

    edges_list.sort()
    krushkal(graph)

if __name__=='__main__':
    main()
