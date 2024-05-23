print("hi")

x=5
print(x)

#print(y)

import os
print(os.getcwd()) #function
import sys
print(sys.version) # variable

import main2
main2.fun1()

from importlib import reload
reload(main2)