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
