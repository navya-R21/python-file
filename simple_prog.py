#avg of 3 numbers using split()
a,b,c=[int(x) for x in input("enter 3 digit number").split()]
average=(a+b+c)/3
print("Average:",average)

# Program to check if a number is prime or not

num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Python program to find the factorial of a number

num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# to swap two variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# find the largest number among the three input numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# Python Program to find the area of triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#to find si
def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100
    print('The Simple Interest is', si)
    return si
simple_interest(8, 6, 8)

#to check whether its leap yr or not
year = int(input("Please Enter the Year Number you wish: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is Leap Year" %year)
else:
    print("%d is Not Leap Year" %year)