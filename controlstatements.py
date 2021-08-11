#Control statements
#COnditional
#if
if(1>0):
    print("correct")
#comparing
if (100>90):
    print("the input is right")

#ifelse
if(1>0):
    print("have entered the right values")
else:
    print("wrong values")
#even or odd
x=int(input("enter a number"))
if x%2 ==0:
    print(x,"is even")
else:
    print(x, "is odd")

#ifelse ladder
name="can"
if name=="van":
    print("wait")
elif name=="man":
    print("do the work")
else:
    print("take a can of coke")
#to check the number is equal to zero or even or odd
y= int(input("enter a number"))
if y==0:
    print(y,"is zero")
elif y%2==0:
    print(y,"is even")
else:
    print(y,"is odd")

#Looping Statements
#while
a=0
while a<5:
    print(a)
    a=a+1
#displaying numbers from 1 to 20
b=1
while(b<=20):
    print(b)
    b+=1

#odd number between c & d
c=int(input("enter lower number"))
d=int(input("enter higher number"))
i=c
if i%2==0:
   i=c+1
while i<=d:
      print(i)
      i+=2

#for loop
#to print the numbers that are in list
list_num=[1,2,3,4,5]
for item in (list_num):
    print(item)
print("all items are printed")

#product of a number in list
lit=[1,2,3,5]
prod=1
for i in lit:
    prod *=i
print(prod)

#sum of number in list
lit=[1,2,3,5]
sum=0
for i in lit:
    sum=sum+i
print(sum)


#to print hello 3 times
lis=[1,2,3]
for item in lis:
    print('hello')

#to check even or odd using for loop
my=[1,2,3,4,5,6,7,8,9,0]
for num in my:
    if num%2==0:
        print(f'{num}is even')
    else:
        print(f'{num}is odd')

#tuple unpacking using for loop
un=[(1,4), (3,4),(7,8),(5,0)]
for item in un:
    print(item)

#to print only a column items
for a,b in un:
    print(a)

#unpacking using for loop in dictionary
dict={'key': 5 ,'lock':10}
for x in dict:
    print(x)
#print multiplication table
n=int(input("enter a number"))
for i in range(1,11):
    print(n ,'X',i,'='  ,i*n)

#break
s=[1,3,6,8]
for i in s:
    if(i==6):
        break
    print(i)
#pass
s=[1,3,6,8]
for i in s:
    if(i==6):
        pass

#continue
con=[1,2,3,4,5]
for num in con:
    if num ==4:
        continue
    print(num)

#range
for num in range(10):
    print(num)

for k in range(2,10):
    print(k)

for l in range(0,11,3):
    print(l)
#to get each element
msg="kishan"
for char in msg:
    print(char)

#to get index of each letter
msg="killer"
index_count=0
for char in msg:
    print(f'at index {index_count}is {char}')
    index_count=index_count+1

#enumerate
line="saraswathi"
for char in enumerate(line):
    print(char)

#zip function
mine=[1,2,3,4]
urs=['a','v','l']
for item in zip(mine,urs):
    print(item)

#zip function to get the items separately
mine=[1,2,3,4]
urs=['a','v','l']
for a,b in zip(mine,urs):
    print(a)
    print(b)

#in operator
print(5 in[1,2,3])
print('n' in['a','b','n'])

#functions
#shuffle
import random
l=list(range(5))
print(l)
random.shuffle(l)
print(l)

#randint
import random
print(random.randint(1,100))

#input function
print(input("what is your name?"))



