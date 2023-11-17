a=int(input())

ans=100

if a>2000:
	ans=100+(a-2000+499)//500*5
print(ans)