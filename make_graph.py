from collections import defaultdict

def main():
    n,e = map(int,raw_input().split())
    graph = defaultdict(list)

    for i in range(e):
        node,neighbour = raw_input().split()
        graph[node].append(neighbour)
        graph[neighbour].append(node)

    for node in graph:
        print node + '--->' + str(graph[node])

if __name__ == '__main__':
    main()
