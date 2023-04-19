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