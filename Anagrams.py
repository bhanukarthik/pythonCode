t=int(input())
for i in range(0,t):
    s=input()
    if len(s)%2!=0:
        print(-1)
    else:
        
        a=int(len(s)/2)
        
        x=s[0:a]
        y=s[a:len(s)]
        xd={}
        yd={}
        for c in x:
            if c in xd.keys():
                xd[c]+=1
            else:
                xd[c]=1
        for c in y:
            if c in yd.keys():
                yd[c]+=1
            else:
                yd[c]=1
        cs=0
        keys=list(set(yd.keys()) & set(xd.keys()))
        l=0
        for key in keys:
              cs+=abs(xd[key]-yd[key])
              if xd[key]>yd[key]:
                  l+=xd[key]
              else:
                  l+=yd[key]
        
        print(int(cs+((len(s)/2)-l)))
        
