# 1--->PROGRAM TO FIND THE GRADE OF A STUDENT
x=int(input("Enter the marks obtained"))
if(x>100):
 print("ERROR!Invalid marks")
elif(x>90 and x<100):
 print("A+ grade")
elif(x>80 and x<90):
 print("A grade")
elif(x>70 and x<80):
 print("B+ grade")
elif(x>60 and x<70):
 print("B grade")
elif(x>50 and x<60):
 print("C+ grade")
elif(x>40 and x<50):
 print("C grade")
else:
 print("F grade")

# 2--->PROGRAM TO FIND A LEAP YEAR OR NOT
x=int(input("Enter the year:"))
if(x%4==0 and x%100!=0):
 print(x,"is a leap year")
elif(x%400==0):
 print(x,"is a leap year")
else:
 print(x,"is not a leap year")



# 3---> PROGRAM TO FIND ODD OR EVEN OR ZERO
a=int(input("Enter the number:"))
if(a==0):
 print("Number is zero")
elif(a%2==0):
 print("Number is even")
else:
 print("Number is odd")

#4---> CALCULATOR TO PERFORM ARITHMETIC OPERATIONS
a=int(input("Enter the value,a="))
b=int(input("Enter the value,b="))
exp=input("Enter the operator symbol :")
if(exp=='+'):
 print("Result =",a+b)
elif(exp=='-'):
 print("Result =",a-b)
elif(exp=='*'):
 print("Result =",a*b)
elif(exp=='/'):
 print("Result =",a/b)
elif(exp=='%'):
 print("Result =",a%b)
else:
 print("Error!invalid Arithmetic Operator")





# 5--->PROGRAM TO CHECK STRENGTH OF A PASSWORD 
    # RULES: Atleast 1 lowercase alphabet
      #       Atleast 1 uppercase alphabet
       #      Contain more than 6 digits
        #     Atleast 1 special character(@, #, $, %, &)
         #    Length must be more than 8 characters
pw=input("Enter a password:")
count1=0
count2=0
count3=0
count4=0
if(len(pw)<=8):
 print("Password is too short!")
for i in pw:
  if(i.isupper()):
    count1=count1+1
  if(i.islower()):
    count2=count2+1
  if(i.isdigit()):
    count3=count3+1
  if(i=='@' or i=='#' or i=='$' or i=='%' or i=='&'):
   count4=count4+1   
if(count1==0):
     print("Password must contain atleast one uppercase alphabet")
if(count2==0):
     print("Password must contain atleast one lowercase alphabet")
if(count3<6):
     print("Password must contain more than 6 digits")
if(count4==0):
     print("Password must contain atleast contain atleast one special character")
if(count1!=0 and count2!=0 and count3>6 and count4!=0):
  print("Password is strong !")