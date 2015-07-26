def dfs(graph,b,e):
    out=0
    discoverd=[]
    stack=[]
    stack.append(b)
    while e not in discoverd and len(stack)!=0:
        v=stack.pop()
        if v not in discoverd:
            discoverd.append(v)
            if e in discoverd:
                break
            if v in graph:
                if len(list(set(graph[v])-set(discoverd))) > 1:
                   # print(graph[v])        
                    out+=1
                for x in graph[v]:
                    stack.append(x)
    
    return out
t=int(input())
for test in range(0,t):
    r,c=map(int,input().strip().split())
    mat=[]
    graph={}
    for i in range(0,r):
        l=list(input())
        if len(l)==c:
            mat.append(l)
    hops=int(input())
    k=1
    b=0
    e=0
    for i in range(0,r):
        for j in range(0,c):
            graph[k]=[]
            if mat[i][j]=='.' or mat[i][j]=='M' or mat[i][j]=='*':
                if j != c-1:
                    if mat[i][j+1]=='.' or mat[i][j+1]=='M' or mat[i][j+1]=='*':
                        graph[k].append(k+1)
                if j != 0:
                    if mat[i][j-1]=='.' or mat[i][j-1]=='M' or mat[i][j-1]=='*':
                        graph[k].append(k-1)
                if i !=0 :
                    if mat[i-1][j]=='.' or mat[i-1][j]=='M' or mat[i-1][j]=='*':
                        graph[k].append(k-c)
                if i != r-1:
                    if mat[i+1][j]=='.' or mat[i+1][j]=='M' or mat[i+1][j]=='*':
                        graph[k].append(k+c)
            if mat[i][j]=='*':
               e=k
            if mat[i][j]=='M':
               b=k
            

            k+=1
            
    finalGraph={}
    for key in graph:
        if len(graph[key])!=0:
            finalGraph[key]=graph[key]

    out=dfs(finalGraph,b,e)
    
   #print(out)
    if hops == out:
        print("Impressed")
    else:
        print("Oops!")
