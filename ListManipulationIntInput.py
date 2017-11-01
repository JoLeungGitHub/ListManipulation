def l(n):
	a=range;p=print;r=[x for x in a(n)];p(r);d=r
	while True:
		r=r[::-1];p(r)
		for i in a(0,n-1,2):r[i],r[i+1]=r[i+1],r[i]
		p(r)
		if r==d:break