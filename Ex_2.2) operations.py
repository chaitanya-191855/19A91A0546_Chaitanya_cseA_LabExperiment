
'''
2.2) Implement a python script add.py that takes 2 numbers
     as command line arguments and perform arithmetic operations
     on them
'''
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print('Sum of the two arguments is',(num1+num2))
print('Difference of the two arguments is',(num1-num2))
print('Product of the two arguments is',(num1*num2))
print('Division of the two arguments is',(num1//num2))
print('Modulus of the two arguments is',(num1%num2))

'''
Output:
C:\Users\Lenovo\OneDrive\Documents\Python Lab Programs>python add.py 10 5
Sum of the two arguments is 15
Difference of the two arguments is 5
Product of the two arguments is 50
Division of the two arguments is 2
Modulus of the two arguments is 0
'''
