def list_manipulation(n):
	r = [x for x in range(n)]
	print(r)
	d = r
	while True:
		r = r[::-1]
		print(r)
		for i in range(0, n-1, 2):
			r[i], r[i+1] = r[i+1], r[i]
		print(r)
		if r == d:
			break