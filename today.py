
def divisor(n):
	sum_i=0
	for i in range(1, (n//2)+1):
		if n%i==0:
			sum_i+=i
			
	if sum_i==n:return("YES")
	else:return("NO")
	

n=int(input())
print(divisor(n))