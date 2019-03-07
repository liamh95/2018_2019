def tk(k):
	if k==1:
		return -1
	if k==2:
		return -3
	return ((-1)*tk(k-1))-2*tk(k-2)

def count(k):
	return (2**k) + 1 - tk(k)


def tau(n):
	n0 = n
	n1 = 0
	i=0
	ret = []
	while n0 != 0 or n1 != 0:
		print('n0: ' + str(n0))
		print('n1: ' + str(n1))
		if n0 % 2 == 1:
			vi = 2-((n0-2*n1)%4)
			ret.append(vi)
			n0 -= vi
		else:
			ret.append(0)
		i += 1
		tmp = n0
		n0 = n1 - (n0//2)
		n1 = -(tmp//2)
		print('------------')
	return ret