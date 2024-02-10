# used to iterate the block of code as long as the test expression is true
# test exp is checked first ,if it is true , then it will go in to the body of loop
# conditions are used to stop the loop
# we can use it on list , strings , tuples ,dictionary

# x=0
# while x <= 10:
#     print(x)
#     print("we are inside the loop")
#     x= x+1   # this indentation  refers that we are checking the internal part of loop
# print("we came out of the loop")  # this prints after the completion of loop i.e. outside of loop

# while loop in strings
# city = "ThisismyBangaloreCity"
# x=0
# while x < len(city):
#     print(city[x])
#     x = x+1
# print("we are out of loop")

# while loop in lists
# list1=[1, 'bangalore', 'is a big city', 12.456, 100000,10 ,20,30,40,50.2345,"a","qwert"]
# i=0
# while i< len(list1):
#     print(list1[i])
#     i=i+1
# print("we are out of loop of the list")

# while loop in tuples
# tup1 = ("Delhi", "Goa", "Bangalore", "Punjab", "Kashmir", "Vizag", "Pune", "Goa",1,50.90,'f',"Delhi", "Goa", "Bangalore")
# i = 0
# while i< len(tup1):
#     print(tup1[i])
#     i=i+1
# print("we are out of loop for tuples")

# while loop in dictionaries

# books = {"learning python": "Mark Lutz",
#          "think python": "Allen B. Downey",
#          "Fluent Python": "Luciano Ramalho"}
# con_list = list(books)  # converts keys into a list
# print(con_list)
# print(books.keys())
# i = 0
# while i < len(con_list):
#     # then we print keys using con_list[] and separate by ":" then print values of each key using "books[con_list[]]".
#     key = con_list[i]
#     print(key, ":", books[key])
#     i += 1
# print("loop ends")
#

d1 = {1: 23, 2: 45, 3: 90, "qa": "test_url", "prod": "prod_url", "UAT": "uat_url",'qs': 56,89: "qwerty"}
conv_list2=list(d1)
i=0
while i< len(conv_list2):
    print(conv_list2[i],":",d1[conv_list2[i]])
    i=i+1
