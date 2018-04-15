import sys
import math
import cmath

# abs_my() ==> abs() in python
# the absolute value of a number is how far it is from zero .
# this function takes as input integer ,float ,or complex number
# and return absolute value for integer ,float
# or magnitude for complex number.
def abs_my(x):
    message="int ,float ,complex numbers "
    try:
        if isinstance(x,int):
            return -x if x < 0 else x
        elif isinstance(x,float):
            return -x if x < 0 else x
        elif isinstance(x,complex):
            magnitude=cmath.sqrt(x*x.conjugate())
            return magnitude.real
        else:
            print(message)
        
    except TypeError as error:
        print(message)
        print(error)

# test function for abs_my , it takes to lists as input
# input=[ values to test ]
# output=[ expected values ]
# func= abs_my
def test_abs_my(input,output,func):
    for a,b in zip(input,output):
        test_result=func(a)
        if test_result == b:
            print("input: {}\toutput: {}\t ==> TEST PASS ./".format(a,b,test_result))
        else:
            print("input: {}\toutput: {}\t ==> TEST FAIL X".format(a,b,test_result))

#test_abs_my([-1,-4.0,4j],[4,4.0,4.0],abs_my)

