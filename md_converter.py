file = open('solution.py', 'r')

a=''
for line in file:
	a += line
 
a = a.split('# ---end----')
print(a)
ouf = open("out.txt", 'w')
ouf.write(a[-1])