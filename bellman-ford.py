from collections import defaultdict

graph = defaultdict(list)
distance = dict()
previous = dict()
paths = []

def bellman_ford(source_node, n):
    for node in graph:
        distance[node]= 99999
    distance[source_node] = 0
    
    for k in range(n):
        for node in graph:
            for adjnode in graph[node]:
                if distance[adjnode[0]] > distance[node] + int(adjnode[1]):
                    previous[adjnode[0]] = node
                    distance[adjnode[0]] = distance[node] + int(adjnode[1])

        for node in graph:
            for adjnode in graph[node]:
                if distance[adjnode[0]] > distance[node] + int(adjnode[1]):
                    print 'Negative cycle'
    print previous
    print distance

def main():
    n,e = map(int,raw_input().split())
    for count in range(e):
        v1,v2,w = raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))

    print 'enter source node'
    source_node = raw_input()
    bellman_ford(source_node, n)



if __name__ == '__main__':
    main()
        
        
    
