def abcd(dict):
	a2030={'30s':[],'20s':[]}
	
	for name in dict:
		if(dict[name]>=20 and dict[name]<30):
			a2030['20s'].append(name)
		elif(dict[name]>=30 and dict[name]<40):
			a2030['30s'].append(name)

	return a2030

#2
member_info = {'minsu' : 23 , 'jisu':33 , 'john' : 21 , 'david' : 33, 'jisu' : 21, 'hary':36, 'messi' :33, 'ronaldo' : 27}

print abcd(member_info)
