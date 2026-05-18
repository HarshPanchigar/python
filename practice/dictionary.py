menu = {
    "pizza" : 20.00,
    "burgur" : 15.25,
    "coffee" : 10.00
}

# print in dic
print(menu.get("coffee"))

# update 
menu.update({"chips" : 2.00})
menu.update({"pizza": 20.25})
print(menu)

#remove any key : value 
menu.pop("chips")
print(menu)

#popitem remove last or letest key : vlaue 
# menu.popitem()
# print(menu)

#clear 
# menu.clear()
# print(menu)

# print only keys 
# print(menu.keys())

# print one by one 
# for i in menu.keys():
#     print(i)


# same as key print values
# print(menu.values())
# for i in menu.values():
#     print(i)

print(menu.items())
for name , price in menu.items():
    print(f"{name}: {price}")