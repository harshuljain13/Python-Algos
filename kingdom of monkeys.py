

#1
#4 3
#1 2
#2 3
#3 1
#1 2 3 5
def main():
    t = int(raw_input())
    for count in range(t):
        graph = dict()
        visited = dict()
        stack =[]
        results = []
        maxi =0
        n,e = map(int,raw_input().split())
        for  i in range(n):
            graph[i+1] = list()
        for i in range(e):
            v1,v2 = map(int,raw_input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)

        ban = map(int,raw_input().split())
        
        for node in graph:
            visited[node] = False
            
        for node in graph:
            if visited[node]==False:
                sumi=0
                stack.append(node)
                while(len(stack)>0):
                    v = stack.pop()
                    visited[v]=True
                    sumi = sumi + ban[v-1]
                    
                    for adjnode in graph[v]:
                        if visited[adjnode]==False:
                            visited[adjnode]=True
                            stack.append(adjnode)
            results.append(sumi)

        for ele in results:
            if ele > maxi:
                maxi = ele
                
        print maxi

if __name__ == '__main__':
    main()
