import math


def position(x1,x2,y1,y2):
	dx=x2-x1
	dy=y2-y1;
	l=math.sqrt(dx**2+dy**2)
	return l;

x1=raw_input("x1 : \n")
x2=raw_input("x2 : \n")
y1=raw_input("y1 : \n")
y2=raw_input("y2 : \n")
x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)
print position(x1,x2,y1,y2);
