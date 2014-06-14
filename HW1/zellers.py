# Anurag Mukkara
# 11 June, 2014
# zellers.py

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
print "Enter your date of birth: "
month = input("Month? ")
date = raw_input("Date? ")
year = raw_input("Year? ")

A = month
B = int(date)
C = int(year)%100
D = int(year)/100
if(A>10):
    C = C - 1
    
W = (13*A - 1) / 5 
X = C / 4 
Y = D / 4 
Z = W + X + Y + B + C - 2*D 
R = Z % 7

a= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print first_name, "was born on", a[R]

