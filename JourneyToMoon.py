def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

n,i=input().split()
n=int(n)
i=int(i)
graph={}
listOfNodes=[]
for x in range(0,i):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a in graph.keys() and b not in graph.keys():
        graph[a].append(b)
        graph[b]=[]
        graph[b].append(a)
    elif b in graph.keys() and a not in graph.keys():
        graph[b].append(a)
        graph[a]=[]
        graph[a].append(b)
    elif a in graph.keys() and b in graph.keys():
        graph[b].append(a)
        graph[a].append(b)
    else:
        graph[a]=[]
        graph[a].append(b)
        graph[b]=[]
        graph[b].append(a)
        
    if a not in listOfNodes:
        listOfNodes.append(a)
    if b not in listOfNodes:
        listOfNodes.append(b)
listOfNodes.sort()
tempList=[]
for y in range(1,len(listOfNodes)):
      if listOfNodes[y-1]+1!=listOfNodes[y]:
            graph[listOfNodes[y-1]+1]=[]
            tempList.append(listOfNodes[y-1]+1)
    
listOfNodes=sorted(union(listOfNodes,tempList))

grevisited={}
nodes=graph.keys()
alreadyCoverd=[]
for node in nodes:
    if node not in alreadyCoverd:
        grevisited[node]=[]
        visited=[]
        stack=[node]
        while len(stack)!=0:
            v=stack.pop()
            if v not in visited:
                visited.append(v)
                if v in graph:
                    for ne in graph[v]:
                        stack.append(ne)
        grevisited[node]=visited
        #print(grevisited[node])
        alreadyCoverd=union(alreadyCoverd,visited)


sums=[len(grevisited[k]) for k in grevisited.keys()]
total=(n*(n-1))/2
for s in sums:
    total=total-((s*(s-1))/2)
print (int(total))
