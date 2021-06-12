"""
6.2) Implement a Python script to rotate list of elements towards right up to given number 
of times. 
Example: Input: [23,34,9,45,19] and 2 (Hint: 2 indicates No of times to rotate)
 Output: [45,19,23,34,9]
 """
n1=int(input("Enter range of a list : "))
list=[]
n=int(input("Enter no of rotations : "))
for i in range(n1):
    num=int(input())
    list.append(num)
print(list)
list = list[-n::] + list[:n-1:]
print(list)

"""
output:
	
Enter range of a list : 5
Enter no of rotations : 3
27
25
45
46
41
[27, 25, 45, 46, 41]
[45, 46, 41, 27, 25]

[Program finished]
"""