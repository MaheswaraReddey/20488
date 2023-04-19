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


a=int(input())
b=int(input())
c=int(input())
temp1=a
temp2=b
temp3=c
if(a>b):
  if(a>c):
    a=temp3
    if(b>c):
     b=temp2
     c=temp1
    else:
     b=temp1
     c=temp2
else:
   if(b>c):
    if(a>c):
      a=temp3
      b=temp1
      c=temp2
    else:
      a=temp1
      b=temp3
      c=temp2
print(a,b,c)    


a=0
b=1
n=int(input("Enter the number"))
print(a,b,end=" ")
if(n<=2):
    print("Enter a valid number")
else:
    for i in range(3,n+1):
     c=a+b
     a=b
     b=c
     print(c,end=" ")

