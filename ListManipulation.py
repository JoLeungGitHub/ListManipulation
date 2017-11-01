def list_manipulation(n):
	r = n[::-1]
	if len(r) >=2 :
		i = 0
		r[i], r[i+1] = r[i+1], r[i]

[1 ,2, 3, 4]
[4, 3, 2, 1]
[3, 4, 1, 2]
[2, 1, 4, 3]
[1, 2, 3, 4]
