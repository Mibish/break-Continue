#1
'''for i in range(1,11):
    print("softwarica")'''

#2
'''a=[1,2,3]
b=0
for i in a:
    b=i+b
print(b)'''

#3
'''ch='character'
for i in ch:
    print(i)'''

#4
'''list=[1,"a","c",2,3,4]
for i in list:
    if type(i)==int:
        print(i)'''

#5
'''list=[4,5,3,2]
b=1
for i in list:
    b=b*i
print(b)'''

#6
'''a=int(input('Enter a number:'))
for i in range(1,11):
    print(a,'x',i,'=',a*i)'''

#7
'''list=[1,2,3,4]
for i in range(3,-1,-1):
    print(list[i])'''    

#8
'''list=[1,2,3,4]
for i in range(0,4):
    print(list[i]+1)'''

#9
'''list=[1,2,3,4]
for i in list:
    if i==1 or i==4:
        print(i)'''

#10
'''lst=[1,2,3,4]
for i in lst:
    if i==1 or i==2 or i==4:
        print(i)'''

#11
'''l=[1,2,3,4]
for i in l:
    if i==3:
      l[2]=2
    if i==2:
        l[1]="a"
print(l)'''    
    
#12
'''l=[1,2,3,4,5]
for i in l:
    if i%2==0:
        print(i,"is even")
    elif i%2!=0:
        print(i,"is odd")'''
    
#13  
'''l=[1,2,3,"d",4,5,"a"]
for i in l:
    if isinstance(i,int):
        print("number:",i)
    else: print("String:",i)'''

#14
'''numbers=[]
strings=[]
l=[1,2,3,4,"a","b"]
for i in l:
    if isinstance(i,int):
        numbers.append(i)
    elif isinstance(i,str):
        strings.append(i)
print("Numbers:",numbers)
print("string:",strings)'''

#15
'''l=str(input("Enter any character:"))
b=0
c=0
d=0
for i in l:
    if i.isdigit():
        b+=1
    elif i.isalpha():
        c+=1
    elif i==' ':
        d+=1
print("number of digit:",b)
print("number of character:",c)
print("number of space:",d)'''

#16
'''us=input("Enter username:")
ps=input("Enter password:")
if us=='softwarica' and ps=='admin':
    print("Correct username and password")
elif us!='softwrica' and ps=='admin':
    print("Username is invalid")
elif us=='softwarica' and ps!='admin':
    print("Password is invalid")
else:
    print("Both username and password is invalid")'''

#17
'''num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
elif num%2!=0:
    print("Odd")'''

#18
'''num=int(input("Enter a number:"))
b=1
for i in range(num,0,-1):
    b*=i
print(b)'''

#19
'''for i in range(1,9,1):
    print("Multiplication table for",i)
    for j in range(1,11):
        print(i,"x",j,"=",j*i)'''

#20
'''lst=[1,2,3,4]
for i in lst:
    if i==1 or i==2:
        print(i)'''

#21
'''l=int(input("Enter number:"))
b=0
if l%2==0:
    for i in range(l-1,0,-2):
        b+=i
else:
    for i in range(l,0,-2):
        b+=i
print(b)'''

#22
'''l=int(input("Enter number:"))
b=0
if l%2==0:
    for i in range(l,0,-2):
        b+=i
else:
    for i in range(l-1,0,-2):
        b+=i
print(b)'''

#23
'''l=input("enter a statement:")
b=0
for i in l:
    if i==" ":
        b+=1
print(b)'''

#24
'''l=[1,2,3,4]
upl=[]
b=1
for i in l:
    b=i**3
    upl.append(b)
print(upl)'''

#25
'''a="programming"
for i in range(10,-1,-1):
    print(a[i],end='')'''

#26
'''for i in range(1,51):
    print(i)
    if i==7:
        break'''

#27
'''m=input("Enter any charcter")
for i in m:
    if i.isalpha():
        print(i)'''

#28
'''list=["ram","shyam",1,2]
for i in list:
    if isinstance(i,str):
        print("Hello!",i)'''

#29
'''a=["ram","shyam"]
for i in a:
    print("Dr.",i)'''

#30
'''a=[2,3,4,5]
b=[]
for i in a:
    b.append(i**2)
print(b)'''

#31
'''lst1=[111,32,-9,-45,-17,9,85,-10]
plst=[]
nlst=[]
for i in lst1:
    if i>0:
        plst.append(i)
    else:
        nlst.append(i)
print("Positive:",plst)
print("Negative:",nlst)'''

#32
'''list=[0,1,2,3,4,5,6]
for i in list:
    if i==3 or i==6:
        continue
    print(i)'''

#33
'''a=[1,"mibish",3.14,True]
b=[]
for i in a:
    b.append(type(i))
print(b)'''

#34
'''a= [1, "hello", 3.14, True]
b= []
for i in a:
    b.append(type(i))
else:
    print("Done")
print(b)'''

#35
'''for i in range(105,6,-7):
    print(i)'''

#36
'''string="py;th*on!;py*t*h:o!n"
for i in string:
    if i.isalpha():
        print(i,end='')'''

#37
'''print("Natural number upto 1000")
a=0
b=0
for i in range(1,1000,1):
    if i%2==0:
        b+=1
    elif i%2!=0:
        a+=1
print("Total even number:",b)
print("Total odd number:",a)'''

#38
'''b=0
for i in range(3,100,1):
    if i%3==0 or i%5==0:
        b+=i
print(b)'''

#39 
'''b=0
c=0
for i in range(1,101):
    if i%2==0:
        b+=i
    elif i%2!=0:
        c+=i
print("Sum of even numbers:",b)
print("Sum of odd numbers:",c)'''

#40
'''a=int(input("Enter a number:"))
b=str(a)
if b==b[::-1]:
    print(f"{a} is palindrome")
else: 
    print(f"{a} is not palindrome")'''

#41
'''a=int(input("Enter a number:"))
b=str(a)
d=len(b)
c=0
for i in b:
    c+=int(i)**d
if c==a:print(f"{a} is armstrong number")
else:print(f"{a} is not armstrong number")'''

#42
'''a=input("Enetr a character:")
for i in a:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=="u":
        continue
    print(i,end='')'''

#43
'''a=int(input("Enter a number:"))
b=0
for i in range(1,a):
    if a%i==0:
        b+=i
if a==b:
    print("it is perfect number")
else: print("it is not perfect number")'''

#44
'''a=[1,2,3,4,5]
b=[3,4,5,6,7]
for i in a:
    for j in b:
        if i==j:
            print(i)'''

#45
'''a=int(input("Enter a number:"))
for i in range(2,a):
    if a%i==0:
       print("It is not prime number")
       break
    else: print("It is prime number")   
    break'''        