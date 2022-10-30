#string reversal
strr=str(input("enter the string"))
str2=""
a=len(strr)
for i in range(a-1,-1,-1):
    str2=str2+strr[i]
print(str2)
