#uses python3
def karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		n_2 = n // 2

		a = x // 10**(n_2)
		b = x % 10**(n_2)
		c = y // 10**(n_2)
		d = y % 10**(n_2)

		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_bc_sum = karatsuba(a+b,c+d) - ac - bd
		prod = ac * 10**(2*n_2) + (ad_bc_sum * 10**n_2) + bd

		return prod

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
