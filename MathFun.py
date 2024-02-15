"""
This is math library fun in python !
Anything in between tripple quotations are comments. Please read them.

pi
Return the value of pi: 3.141592
E
Return the value of natural base e. e is 0.718282
tau
Returns the value of tau. tau = 6.283185
inf
Returns the infinite
nan
Not a number type.
ceil(x)
Return the Ceiling value. It is the smallest integer, greater or equal to the number x.
copysign(x, y)
It returns the number x and copy the sign of y to x.
fabs(x)
Returns the absolute value of x.
factorial(x)
Returns factorial of x. where x ≥ 0
floor(x)
Return the Floor value. It is the largest integer, less or equal to the number x.
fsum(iterable)
Find sum of the elements in an iterable object
gcd(x, y)
Returns the Greatest Common Divisor of x and y
isfinite(x)
Checks whether x is neither an infinity nor nan.
isinf(x)
Checks whether x is infinity
isnan(x)
Checks whether x is not a number.
remainder(x, y)
Find remainder after dividing x by y.

pow(x, y)
Return the x to the power y value.
sqrt(x)
Finds the square root of x
exp(x)
Finds xe, where e = 2.718281
log(x[, base])
Returns the Log of x, where base is given. The default base is e
log2(x)
Returns the Log of x, where base is 2
log10(x)
Returns the Log of x, where base is 10
sin(x)
Return the sine of x in radians
cos(x)
Return the cosine of x in radians
tan(x)
Return the tangent of x in radians
asin(x)
This is the inverse operation of the sine, there are acos, atan also.
degrees(x)
Convert angle x from radian to degrees
radians(x)
Convert angle x from degrees to radian

"""

#Import math library
import math
#Floor and Ceiling
print('The Floor and Ceiling value of 9.45 are:' + str(math.ceil(9.45)) + ', ' + str(math.floor(9.45)))

#Copysign
x = 94
y = -27
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

#Absolute
print('Absolute value of -94 and 54 are: ' + str(math.fabs(-94)) + ', ' + str(math.fabs(54)))

#Fsum & gcd
my_list = [12, 9.25, 89, 3.02, -75.23, -7.2, 6.3]
print('Sum of the elements of the list: ' + str(math.fsum(my_list)))
print('The GCD of 24 and 56 : ' + str(math.gcd(24, 48)))

#isnan
x = float('nan')
if math.isnan(x):
   print('It is not a number')
   x = float('inf')

#isinf
y = 54
if math.isinf(x):
   print('It is Infinity')
      #x is not a finite number
print(math.isfinite(x))
   #y is a finite number
print(math.isfinite(y))

print("The value of 2^5: " + str(math.pow(2, 5)))
print("Square root of 625: " + str(math.sqrt(625)))
print("The value of 5^e: " + str(math.exp(5)))
print("The value of log(625), base 5: " + str(math.log(625, 5)))
print("The value of log(1024), base 10: " + str(math.log10(1024)))
print("The value of log(1024), base 2: " + str(math.log2(1024)))

print("The value of sin(45 degree): " + str(math.sin(math.radians(45))))
print('The value of cos(pi): ' + str(math.cos(math.pi)))
print("The value of tan(45 degree): " + str(math.tan(math.pi/2)))
print("the angle of sin(0.9876):" + str(math.degrees(math.sin(0.9876))))