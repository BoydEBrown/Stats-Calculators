'''
This program will calculate a confidnce interval given 
the sample size, mean, standard diviation, and level of confidence.
example (n,x,s,c)
Return it as a range(). 
'''

import math as m

def sampleStdD(n,s):
	return s/m.sqrt(n)
	
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
	
def std_err(sx,z):
	return sx * z

def confInt(x,e):
	print 'Your CI is' + '[' + str(x-e) + ', ' + str(x+e) + '].'

# Main
def main():
	n = int(raw_input('Enter your sample size: '))
	x = float(raw_input('Enter your mean: '))
	s = float(raw_input('Enter your standard deviation: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	ci = ci/100

	confInt(x,(std_err(sampleStdD(n,s),two_zs(ci))))

main()
