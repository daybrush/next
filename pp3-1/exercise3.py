
def haha(a):
	if(a>0 and a<10):
		return a+10
	elif(a>10 and a<100):
		return a*0.1
	else:
		return False

a=raw_input("input number\n")
a=int(a);
print haha(a);
