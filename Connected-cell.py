visited=[]
r=int(input())
c=int(input())
matrix=[]
for i in range(0,r):
    matrix.append(input().split())

def getAdj(i,j):
    adj=[]
    if i!=0:
        if matrix[i-1][j]=='1':
            adj.append((i-1,j))
        if j!=c-1 and matrix[i-1][j+1]=='1':
            adj.append((i-1,j+1))
        if j!=0 and matrix[i-1][j-1]=='1':
            adj.append((i-1,j-1))
    if i!=r-1:
        if matrix[i+1][j]=='1':
            adj.append((i+1,j))
        if j!=c-1 and matrix[i+1][j+1]=='1':
            adj.append((i+1,j+1))
        if j!=0 and matrix[i+1][j-1]=='1':
            adj.append((i+1,j-1))
    
    if j!=0 and matrix[i][j-1]=='1':
        adj.append((i,j-1))
    if j!=c-1 and matrix[i][j+1]=='1':
        adj.append((i,j+1))

    return adj
    
    
def dfs(index):
    stack=[]
    stack.append(index)
    visitedTemp=[]
    while len(stack) > 0:
        tempIndex = stack.pop()
        if tempIndex not in visited:
            visited.append(tempIndex)
            visitedTemp.append(tempIndex)
            adj=getAdj(tempIndex[0],tempIndex[1])    
            for inx in adj:
                stack.append(inx)
            
    
    return len(visitedTemp)

maxV=0
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j] == '1' and (i,j) not in visited:
            x=dfs((i,j))
            if x > maxV:
                maxV=x
print(maxV)


