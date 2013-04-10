dic1={'minju':53,'dayounggle':193,'jinwoo':12,'stlk':25,'cyk':20}

#[] -> list
#dict() -> define dictionary  

dic2=dict();
#dic2['20s']=[]#20s -> define list
#dic2['30s']=[]#30s -> define list



for i in dic1:
	dae=dic1[i]/10*10;

	if not str(dae)+'s' in dic2:
		dic2[str(dae)+'s']=[];

	
	dic2[str(dae)+'s'].append(i);

print dic2;


'''
aasas
aasasasas
asas``
'''
