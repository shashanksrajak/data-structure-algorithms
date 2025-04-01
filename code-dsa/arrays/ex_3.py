# Question 3 - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

def odd_numbers(max):
    # create a list of odd nos
    result = []
    for i in range(1, int(max)):
        if((i+1)%2 != 0):
            result.append(i+1)
        #  if i % 2 == 1:
        #     result.append(i)
    print("The list of odd numbers is ->", result)


max_number = input("Enter a max number:")
odd_numbers(max_number)
