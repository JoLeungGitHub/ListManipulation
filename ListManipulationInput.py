n=int(input());a=range;r=list(a(n));d=r
while 1:
	r=r[::-1]
	for i in a(0,n-1,2):r[i],r[i+1]=r[i+1],r[i]
	print(r)
	if r==d:break
