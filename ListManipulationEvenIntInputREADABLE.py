def list_manipulation(n):
	r = [x for x in range(n)]
	d = r
	while True:
		r = r[::-1]
		r[::2], r[1::2] = r[1::2], r[::2]
		print(r)
		if r == d:
			break