def list_manipulation(n):
	r = [x for x in range(n)]
	print(r)
	d = r
	while True:
		r = r[::-1]
		print(r)
		r[::2], r[1::2] = r[1::2], r[::2]
		print(r)
		if r == d:
			break