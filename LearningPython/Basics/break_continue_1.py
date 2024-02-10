# break -- breaks out from the nearest enclosing loop
# continue -- go to the start of the nearest enclosing loop
# ex 1
# x= 0
# while x < 5 :
#     print(x)
#     x= x+ 1
#     print("we are in the parent loop")
#
# print("we are out of the parent loop")

# ex 2
# x= 0
# while x < 5 :
#     print(x)
#     x= x+ 1
#     break # after this break , no more statements of the loop will be printed because we came out of the loop
#     print("we are in the parent loop")
#
# print("we are out of the parent loop")

# ex 3
# x = 0
# while x < 5:
#     print(x)
#     x = x + 1
#     continue  # after this continue , no more statements after this continue  will be printed because we are goingto the start of the loop
#     print("we are in the parent loop")
#
# print("we are out of the parent loop")

# ex 4 while loop inside while loop
# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("we are in the parent loop")
#     while y < 5:
#         print(y)
#         y = y+1
#         print("we are in the child loop")
#
# print("we are out of the while loop finally")

# ex 5 while loop inside while loop with break
# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("we are in the parent loop")
#     while y < 5:
#         print(y)
#         break
#         y = y+1
#         print("we are in the child loop")
#
# print("we are out of the while loop finally")

# ex 6 while loop inside while loop with continue
# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("we are in the parent loop")
#     while y < 5:
#         print(y)
#         y = y + 1
#         continue
#         print("we are in the child loop")
#
# print("we are out of the while loop finally")

# ex 6 while else loop
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
#     print("we are in the parent loop")
# else:
#     print("we are out of the loop")

# ex 7 while else loop
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
#     if x == 5:
#         break
#     print("we are in the parent loop")
# else: # else is not printed here because of the break statement in the while loop
#     print("we are out of the loop")

# ex 7 while else loop without break 
x = 0
while x <= 5:
    print(x)
    x = x + 1
    print("we are in the parent loop")
else:  # after the while loop , else is also printed
    print("we are out of the loop")
