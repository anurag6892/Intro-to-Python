

a_list = [1, 3.0, 'a', 2, 3, 4.5]
#print [x for x in a_list if isinstance(x,int)]

#print [(x,y) for x in range(-5, 6, 1) for y in range(0, 11, 1) if y == x**2 + 1]

print [(x,y) for x in range(-5, 6, 1) for y in range(-5, 6, 1) if x**2 + y**2 == 25]
