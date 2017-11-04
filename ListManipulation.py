def l(n):
	p=print;r=n;p(r)
	while 1:
		r=r[::-1];p(r)
		for i in range(0,len(n)-1,2):r[i],r[i+1]=r[i+1],r[i]
		p(r)
		if r==n:break