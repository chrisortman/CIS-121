from sys import exc_info
from subprocess import check_output, CalledProcessError, STDOUT
from glob import glob
from os import path
from os import devnull

FNULL = open(devnull, 'w')
EXPECTED = "----------SAY HI TO----------"

paths = glob("k*/")
for p in paths:
    k_number = path.dirname(p)
    assignment_file = path.join(p,'assignment06.py')
    file_exists = path.isfile(assignment_file)

    if file_exists:
        try:
            output = check_output(["python",assignment_file,"say_hi_to","-"], stderr=STDOUT)
            if output == EXPECTED or output.rstrip() == EXPECTED: #allow correctness with and without trailing newline
                print "%s --- CORRECT!" % k_number
            else:
                print "%s --- INCORRECT" % k_number
                print ">>>%r" % EXPECTED
                print "<<<%r" % output

        except CalledProcessError as e:
            print "%s --- INCORRECT:" % k_number
            print e.output
    else:
        print "%s --- No Assignment 06" % k_number

