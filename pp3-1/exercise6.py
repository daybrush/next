

str=raw_input("input String : ")

length=len(str)

half_length=length/2#half length

compare = True

for i in range(0,half_length):
	if(str[i]!=str[length -1-i]): # 0 ~ half  half ~ length compare
		compare=False
		break


if(compare == True):
    print("same")
elif(compare == False):
    print("different")       
