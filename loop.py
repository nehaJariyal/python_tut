# loop  uses to repeat a block of code until a certain condition is met
# while loop is used to repeat a block of code until a certain condition is met
# for loop is used to iterate over a sequence (such as a list, tuple, or string)
# do while loop is used to execute a block of code at least once, and then repeat the loop as long as a condition is true
#  range() function is used to generate a sequence of numbers, which can be used in a for loop
# range(start, stop, step) start: the starting number of the sequence (inclusive), stop: the ending number of the sequence (exclusive), step: the increment between each number in the sequence (optional, default is 1)    



# i = 1
# while i < 5:
#     print(i)
#     i += 1

#     print("Looping through while loop")

# while True:
#     print("This is an infinite loop")
#     break


# while i<101:
#     print(i)
#     i+=1


# while i>0:
#     print(i)
#     i-=1

# n = 2
# while i <= 10:
#     print(n*i)
#     i += 1

# lit = [1,4,9,16,25,36,49,64,81,100]
# lit = ["1,4,","9,16,25","36,49,64,81,100"]
# i = 1
# while i < len(lit):
#     print(lit[i])
#     i += 1

# tup = [1,4,9,16,25,36,49,64,81,100,36]
# n = 36
# while i < len(tup):
#     if(tup[i] == n):
#         print("Found in index " ,  i)
#     else:   
#             print("Not Found")
         
#     print(tup[i])
#     i += 1
# # 
# while i<=10:
#      if (i%2 == 0):
#         i += 1
#         continue
#      print(i)
#      i += 1  

# lit = [1,4,9,16,25,36,49,64,81,100]
# for i in range(len(lit)):
#     print(lit[i])


# tup = (1,4,9,16,25,36,49,64,81,100,36)
# n = 36
# for i in range(len(tup)):
#     if(tup[i] == n):
#         print("Found in index ::::" ,  i)
#         break
#     else:   
#             print("Not Found")
         
    # print(tup[i])   

    # for el in range(1,11):
        
    #     print(el)

# n = int(input("Enter a number: "))
# for i in range(1,11):
        # print(n*i)
        
# for i in range(1,101):
    # print(i)
    
for i in range(100,0,-1):
    print(i)
    
for i in range(9):
    pass   # pass statement is used to indicate that a block of code is intentionally left empty, and it does nothing when executed. It is often used as a placeholder for code that will be added later, or to create a minimal implementation of a function or class.

print("This is a pass statement")

n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print("The sum is:", sum)   

# i = 1
# while i <= 10:
#     sum += i
#     i += 1
# print("The sum is:", sum)


i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1
print("The factorial is:", factorial)