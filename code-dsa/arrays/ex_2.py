# Question 2 - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md


heros=['spider man','thor','hulk','iron man','captain america']

# length of the list
print("Length of heros is:", len(heros))


# append
heros.append("Black Panther")


# remove
heros.remove("Black Panther")
print(heros)
heros.append("hulk")
print(heros)
heros.append("black panther")
print(heros)


# replace
# heros[2] = heros[5] = "doctor strange"
heros[1:3]=['doctor strange']


print(heros)

# sort alphabetically
print("Sorted list")
heros.sort() #asc order by default
print(heros)