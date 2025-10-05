art = {'gracy','keira','sophia','chloe','amber','kruthi','aarna','freya'}
science = {'gracy','keira','amber','mary','joseph','thomas','freya','cole','alex'}
#removing the duplicates
print(art.union(science))
#common interests
print(art.intersection(science))
#those who like art but not science
print(art.difference(science))
#those who like science but not art
print(science.difference(art))
#removing those who like both
print(art.symmetric_difference(science))