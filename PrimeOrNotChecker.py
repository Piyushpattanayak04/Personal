n= int(input("Enter Number : "))
flag =0
for i in range (2,n):
     if n%i == 0:
        flag =1

if flag == 0:
   print("Prime")
else :
   print("Not Prime")
