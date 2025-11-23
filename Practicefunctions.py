sweets={'blue':4, 'yellow':6, 'pink':12, 'orange':10, 'red':6, 'purple':11,}
print(sweets)
print(type(sweets))
#add items in the dictionary
sweets['green']=8
print(sweets)
#deleting items from dictionary
sweets.pop('yellow')
print(sweets)
#how to change/update the items
sweets['orange']=12
print(sweets)
#counting how many items there are in the dictionary
print(len(sweets))
#printing only the keys
print(sweets.keys())
#printing only the values
print(sweets.values())
#printing both keys and values
print(sweets.items())
for i in sweets:
    print(i)