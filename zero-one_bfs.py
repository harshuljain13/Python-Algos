from collections import defaultdict,deque
from decimal import Decimal

graph = defaultdict(list)
distance = dict()
previous = dict()
paths =[]

def zero_one_bfs(graph,source_node):
    doublequeue = deque()
    for node in graph:
        distance[node] = 999999
    distance[source_node] = 0

    doublequeue.append(source_node)
    while(len(doublequeue)>0):
        v = doublequeue.pop()
        for adjnode in graph[v]:
            if distance[adjnode[0]] > distance[v] + int(adjnode[1]):
                distance[adjnode[0]] = distance[v] + int(adjnode[1])
                previous[adjnode[0]] = v
                if adjnode[1] == '0':
                    doublequeue.append(adjnode[0])
                if adjnode[1]=='1':
                    doublequeue.appendleft(adjnode[0])
        
    #print 'Distance:',distance
    #print 'Previous:',previous

def path(t,s):
    if t == s:
        paths.append(t)
        print 'Path:' , paths
    else:
        paths.append(t)
        path(previous[t],s)
    
    

def main():
    n,e = map(int,raw_input().split())
    for i in range(e):
        v1,v2,w= raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))

    source_node = raw_input()
    target_node =raw_input()
    zero_one_bfs(graph,source_node)
    path(target_node,source_node)
    
    
    
    

if __name__ == '__main__':
    main()
