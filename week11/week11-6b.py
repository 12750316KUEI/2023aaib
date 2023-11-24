a=list(map(int,input().split()))

#a[0] a[1] ... a[9]
ans=0
for b in a: #special for loop
	if b%3==0: ans+=1
	
print(ans)