# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(a,b):
    c = []
    for elem in a:
        if elem in b:
            c.append(elem)
    return c

# Test Cases for Exercise 3.1
# print list_intersection([1, 3, 5], [5, 3, 1])
# print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
# printlist_intersection([2, 3], [3, 3, 3, 2, 10])
# printlist_intersection([2, 4, 6], [1, 3, 5])

# **********  Exercise 3.2 **********

import math
# Define your function here
def ball_collide(ball1, ball2):
    distance = math.sqrt((ball1[0]-ball2[0])**2+(ball1[1]-ball2[1])**2)
    return distance <= ball1[2] + ball2[2]

# Test Cases for Exercise 3.2
# print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
# print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
# print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    return "Not Yet Implemented"

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    ##### YOUR CODE HERE #####
    return "Not Yet Implemented"

# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####

# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    for i in range(len(l2)):
        if l2[i] in comb_dict.keys():
            comb_dict[l2[i]].append(l1[i])
        else:
            comb_dict[l2[i]] = [l1[i]]  
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) # Finish this line...

def people(age):
    if age in combined_dict.keys():
        return combined_dict[age]
    else:
        return []

# Test Cases for Exercise 3.4 (all should be True)
#print 'Dan' in people(18) and 'Cathy' in people(18)
#print 'Ed' in people(19) and 'Helen' in people(19) and\
#       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
#print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
#print people(21) ==   ['Bob']
#print people(22) ==   ['Kelly']
#print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    months_dict = {"January":11,"February":12,"March":1,"April":2,"May":3,"June":4,"July":5,
                   "August":6,"September":7,"October":8,"November":9,"December":10}

    A = months_dict[month]
    B = day
    C = year%100
    D = year/100
    if A > 10:
        C=C-1
    W = (13*A - 1)/5 
    X = C/4 
    Y = D/4 
    Z = W + X + Y + B + C - 2*D 
    R = Z%7
    
    days_list= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_list[R]

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True

