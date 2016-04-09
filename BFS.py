def bfs(graphMap,distMap,root):
    #parentMap={}
    queue=[]
    queue.append(root)

    while len(queue) > 0:
        current = queue.pop()

        if current in graphMap:
            for s in graphMap[current]:
                if distMap[s] == -1 or distMap[s] > distMap[current]+1:
                    distMap[s] = distMap[current]+1
                    #parentMap[s] = current
                    queue.append(s)


numOfTest = int(input())

for i in range(0,numOfTest):
    Nodes,Edges = map(int,input().split())
    graphMap={}
    for j in range(0,Edges):
        fromNode, toNode = map(int,input().split())
        if fromNode not in graphMap:
            graphMap[fromNode] = []
        if toNode not in graphMap:
            graphMap[toNode] = [] 
        graphMap[fromNode].append(toNode)
        graphMap[toNode].append(fromNode)
    nodeS = int(input())
    distMap={}
    for k in range(1,Nodes+1):
        distMap[k]=-1
        if k == nodeS:
            distMap[k]=0
    bfs(graphMap,distMap,nodeS) 
    s=""
    for key in distMap.keys():
        if  distMap[key] != 0 and distMap[key] != -1:
            s+=str(distMap[key]*6)+" "
        elif  distMap[key] == -1:
            s+=str(distMap[key])+" "
    print(s)