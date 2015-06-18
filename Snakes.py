graphDict={}
test=int(input())
ladDict={}
dist={}
prev={}
def dijsktra():
    Q=[]
    dist[1]=0
    prev[1]=-1

    for i in range(1,101):
        if i != 1:
            dist[i]=-1
            prev[i]=-1
        Q.append(i)
    
    while len(Q)>0:
        mini=dist[Q[0]]
        u=Q[0]
        for q in Q:
            if mini>dist[q] and dist[q]!=-1:
                mini=dist[q]
                u=q
                
        Q.remove(u)
        for v in graphDict[u]:
            
            alt=dist[u]+1
            if alt<dist[v] or dist[v]==-1:
                if v not in range(u+1,u+7):
                    dist[v]=dist[u]
                else:
                    dist[v]=alt
                prev[v]=u


for i in range(0,test):
    graphDict.clear()
    ladDict.clear()
    dist.clear()
    prev.clear()
    ladders=int(input())  
    for i in range(0,ladders):
        x,y=input().split()
        x=int(x)
        y=int(y)
        ladDict[x]=y
    snakes=int(input())
    snakeDict={}
    for i in range(0,snakes):
        x,y=input().split()
        x=int(x)
        y=int(y)
        snakeDict[x]=y

    for i in range(1,101):
        graphDict[i]=[]
        if i not in ladDict.keys() and i not in snakeDict.keys():
            for j in range(i+1,i+7):
                if j<=100:
                    graphDict[i].append(j)
        else:
            if i in ladDict.keys():
                graphDict[i]=[ladDict[i]]+graphDict[i]
            if i in snakeDict.keys():
                graphDict[i]=[snakeDict[i]]+graphDict[i]
    dijsktra()
    print(dist[100])
