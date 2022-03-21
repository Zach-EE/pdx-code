# from functools import reduce
# #The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

# numbers = [1,2,3,4,5,6,7,8,9,10,11]

# summation = reduce(lambda x, y: x+y, numbers)
# print (f'Sum of List: {summation}')


# Function will take a list of numbers and return their sum
def sum(numbers):
    total = 0
    for number in numbers:
        total += int(number)

    print(f'----------------\nNumbers: { numbers }\nSum: { total }')

# Function will take in a list and a digit to filter. Will return a filtered list with digit removed.


def remove_all(numbers, num_to_delete):
    print(f'Numbers: { numbers } \nRemove: { num_to_delete }')
    results = list(filter(lambda x: x != num_to_delete, numbers))
    print(f'Numbers: { results }')
    input_msg = '0'
    return results


def main():
    numbers = []
    # User input / interactive prompt allowing user access to application's functionality
    input_msg = input(
        "'  #  ' - adds numeric to list \n'  del  ' - remove entry from list \n'  done  ' - print sum and exit \n\nEnter: ' # ',' del ',' done ' \n=> ")

    while input_msg != 'done':
        if input_msg.isnumeric():
            numbers.append(input_msg)
            input_msg = input("Enter: ' # ',' del ',' done ' \n=> ")
        elif input_msg == 'del':
            num_to_delete = input('Input number to be removed: ')
            numbers = remove_all(numbers, num_to_delete)
            input_msg = input("' # ',' del ',' done ' \n=> ")
        else:
            input_msg = input(
                "Incorrect entry!!!\n\nEnter a whole number,'done', or 'del'")
    sum(numbers)


main()
