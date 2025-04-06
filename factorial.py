#Write a function to compute the factorial of a number using recursion
#recursion
def factorial_num(n):
    fac=1
    if n==0 or n==1:
       return 1 
    else:
        return n*factorial_num(n-1)

print(factorial_num(5))


#without recursion
def factorial_num(n):
    fac=1
    if n==0 or n==1:
        return fac
    else:
        for i in range(2,n+1):
            fac=i*fac
        return fac
print(factorial_num(5))
