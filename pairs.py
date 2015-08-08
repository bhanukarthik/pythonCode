def pairs(a,k):
  return len(set(a)&set(list(map(lambda x:x+k,a))))

if __name__ == '__main__':
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  print(pairs(a,k))