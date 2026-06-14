# list   like a array of js  
# lis is a  built in data type that store set of value 
# it is mutable data type
# list is ordered collection of data
# it can store different data type value in a single list
# list is denoted by square brackets []
# list is a collection of data which is ordered and changeable

# mutable mean that we can change the value of list after it is created            list
# imutable mean that we cannot change the value of list after it is created        string   

marks = [45, 67, 89, 90, 78]
print(marks)
print(marks[0]) # access first element of the list
print(marks[1]) # access second element of the list
print(marks[2]) # access third element of the list
print(marks[3]) # access fourth element of the list         

# list is mutable data type
marks[0] = 50 # change the value of first element of the list
print(marks)

sublist = ["maths", "science", "english", "history", "geography"]
print(sublist)
print(sublist[0:1]) # access first element of the list
print(sublist[2:3]) # access third element of the list
print(sublist[1:4]) # access second to fourth element of the list

negitive_index = [10, 20, 30, 40, 50]
print(negitive_index[-1]) # access last element of the list
print(negitive_index[-2]) # access second last element of the list    

# methods
append_list = [1, 2, 3, 4, 5]
append_list.append(6) # add element to the end of the list
print(append_list)

insert_list = [1, 2, 3, 4, 5]
insert_list.insert(2, 10) # add element at specific index
print(insert_list)


sort_list = [5, 2, 9, 1, 3]
sort_list.sort() # sort the list in ascending order
print(sort_list)
sort_list.sort() # sort the list in descending order
sort_list.sort(reverse=True) # reverse the list
print(sort_list)

reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse() # reverse the list
print(reverse_list)


# tuple is a built in data type that store set of value
# it is immutable data type
# tuple is ordered collection of data
# it can store different data type value in a single tuple
# tuple is denoted by parentheses ()
# tuple is a collection of data which is ordered and unchangeable

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[0]) # access first element of the tuple
print(tuple1[1]) # access second element of the tuple
print(tuple1[2]) # access third element of the tuple
print(tuple1[3]) # access fourth element of the tuple
print(tuple1[4]) # access fifth element of the tuple        

methods_tuple = (1, 2, 3, 4, 5)
print(methods_tuple.count(2)) # count the number of times an element appears in the tuple
print(methods_tuple.index(3)) # return the index of the first occurrence of an element in the tuple 
