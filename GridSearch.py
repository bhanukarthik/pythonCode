def check(i,j):
    global array,array1,r1,c1
    list1=[]
    list2=[]
    for x in range(0,r1):
        list1.append(array[i+x][j:j+c1])
        list2.append(array1[x])
    if list1 == list2:
        return True
numTest = int(input())

for i in range(0,numTest):
    r,c=map(int, input().strip().split())
    array={}
    for j in range(0,r):
        array[j]=list(input().strip())
    r1,c1=map(int, input().strip().split())
    array1={}
    for k in range(0,r1):
        array1[k]=list(input().strip())
    done=False
    if r1>r or c1>c:
        continue
    for x in range(0,r):
        if done:
            break
        for y in range(0,c):
            if array[x][y] == array1[0][0] and y+c1-1<=c-1:
                    if array[x][y+c1-1] == array1[0][c1-1] and x+r1-1 <= r-1:
                        if array[x+r1-1][y]==array1[r1-1][0]:
                            if array[x+r1-1][y+c1-1]==array1[r1-1][c1-1]:
                                if check(x,y):
                                    done=True
                                    print("YES")
                                    break
    if not done:
        print("NO")