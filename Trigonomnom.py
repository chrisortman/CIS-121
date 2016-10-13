import math # MATH SON!
# ...
def sqrt(x): # Not that useful...
    return math.sqrt(x) # Ehh, I could've used this...
# ...
def sin(x): # This uses the imported math library to calculate the sine.
    return math.sin(x * 6.28318530718) # This uses tau to smooth out radians
# Watch the night go up in smoke!
def graph(x): # Rock on!
    print x, sin(x) # Rock on!
# ...
the_funk = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]

graph(the_funk.index(0))
graph(the_funk.index(1))
graph(the_funk.index(1))
graph(the_funk.index(0.375))
graph(the_funk.index(0.5))
graph(the_funk.index(0.625))
graph(the_funk.index(0.75))
graph(the_funk.index(0.875))
graph(the_funk.index(1))

# Whatddya know! Doesn't wanna work!

for x in [1, 3, 5]:
    print x
