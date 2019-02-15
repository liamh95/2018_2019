# Implement the Pollard-Rho Algorithm and solve the following DLPs:

# 1) Find x such that (2)^x = (642) mod (100003).

# 2) Find x such that (2)^x = (24) mod (100003).
from Crypto.Util.number import GCD, inverse

prime = 48611
gen = 19
logme = 24717


def f(x, a, b, g, h, p):
	if x < (p//3):
		return (g*x) % p, (a+1) % (p-1), b % (p-1)
	if (p//3) <= x < (2*p//3):
		return (x*x) % p, (2*a) % (p-1), (2*b) % (p-1)
	return (h*x) % p, a % (p-1), (b+1) % (p-1)



xi = 1
yi = 1
alpha = 0
beta = 0
gamma = 0
delta = 0

iterations = 0
first = True
while first or xi != yi:
	first = False
	iterations += 1
	(xi, alpha, beta) = f(xi, alpha, beta, gen, logme, prime)
	(yi, gamma, delta) = f(yi, gamma, delta, gen, logme, prime)
	(yi, gamma, delta) = f(yi, gamma, delta, gen, logme, prime)
	#print(f'i: {iterations}   xi: {xi}   yi: {yi}   ai: {alpha}   bi: {beta}   gamma: {gamma}   delta: {delta}')

u = (alpha - gamma) % (p-1)
v = (beta - delta) % (p-1)

