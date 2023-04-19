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
