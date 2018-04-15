"""This code will print all Built_in python function (sorted by alphabet)"""
import os,sys

list_of_functions=[]
for item in dir(__builtins__):
        try:
                obj=str(type(eval(item)))
                if obj.find("builtin_function_or_method"):
                        if not item[0].isupper()and item[0]!= '_':
                                list_of_functions.append(item)
        except:
                pass

print("Python {}, has {} builtin function.\n".format(sys.version.split(' ')[0],len(list_of_functions)))
i=1
for function in list_of_functions:
      print("{}: {} ".format(i,function))
      i+=1
