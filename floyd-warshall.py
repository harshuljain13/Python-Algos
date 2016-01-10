from collections import defaultdict

graph = defaultdict(list)
distance = dict()
previous = dict()

def main():
    n,e = map(int,raw_input().split())
    for count in range(e):
        v1,v2,w = raw_input().split()
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))

    for node in graph:
        distance[node] = dict()
        previous[node] = dict()
        for node2 in graph:
            distance[node][node2] = 99999
        distance[node][node] = 0
        for adjnode in graph[node]:
            distance[node][adjnode[0]] = adjnode[1]
        
    print distance
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(int(distance[i][j]), int(distance[i][k]) + int(distance[k][j]))
                previous[k][
    print distance
                
        

if __name__ == '__main__':
    main()
