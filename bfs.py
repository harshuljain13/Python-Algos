from collections import defaultdict,deque

graph = defaultdict(list)
visited = dict()

def bfs(graph, s):
    queue = deque()
    queue.append(s)
    while(len(queue) >0):
        v=queue.popleft()
        if visited[v] == False:
            visited[v] = True
            print 'visited:' + v
            for adjnode in graph[v]:
                if visited[adjnode] == False:
                    queue.append(adjnode)
    
def main():
    n,e = map(int,raw_input().split())
    for i in range(e):
        v1,v2 = raw_input().split()
        graph[v1].append(v2)
        graph[v2].append(v1)

    for node in graph:
        visited[node] = False
        print node

    s= raw_input()
    bfs(graph, s)

if __name__ == '__main__':
    main()
