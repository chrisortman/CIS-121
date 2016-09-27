def zero():
    print ""

def one():
    print ""
    
# data function information

# funcs is """like""" a matrix of """functions"""

# def is like a function
    
funcs = {
        'circle' : { 'area' : calc_circle_area, 'draw' : draw_circle_area},
        'square' : one,
        2 : two
        }
        
# funcs is like "procedural generation"

# Work for September 20th, 2016
def make_student(name, age):
    return {'name' : name, 'age' : age}.

# bryant = {'name' : 'Bryant', 'age' : 17}
# bruno = {'name' : 'Bruno', 'age' : 17}
bryant = make_student("Bryant", 17)
bruno = make_student("Bruno", 17)

# I didn't quite understand the purpose of dictionaries and the def function,
# but now I remember the ultimate goal of coding: save them lines, playa.

students = [bryant, bruno]

def calc_year_born(age):
    return 1998
    
for s in students:
    year_born = calc_year_born(s['age'])
    print "%s was born in %d" % (s['name'], year_born )
    
# What kind of geometric crap did chris just do?