import pdb

a=[]

for value in range(7):
	if( value%2==0):
		a.append(value)
		pdb.set_trace()


for value in range(4):
	print("%d th value of list 'a' is %d"%(value,a[value]))