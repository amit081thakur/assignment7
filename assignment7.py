Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Q.1- Create a function to calculate the area of a circle by
>>> #taking radius from user.
>>>
>>>
>>> def area():
	for i in range(5):
		r = int(input("\n\n radius of circle:"))
		a = 22/7*r*r
		print("area of circle is:",a)

		
>>> area()


 radius of circle:2
area of circle is: 12.571428571428571


 radius of circle:3
area of circle is: 28.285714285714285


 radius of circle:7
area of circle is: 154.0


 radius of circle:0
area of circle is: 0.0


 radius of circle:8
area of circle is: 201.14285714285714
>>>
>>>
>>>
>>> #Q.2- Write a function “perfect()” that determines if parameter number
>>> #is a perfect number. Use this function in a program that determines and
>>> #prints all the perfect numbers between 1 and 1000.
>>>
>>>
>>> def div(x):
	return[ y for y in range(1,int(x/2)+1) if x%y==0]

>>> def perfect(a,b):
	return[ x for x in range(a,b+1) if sum(div(x))==x]

>>> print(perfect(1,1000))
[6, 28, 496]
>>>
>>>
>>>
>>> #Q.3- Print multiplication table of 12 using recursion.
>>>
>>>
>>> >>> def table(t = 0,counter = 0):
	if counter<11 & t!=0:
		counter += 1
		result = int(t*counter)
		print("{}*{} = {}".format(t,counter,result))
		table(t,counter)

		
>>> table(t=int(input("which table u want to see=")),counter=0)
which table u want to see=12
12*1 = 12
12*2 = 24
12*3 = 36
12*4 = 48
12*5 = 60
12*6 = 72
12*7 = 84
12*8 = 96
>>>
>>>
>>> #Q.4- Write a function to calculate power of a number raised to
>>> #other ( a^b ) using recursion. 
>>>
>>> def power(base,exp):
	if(exp==1):
		return(base);
	if(exp!=1):
		return(base*power(base,exp-1))

	
>>> base = int(input("enter base:"))
enter base:2
>>> exp = int(input("enter exponential value:"))
enter exponential value:4
>>> print("result:",power(base,exp))
result: 16
>>>
>>>
>>>
>>> #Q.5- Write a function to find factorial of a number but also
>>> #store the factorials calculated in a dictionary 
>>>
>>>
>>> a= int(input("enter the number:"))
enter the number:4
>>> def factorial(a):
	if a <= 1:
		return 1;
	else:
		return (a * factorial(a-1));

	
>>> factorial(a)
24
>>> factorial(5)
120
>>> factorial(8)
40320
>>> factorial(10)
3628800
>>> dict = {'factorial(4)': 24 ,'factorial(5)': 120, 'factorial(8)':40320,'factorial(10)':3628800}
>>> print(dict)
{'factorial(4)': 24, 'factorial(5)': 120, 'factorial(8)': 40320, 'factorial(10)': 3628800}
>>> 

