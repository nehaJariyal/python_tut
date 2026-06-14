# recursion is a programming technique where a function calls itself in order to solve a problem.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   
    
print(factorial(5)) # Output: 120

#  base case is the condition under which the recursion stops. It is a simple case that can be solved directly without further recursion. In the factorial function, the base case is when n is equal to 0, at which point the function returns 1.

def show_numbers(n):
    if n == 0:
        return
    print(n)
    show_numbers(n-1)
    print("end of function call for n =")

show_numbers(5) # Output: 5 4 3 2 1
print("end of function call for n = 1")