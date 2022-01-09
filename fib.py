def productFib(prod):
	a,b=0,1
	while prod>a*b:
		temp=a
		a=b
		b=b+temp
	return [a,b, prod==a*b]
