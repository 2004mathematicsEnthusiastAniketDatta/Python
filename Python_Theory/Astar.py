import heapq
def h(node):
    return distance[node]
def g(node1,node2):
    return graph[node1][node2]

def astar(start,goal):
     queue=[]
     heapq.heappush(queue,((0+h(start)),start))
     cost = {start:0}
     path = {start: [start]}
     while queue:
            (priority,current) = heapq.heappop(queue)
            if current == goal :
                return path[current]
            for next_node in graph[current].keys():
                new_cost = cost[current] + g(current,next_node)
                if next_node not in cost or new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    priority = new_cost + h(next_node)
                    heapq.heappush(queue,(priority,next_node))
                    path[next_node] = path[current] + [next_node]
     return []

graph = {
     'S':{'B':4,'C':3},
     'B':{'E':12,'F': 5},
     'C':{'D':7 ,'E':10},
     'D':{'E':2},
     'E':{'G':5},
     'F':{'G':16},
     'G':{}
 }
distance ={
        'S':14,
        'B':12,
        'C':5,
        'D':6,
        'E':4,
        'F':11,
        'G':0
    }
print(astar('S','G'))
