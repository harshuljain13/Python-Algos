from collections import defaultdict
import heapq

graph = defaultdict(list)
visited = dict()
distance = dict()
previous = dict()
paths = list()

def dijkstra(graph,source_node):
    for node in graph:
        distance[node] = 99999
        previous[node] = None
        visited[node] = False
    distance[source_node] = 0
    #define priority queue
    pqueue = [(distance[node],node) for node in graph]
    heapq.heapify(pqueue)
    while(len(pqueue) > 0):
        v = heapq.heappop(pqueue)
        visited[v[1]] = True
        for adjnode in graph[v[1]]:
            if visited[adjnode[0]] == True:
                continue
            if distance[adjnode[0]] > distance[v[1]]+int(adjnode[1]):
                distance[adjnode[0]]=distance[v[1]]+int(adjnode[1])
                previous[adjnode[0]] = v[1]
        for i in range(len(pqueue)):
            heapq.heappop(pqueue)
        pqueue = [(distance[node],node) for node in graph if visited[node] is False]
        heapq.heapify(pqueue)

    #print 'Distance:' , distance
    #print 'Previous:' , previous

def path(target_node,source_node):
    if target_node == source_node:
        paths.append(target_node)
        print 'Path to node', paths[::-1]
    else:
        paths.append(target_node)
        path(previous[target_node],source_node)
    
def main():
    n,e = map(int,raw_input().split())
    for count in range(e):
        v1,v2,w = raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))

    print 'enter source node'
    source_node = raw_input()
    print 'enter target node'
    target_node = raw_input()

    dijkstra(graph,source_node)
    path(target_node,source_node)

if __name__ == '__main__':
    main()
    
