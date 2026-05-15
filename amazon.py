n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(n):
  for j in range (i+1,len(arr)):
    if arr[j]>arr[i]:
      larger=arr[j]
      ans.append(larger)
      break;

  print(*ans)
      