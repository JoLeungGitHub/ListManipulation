def l(n):
	r=list(range(n));d=r
	while 1:
		r=r[::-1];r[::2],r[1::2]=r[1::2],r[::2];print(r)
		if r==d:break