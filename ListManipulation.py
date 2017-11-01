def list_manipulation(n):
	r = n
	print(r)
	while True:
		r = r[::-1]
		print(r)
		for i in range(0, len(n)-1, 2):
			r[i], r[i+1] = r[i+1], r[i]
		print(r)
		if r == n:
			return "done"
