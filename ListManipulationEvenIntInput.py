def l(n):
	p=print;r=list(range(n));p(r);d=r
	while 1:
		r=r[::-1];p(r);r[::2],r[1::2]=r[1::2],r[::2];p(r)
		if r==d:break