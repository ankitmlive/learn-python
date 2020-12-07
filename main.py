"""""""""""""""""""""""""""""""""""""
""" Leap Year Check in Python """""""
"""""""""""""""""""""""""""""""""""""

year = 1992
def is_leap(year):
    leap = False
    if year%4 is 0:
        if year%100 is 0:
            if year%400 is 0:
                leap = True
            else:
            	leap = False
        else:
        	leap = True
    else:
        leap = False
    return leap
    
x = is_leap(year)
print(x)

""""""""""""""""""""""""""""""""""""""""""""""
""""    Cube Volume where n is len       """""
"""" Volume = length x width x height    """""
""""""""""""""""""""""""""""""""""""""""""""""

n = 3
def cube(n):
	return n**3
x = cube(n)
print(x)

## Result : 27

"""""""""""""""""""""""""""""""""""""""""""""""
"""" List Comprehensions 
"""" creating a list with prev. cube function
"""""""""""""""""""""""""""""""""""""""""""""""

xList = range(1,11)
x = [cube(x) for x in xList] 
print(x)

# Result : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

## EXAMPLE - 2

print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
# This code is equvalent to :
results = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        results.append([x, y])

print(results)

Result : [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]] -- for both case
