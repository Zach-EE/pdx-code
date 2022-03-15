from functools import reduce
#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

numbers = [1,2,3,4,5,6,7,8,9,10,11]

summation = reduce(lambda x, y: x+y, numbers)
print (f'Sum of List: {summation}')

# TODO: Using a Read, Evaluate, Print, Loop (REPL), build a list of numbers by asking the user to enter them one at a time. Add each number to the list. Once the user enters 'done', pass the list to the sum function from version 2.1 and display the sum that's returned.

# TODO: Create a function called remove_all which takes in two parameters, numbers & target.The numbers parameter will be passed a list of numbers and the target parameter will be passed the number to remove from the list.The function will return a new list containing only the numbers that are not the target number.