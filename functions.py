#creating  a list with for loop and append method
a="bye"
lis=[ ]
for i in a:
    lis.append(i)
print(lis)
#creating  a list with for loop and append method
name='nisha'
list= [char for char in name]
print(list)

#list comprehend
# to get square
sq=[num**2 for num in range(0,5)]
print(sq)
#to get only even numbers
eve=[num for num in range(0,11) if num %2==0]
print(eve)
#to get only even numbers with square
eve=[num**2 for num in range(0,11) if num %2==0]
print(eve)
#list comprehension with nested for loop
for x in [1,2,3]:
    for y in[10,100,1000]:
        print(x*y)

ne=[x*y for x in[5,6,7] for y in[10,10,199]]
print(ne)

#functions
#define a method using def keyword
def namefun_ction():
    print("i am doing my assignment")
print(namefun_ction())


#pass parameter to a method
def name(name):
    name('jeeva')
print(f'hello{name}')


#return
def sum_numb(a,b):
    return a+b
lis=sum_numb(10,8)
print(lis)

#function within a function
def display(name):
  def mess():
        return 'hello'
        result= mess()+name
        return result
        display('Nithin')
print(display(name))

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
z=list(range(5))
print(z)
random.shuffle(z)
print(z)

#randint
import random
print(random.randint(1,100))

#input function
print(input("what is your name?"))

#to find the emp where working is more
#wrk_hr=[('san',200),('can',4000),('man',2)]
#def emp_max(wrk_hr):
#    cur_max_hr=0
#    emp_name=''

#    for employee,hours in wrk_hr:
#print(emp_max(wrk_hr))

