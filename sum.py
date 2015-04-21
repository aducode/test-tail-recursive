#!/usr/bin/python
# -*- coding:utf-8 -*-
from tail import tail_call_optimized

def sum(n):
	if n>0:
		return n+sum(n-1)
	else:
		return 0


def sum1(n, total=0):
	if n<=0:
		return total
	else:
		return sum1(n-1, total = total+n)


@tail_call_optimized
def sum2(n, total=0):
        if n<=0:
                return total
        else:
                return sum2(n-1, total = total+n)



if __name__ == '__main__':
	import sys
	import time
	start = time.time()
	print sum2(int(sys.argv[1]))
	print 'Cost:', (time.time() - start)
