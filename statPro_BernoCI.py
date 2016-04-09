'''
This program will calculate a confidnce interval given 
the sample size, mean, standard diviation, and level of confidence.
example (n,x,s,c)
Return it as a range(). 
'''

import math as m
# Main
def main():
	n = int(raw_input('Enter your sample size: '))
	y = float(raw_input('Enter the number of positive responces: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	ci = ci/100
	p = y/n
	e = two_zs(ci)*sampleStdD(p,n)

	print 'Your mean is: ' + str(p)
	print 'Your confidence interval at ' + str(ci*100) + '% is: ' + '[' + str(p-e) + ', ' + str(p+e) + ']'


def two_zs(ci):
	if ci == 0.8:
		z = 1.28
	elif ci == 0.9:
		z = 1.645
	elif ci == 0.95:
		z= 1.96
	elif ci == 0.98:
		z = 2.33
	elif ci == 0.99:
		z = 2.58
	return z

def sampleStdD(p,n):
	return m.sqrt(p*(1-p)/n)

main()