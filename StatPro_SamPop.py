'''
This program calculates the necessary
sample population size for a desired
margin of error and level of confidence
given a known std.d. and mean.
Inputs are error, std. d., x, Con Lvl.  
'''
import math as m

def s_Pop(z,e,s):
	return (z*s/e)**2
	
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
	

# Main
def main():
	e = float(raw_input('Enter your margin of error:'))
	s = float(raw_input('Enter your standard deviation: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	ci = ci/100	

	print''
	print 'Your sample size must be at least: ' + str(m.ceil(s_Pop(two_zs(ci),e,s)))

main()