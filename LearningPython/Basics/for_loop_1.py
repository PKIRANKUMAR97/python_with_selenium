# for loop in string
# a ="Thisisthebiggestcity"
# for i in a:
#     print(i)

# for loop in list
# list_1 =["Andhraa","Bihar","Chattisgarh","Delhi","telangana"]
# for i in list_1:
#     print(i)

# for loop in tuple
# tuple_1 =("Andhraa","Bihar","Chattisgarh","Delhi","telangana")
# for i in tuple_1:
#     print(i)

# for loop in list inside list
# list_2 =[["Andhraa","Amaravathi"],["Bihar","Patna"],["Chattisgarh","Raipur"],["India","Delhi"],["telangana","Hyderabad"]]
# for i in list_2:
#     print(i)
#
# list_3 =["Andhraa",["Bihar","Patna"],["Chattisgarh","Raipur"],["India","Delhi"],["telangana","Hyderabad"]]
# for i in list_3:
#     print(i)

# list_4 =[["Andhraa","Amaravathi"],["Bihar","Patna"],["Chattisgarh","Raipur"],["India","Delhi"],["telangana","Hyderabad"]]
# for state,capital in list_4:
#     print(state +"   capital is  "+capital)

# for loop in sets
# set_1={"Andhraa","Amaravathi"}
# for i in set_1:
#     print(i)

# for loop in dictionary
# list_4 =[["Andhraa","Amaravathi"],["Bihar","Patna"],["Chattisgarh","Raipur"],["India","Delhi"],["telangana","Hyderabad"]]
# dict_1 =dict(list_4)
# print(type(dict_1))
# print(dict_1)
# for state , capital in dict_1.items():
#     print(state+" capital is "+capital)

# for loop in for loop dictionary
list_4 = [["Andhraa", "Amaravathi"], ["Bihar", "Patna"], ["Chattisgarh", "Raipur"], ["India", "Delhi"],
          ["telangana", "Hyderabad"]]
dict_1 = dict(list_4)
print(type(dict_1))
print(dict_1)
for state, capital in dict_1.items():
    print(state, capital)
    for s in state:
        print(s)
        
