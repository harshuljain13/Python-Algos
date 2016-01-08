from collections import defaultdict
graph = defaultdict(list)
visited = dict()

def dfs(graph,s):
    stack = list()
    visited[s] = True
    for adjnode in graph[s]:
        if visited[adjnode] == False:
            visited[adjnode] = True
            print 'visited:' + adjnode
            stack.append(adjnode)
            while(len(stack)>0):
                node = stack.pop()
                for subadjnode in graph[node]:
                    if visited[subadjnode] == False:
                        print 'visited:' + subadjnode
                        visited[subadjnode] = True
                        stack.append(subadjnode)
                

        
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
