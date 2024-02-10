# d1 = {1: 23, 2: 45, 3: 90, "qa": "test_url", "prod": "prod_url", "UAT": "uat_url",'qs': 56,89: "qwerty"}
# print(d1.get("prod")) # returns the values of particular key that is passed
# print(d1.keys())   # returns only the keys of that dictionary
# print(d1.keys())   # returns only the keys of that dictionary
# print(d1.values())  # returns only the values of that dictionary
# print(d1.items())   # returns copy of the key-value pairs as a list
# print(d1.pop("qa"))  # return the value of that particular key
# print(d1)  # after removing the above , it will print the remaining
# print(d1.popitem()) # returns the last key value pair
# print(d1)  # after removing the above , it will print the remaining
# d1.update({"city":"Bangalore"})  # update the existing dictionary with this key-value pair
# print(d1)
# d1_copy=d1.copy()   # copy the dictionary
# print(d1_copy)
# d1_copy.clear()     # clears the dictionary
# print(d1_copy)

d23 = {1: 23, 2: 45, 3: 90, "qa": "test_url", "prod": "prod_url", "UAT": "uat_url",'qs': 56,89: "qwerty"}
print(d23)
print(d23["prod"]) # we can directly pass the key , then we got the value of that key 