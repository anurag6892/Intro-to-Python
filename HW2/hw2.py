# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1


# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

def is_divisible(m, n):
    if (n==0):
        return True
    else:
        if (m%n == 0):
            return True
        else:
            return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####

def not_equal(a,b):
    if (a==b):
        return False
    else:
        return True
    
# Test cases for not_equal
##### YOUR CODE HERE #####

#print not_equal(3, 4)
#print not_equal(4, 4)
#print not_equal("Hello", "Hello")

# ********** Exercise 2.3 ********** 

import math

## 1 - multadd function
##### YOUR CODE HERE #####

def multadd(a, b, c):
    return a*b + c

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
#angle_test = math.sin(math.pi/4) + math.cos(math.pi/4)/2
#print "sin(pi/4) + cos(pi/4)/2 is:"
#print angle_test

#ceiling_test = math.ceil(276.0/19) + 2*math.log(12, 7)
#print "ceiling(276.0/19) + 2 log_7(12) is:"
#print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####

def yikes(x):
    return multadd(x, math.exp(-x), math.sqrt(1-math.exp(-x)))

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
