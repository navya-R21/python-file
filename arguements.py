#arguements
#args
def int_sum(*args):
    return sum(args)
print (int_sum(1,2,3))

#kwargs
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun("Hi", first='i like', mid='chocolate', last='icecream')


#
kwargs={'fruit':'chicken','color':'red'}
print(kwargs['color'])
#map
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#filter
def filterdata(x):
    if x>5:
        return x
result = filter(filterdata,(1,2,6))
print(list(result))

#lamda
sq=lambda num: num ** 2
print(sq(2))

cube=lambda num: num ** 3
print(cube(4))

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

#default arguements
def sum_numb(a,b=10):
    return a+b
lis=sum_numb(18)
print(lis)

def avg(a=10,b=20):
    return(a+b)/2
print(avg(a=5))

