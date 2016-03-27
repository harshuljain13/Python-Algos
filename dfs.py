from collections import defaultdict
graph = defaultdict(list)
visited = dict()

##input:
##4 3
##1 2
##2 3
##3 4

def dfs(graph,s):
    stack = list()
    visited[s] = True
    stack.append(s)
    while(len(stack)>0):
        node = stack.pop()
        print 'visited'+node
        for subadjnode in graph[node]:
            if visited[subadjnode] == False:
                stack.append(subadjnode)
                visited[subadjnode] = True
                

        
def main():
    n,e = map(int,raw_input().split())
    for count in range(e):
        v1,v2 = raw_input().split()
        graph[v1].append(v2)
        graph[v2].append(v1)   ##undirected graph

    for node in graph:
        visited[node] = False
        print node + '---->' + str(graph[node])
        #print visited

    s = raw_input()
    dfs(graph, s)
    
if __name__ == '__main__':
    main()
