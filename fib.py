#!/usr/bin/python
# -*- coding:utf-8 -*-
from tail import tail_call_optimized


#@tail_call_optimized
def Fib(n):
	if n<2:
		return n
	else:
		return Fib(n-1) + Fib(n-2)



def Fib1(n, b1=1, b2=1, c=3):
	if n<3:
		return 1
	else:
		if n == c:
			return b1+b2
		else:
			return Fib1(n, b1=b2,b2=b1+b2,c=c+1)


@tail_call_optimized
def Fib2(n, b1=1, b2=1, c=3):
	if n<3:
		return 1
	else:
		if n == c:
			return b1+b2
		else:
			return Fib2(n, b1=b2,  b2=b1+b2, c=c+1)

if __name__ == '__main__':
	import sys
	import time
	start = time.time()
	print Fib1(int(sys.argv[1]))
	print 'Cost:', (time.time() - start)
