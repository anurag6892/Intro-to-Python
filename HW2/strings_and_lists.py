# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
# print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
# print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
    cum_sum = [0]*len(number_list)
    total = 0
    for i in range(len(number_list)):
        total += number_list[i]
        cum_sum[i] = total
    
    ##### YOUR CODE HERE #####
    return cum_sum

# Test Cases
##### YOUR CODE HERE #####
# print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])

# **********  Exercise 2.8 **********

#def report_card():
    ##### YOUR CODE HERE #####
    

# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    ##### YOUR CODE HERE #####
    return "Not Implemented Yet"    

# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####
print [x**3 for x in range(11)]
print [i+j for i in ['h','t'] for j in ['h','t']]
a = "Hello"
Vowels = ['a', 'e', 'i', 'o', 'u']
print [x for x in a if (x in Vowels)]
print [x+y for x in [10,20,30] for y in [1,2,3]]
        

# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
