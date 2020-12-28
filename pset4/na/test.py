# seq = 'apple'
# print(seq[1:len(seq)])

# sequence = 'apple'
# print(list(sequence))

# sequence = 'apple'
# print(sequence[1:])

# a = 'aba'
# print(len(a))

# print(list(a))
# wl = list(a)
# print(wl[0])

# wl.insert(1,'v')
# print(wl)

# sequence = 'appla'
# print(sequence[0])
# print(sequence[-2])

# print(sequence[0] == sequence[-1])

# res.append(permutation[:i] + array[0:1] + permutation[i:])

# a = 'a'
# for i in range(len(a)):
# 	print(len(a))
# 	print(i)

# s = 'nt'
# ps = 't'

# print(ps[:0])
# print(s[0])
# print(ps[0:])


def fact(n):
	if n == 1:
		return(n)

	return(n*fact(n-1))

print(fact(6))


n = 1
factorial = 6
for i in range(factorial):
	n = n*(i+1)

print(n)
