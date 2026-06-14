# set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# set is denoted by curly braces {}
# set is a built in data type that store set of value
# set is a collection of data which is unordered and unchangeable       

set1 = {1, 2, 3, 4, 5}
print(set1) 
 #  methods of set
set2 = {1, 2, 3, 4, 5}
set2.add(6) # add element to the set
print(set2) 
set3 = {1, 2, 3, 4, 5}
set3.remove(3) # remove element from the set
print(set3) 
set4 = {1, 2, 3, 4, 5}
set4.discard(4) # remove element from the set   
print(set4)

set5 = {1, 2, 3, 4, 5}
set5.clear() # remove all elements from the set
print(set5) 

set6 = {1, 2, 3, 4, 5}
set6.pop() # remove random element from the set
print(set6)

set7 = {1, 2, 3, 4, 5}
set7.update({6, 7, 8}) # add multiple elements to the set
print(set7) 

set8 = {1, 2, 3, 4, 5}
set8.union({6, 7, 8}) # return a new set that is the union of two sets
print(set8.union({6, 7, 8}))    
