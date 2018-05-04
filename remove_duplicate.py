#Assignment: Write a program which will remove duplicates from the array.

names = ["Alex","John","Mary","Steve","John", "Steve"]
new_names = []
for x in names:
    if x not in new_names:
        new_names.append(x)
print (new_names)
