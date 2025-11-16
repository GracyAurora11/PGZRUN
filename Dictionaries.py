householditems={'chair':4, 'table':6, 'utensil':12, 'books':10, 'fruit':6, 'electronics':11}

print(householditems)

print(type(householditems))

#add items in the dictionary

householditems['stationery']=8

print(householditems)

#deleting items from dictionary

householditems.pop('utensil')

print(householditems)

#how to change/update the items

householditems['chair']=12

print(householditems)

#counting how many items there are in the dictionary

print(len(householditems))

#printing only the keys

print(householditems.keys())

#printing only the values

print(householditems.values())

#printing both keys and values

print(householditems.items())

for i in householditems:
    print(i)