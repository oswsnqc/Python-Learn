from sys import argv

script, name = argv

numbers = []

ppp = name

def loop(a):
	i = 0
	while i < a:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i
	return numbers
	
loop(ppp)
print name