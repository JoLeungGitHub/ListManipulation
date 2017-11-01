def list_manipulation(n):
	r = n
	print(r)
	while True:
		i = 0
		r = r[::-1]
		print(r)
		while i < len(r) - 1:
			r[i], r[i+1] = r[i+1], r[i]
			i += 2
		print(r)
		if r == n:
			return "done"
