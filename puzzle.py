#/usr/bin/python
# _*_ coding:utf-8 _*_
from random import randint

r=range(9);
rc=range(9);
a=0;


while (a<9):
	b=randint(0,8);
	if(r[b]!=-1):
		r[b]=-1;
		rc[a]=b;
		a=a+1;

puzzle=[rc[0:3],rc[3:6],rc[6:9]];

ok=0;
num=0;

ar1=0;
ar2=0;
for i in range(0,3):
	for j in range(0,3):
		if(puzzle[i][j]==0):
			ar1=i;
			ar2=j;

def changes(a1,a2,b1,b2):
	
	t=puzzle[a1+b1][a2+b2];
	puzzle[a1+b1][a2+b2]=puzzle[a1][a2];
	puzzle[a1][a2]=t;
	

while(ok==0):
	num=num+1;

	print("num : "+str(num));
	print(puzzle[0]);
	print(puzzle[1]);
	print(puzzle[2]);
	
	b=raw_input("왼쪽 a 오른쪽 d 위쪽 w 아래쪽 s : ");
	
	
	err=1;
	if(b=="a" and ar2!=0 ):
		
		changes(ar1,ar2,0,-1);
		ar1=ar1+0;
		ar2=ar2-1;
		err=0;
	elif(b=="d" and ar2!=2):
		changes(ar1,ar2,0,+1);
		ar1=ar1+0;
		ar2=ar2+1;
		err=0;
	elif(b=='w' and ar1!=0):
		changes(ar1,ar2,-1,0);
		ar1=ar1-1;
		ar2=ar2+0;
		err=0;
	elif(b=='s' and ar1!=2):
		changes(ar1,ar2,+1,0);
		ar1=ar1+1;
		ar2=ar2+0;
		err=0;

	if(err==1):
		print("Err");
		num=num-1;

		suc=0;
		for i in range(0,3):
			for j in range(0,3):
				if(i==2 and j==2):
					if(puzzle[i][j]==0):
						suc=suc+1;
				else:
					if(puzzle[i][j]==i*3+j+1):
						suc=suc+1;

		if(suc==9):
			ok=1;
			print("end"+num);
