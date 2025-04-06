#How do you reverse a string in Python?
#using slicing
'''def rev(s):
    return s[::-1]
   
print(rev("Ashwini"))'''

#without using slicing

def reverse_str(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(reverse_str("Ashwini"))
