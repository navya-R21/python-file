#print statement
print(" Its my assignment Navya!!")

#Numeric data_type
#integer using variables & with type() method
a=10
b=5
print(a,b)
print(type(a))

#float with type() method
c=9.6
print(c)
print(type(c))

#complex with type() method
d=3+5j
print(d)
print(type(d))

#conversion frm one datatype to another
e=33.5
g=15
f=int(e)
print (f)

h=float(g)
print(h)

print(bin(g))
print(hex(10))
print(oct(g))

#arithmetic operations
#addition
print(2+3)
#subtraction
print(8-9)
#division
print(10/2)
#modulo
print(10%2)
#multiplication
print(4*4)
#power
print(6 ** 2)
print(9 ** 5)

#STRING
print("Barbie")
#Repition
i="Im a barbie doll!! "
print(i *2)
#to give the length of string
print(len(i))
#index
print(i[4])
print(i[3])
#slicing
j="i like sweets"
print(j[0:6])
print(j[6:])
print(j[0:10:3])
#reverse a string using slicing
print(j[: : -1])
#string methods
k='doll'
l='MAN'
print(k.upper())
print(l.lower())
#title is used to make the first letter of a word as a capital letter
print(k.title())
m="i'm am learning python"
print(m.title())
#to find the position of a string
print(m.find("python"))
#to find how many time does a letter occur in a word or in a string
print(k.count('l'))
print(m.count('i'))
#to replace a string
print(m.replace("python","testing"))
#strip- used to remove the spaces before or after a string or statement
n="    please help me       "
print(n.strip())
o="     i am scared   "
#used to remove left side spaces
print(o.lstrip())
#used to remove right side spaces
print(o.rstrip())
#print formatting
language="c++"
print(f'i love working with {language}')

p=5
q=0
mult=p*q
print(f'multiplication of {p} and {q} are {mult}')

#LISTS
r=['a','b','c','d','e']
print(r)
#list using index
print(r[2])
#list using slicing
print(r[0::2])
#Lists are Mutable
r[3]='p'
print(r)
#concatination
list_a=["its"]
list_b=["me!!"]
list_c= list_a+list_b
print(list_c)
#lists method
#append
list_a.append('hii')
print(list_a)
#pop
list_a.pop()
print(list_a)
#remove
list_c.remove('me!!')
print(list_c)
#delete
li=[0,3,5,7,9,1,2,6]
del (li[1])
print(li)
#sorting
li.sort()
print(li)
#reverse
li.reverse()
print(li)
#max and min
print(max(li))
print(min(li))
#to clear
lis=[5,6,7,9,0,2]
lis.clear()
print(lis)

#dictionaries
di={'john': 1,'kamal': 60, 'kiran': 100}
print(di)
#fetching a particular key
print(di['kamal'])
#to add key n value
di['dora']=0
print(di)
#change the value of existing key
di['john']=999
print(di)
#to fectch only keys and values separately and items
print(di.keys())
print(di.values())
print(di.items())
#mixed elements as values in dictionary
values={'name':'raj', 'scores':[10,100,200,257,999]}
print(values['scores'])


#Tuples
z=(1,2,8,9,0)
print(z)
#type
print(type(z))
#indexing and slicing
print(z[2])
print(z[:3])
print(z[0::3])
#mixed tuple
x=(1,21,14,18,'nis','nav')
print(x)

#small program to convert list to tuple
lst=[10,20,30]
print(type(lst))

tp=tuple(lst)
print(type(tp))
print(tp)


#SETS
se={1000,2090,3090}
print(se)
#doesnt allow duplicacy
dup={1,1,3,4,5,5,57,8,8,0}
print(dup)
#to add an element
se.add(500)
print(se)
#to update
se.update([80,90])
print(se)
#toremove
se.remove(2090)
print(se)

#boolean(true or false) with operators
#comparision operators
print(5>2)
print(5<2)
print(1>=2)
print(2>=2)
print(2!=2)
print(5==2)

#Logical operator
print(4>2 and 1<0)
print(2>=2 and 5>0)
print(5>2 or 1<0)
print(not 2>=2)















