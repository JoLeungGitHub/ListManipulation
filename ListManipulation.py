def l(n):
	r=n
	while 1:
		r=r[::-1]
		for i in range(0,len(n)-1,2):r[i],r[i+1]=r[i+1],r[i]
		print(r)
		if r==n:break