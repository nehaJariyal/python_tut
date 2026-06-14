# dictionary is stored  value in key value pair
# it is denoted by curly braces {}
# it is mutable data type
# it is unordered collection of data
# it can store different data type value in a single dictionary   
#  dictionary is a collection of data which is unordered and changeable 
# dictionary is just like list and tuple but it is stored in key value pair
# dictionary is a built in data type that store set of value in key value pair
# dictionary is just like js object
dictionary1 = {"name": "John", "age": 30, "city": "New York"}
print(dictionary1)
print(dictionary1["name"]) # access value of name key
print(dictionary1["age"]) # access value of age key
print(dictionary1["city"]) # access value of city key

# change value of name key
dictionary1["name"] = "Jane"
print(dictionary1)

# nested dictionary
dictionary2 = {"name": "John", "age": 30, "city": "New York", "hobbies": {"hobby1": "reading", "hobby2": "traveling", "hobby3": "cooking"}}
print(dictionary2)
print(dictionary2["hobbies"]["hobby1"]) # access value of hobby1 key
print(dictionary2["hobbies"]["hobby2"]) # access value of hobby2 key
print(dictionary2["hobbies"]["hobby3"]) # access value of hobby3 key

# methods of dictionary
dictionary3 = {"name": "John", "age": 30, "city": "New York"}
print(dictionary3.keys()) # access all keys of the dictionary
print(list(dictionary3.keys()))
print(dictionary3.values()) # access all values of the dictionary
print(dictionary3.items()) # access all key value pairs of the dictionary
print(dictionary3.get("name")) # access value of name key using get method
print(dictionary3.get("age")) # access value of age key using get method
print(dictionary3.get("city")) # access value of city key using get method


