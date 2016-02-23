from collections import defaultdict
import heapq

graph = defaultdict(list)

visited = dict()
distance = dict()

def prim(graph,s):
    for node in graph:
        visited[node]=False
        distance[node]=99999
    distance[s]=0
    pqueue = [(distance[node],node) for node in graph]
    heapq.heapify(pqueue)
    minimum_cost = 0
    while(len(pqueue)>0):
        v = heapq.heappop(pqueue)
        visited[v[1]]=True
        minimum_cost += distance[v[1]]
        for adjnode in graph[v[1]]:
            if visited[adjnode[0]]==True:
                continue
            if distance[adjnode[0]] > int(adjnode[1]):
                distance[adjnode[0]]=int(adjnode[1])
        for i in pqueue:
            heapq.heappop(pqueue)
        pqueue = [(distance[node],node) for node in graph if visited[node] is False]
        heapq.heapify(pqueue)
                
    print minimum_cost

def main():
    nodes,edges = map(int,raw_input().split())
    for count in range(edges):
        v1,v2,w = raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))

    print 'enter the source node'
    s = raw_input()
    prim(graph,s)
    
if __name__ == '__main__':
    main()
