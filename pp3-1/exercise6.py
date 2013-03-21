

str=raw_input("input String : ")

length=len(str)

half_length=length/2

compare=True

for i in range(0,half_length):
    if(str[i]!=str[length-1-i]):
        compare=False;
        break;


if(compare):
    print("same");
else:
    print("different");        
