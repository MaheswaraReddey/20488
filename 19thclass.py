n=5
for i in range(1,n+1):
 for j in range(1,i+1):
   print(i,end="")
 print("\n")

num=int(input("Enter a number :"))
rev=0
rem=new=num
while(num!=0):
   rem=num%10
   rev=rev*10+rem
   num=num//10
if(new==rev):
  print("Given number is a Palindrome")
else:
  print("Given number is not a Palindrome")


num=int(input("Enter a number :"))
newnum=num
rem=0
sum=0
count=len(str(num))
while(num!=0):
 rem=num%10
 sum=sum+rem**count
 num=num//10
if(newnum==sum):
  print("An Armstrong Number")
else:
  print("Not an Armstrong Number")



x=int(input("Enter 1-triangle , 2-square , 3-rectangle "))
if(x==1):
    a=int(input("Base="))
    b=int(input("Height="))
    print("Area of triangle is ",0.5*a*b)
if(x==2):
    a=int(input("Side="))
    print("Area of square is",a**2)
if(x==3):
    a=int(input("Length="))
    b=int(input("Breadth="))
    print("Area of rectangle is ",a*b)



