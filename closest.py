input()
l=list(map(int, input().strip().split()))
l.sort()
diff=abs(l[1]-l[0])
pairs={}
pairs[l[1]]=l[0]
for i in range(1,len(l)-1):
   
        if abs(l[i+1]-l[i]) < diff:
            diff=l[i+1]-l[i]
            pairs.clear()
            pairs[l[i+1]]=l[i]
        elif abs(l[i+1]-l[i]) == diff:
            pairs[l[i+1]]=l[i]

        else:
              continue
   
pstr=""
for k in sorted(pairs.keys()):
    pstr+= str(pairs[k])+" "+str(k)+" "

print(pstr)
