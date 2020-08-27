import time
import math 
import numpy as np
from sympy import (pi, exp, integrate, simplify, cos, sin, sqrt)
from itertools import (combinations_with_replacement, permutations)

start_time = time.time()

tl=[]; w=[]
Xs = [1,-4, 5,-2] 
xy=(0,1)
pi=3.14159265359
e=2.71828182846

#n=int(input("Enter number of qubits: "))	
n=2
r=n

def xSubset(x,r):
	return list(combinations_with_replacement(xy,r)) + list(permutations(xy,r))

x=xSubset(xy,r)
tl= list(dict.fromkeys(x))

def seq1(n):
	td= []
	while n != 0:
		d=2**n
		td.append(d)
		n -= 1
	return td
		
s= seq1(n)

fl= list(np.divide(tl, s))

for i in fl:
	j=i[0]+i[1]
	w.append(j)

R=e**(pi*-1j)

N =len(Xs)
t0 = 2*((1*R**(2*w[3]*0) + 5*R**(2*w[2]*0)  -4**R**(2*w[1]*0) -2**R**(2*w[0]*0))/sqrt(N))
t1 = 2*((1*R **(2*w[3]*1) + 5*R**(2*w[2]*1)  -4**R**(2*w[1]*1) -2**R**(2*w[0]*1))/sqrt(N))
t2 = 2*((1*R **(2*w[3]*2) + 5*R**(2*w[2]*2)  -4**R**(2*w[1]*2) -2**R**(2*w[0]*2))/sqrt(N))
t3 = 2*((1*R **(2*w[3]*3) + 5*R**(2*w[2]*3)  -4**R**(2*w[1]*3) -2**R**(2*w[0]*3))/sqrt(N))

if __name__ == "__main__":

	print("the qubits are:", tl)
	print("|x> =", fl)
	print("w =", w)
	#print("dft is: ", Qft(Xs))
	print(t0,t1,t2,t3)
	print("%s seconds" % (time.time() - start_time))
