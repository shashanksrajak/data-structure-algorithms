# Question - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

expenses = [2200, 2350, 2600, 2130, 2190]

print("Q1 - In Feb, how many dollars you spent extra compare to January?")
print(expenses[1] - expenses[0]) #O(1)

print("Find out your total expense in first quarter (first three months) of the year.")
total_expense = expenses[0] + expenses[1] + expenses[2] #O(1)
print(total_expense)


print("Find out if you spent exactly 2000 dollars in any month")
for i in expenses:  #O(n)
    if(i == 2000):
        print("Spent exactly 2000 in a month")

# add june expense
expenses.append(1980)  #O(1)
print(expenses)

expenses[3] = expenses[3] - 200   #O(n)
print(expenses)