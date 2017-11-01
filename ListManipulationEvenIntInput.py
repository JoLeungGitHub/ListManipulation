def list_manipulation(n):
	r = [x for x in range(1, n+1)]
	print(r)
	done = r
	while True:
		r = r[::-1]
		print(r)
		r[::2], r[1::2] = r[1::2], r[::2]
		print(r)
		if r == done:
			break