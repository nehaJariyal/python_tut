# funxtion is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# paramiter  : parameter is a variable that is used in the function definition to represent the value that will be passed to the function when it is called. It acts as a placeholder for the actual value that will be provided when the function is invoked.
# argument : An argument is the actual value that is passed to a function when it is called. It is the data that is provided to the function's parameters. When you call a function, you can provide arguments that correspond to the parameters defined in the function's signature. The arguments can be of various types, such as numbers, strings, lists, or even other functions, depending on what the function expects as input.
# return statement : The return statement is used in a function to specify the value that should be returned to the caller when the function is executed. It allows you to send a result back from the function to the code that called it. When a return statement is encountered, the function immediately exits and returns the specified value. If no return statement is present, the function will return None by default.

def add(a,b):
 sum = a + b 
 return sum
print(add(5, 3))

# default parameter : A default parameter is a parameter in a function definition that has a default value assigned to it. If the caller does not provide a value for that parameter when calling the function, the default value will be used instead. This allows the function to be called with fewer arguments than the number of parameters defined, providing flexibility in how the function can be used. Default parameters are defined by assigning a value to the parameter in the function definition, like this: def my_function(param1, param2=default_value):

def greet(name, greeting="Hello"):#   default parameter is always defined after the non default parameter
    return f"{greeting}, {name}!"       
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!


citis = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
def print_cities(cities):
    for city in cities:
        print(city)
print_cities(citis)

