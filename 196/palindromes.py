# Reverse number
# str(num) converts int to string
# [::-1] is little magic - revert a string
# int(str(num)[::-1]) convert number to string, reverse it, and convert back to int
# this function can be writen in 3 steps
# def reverse_num(num: int):
#    str_num = str(num)
#    reversed_str = str_num[::-1]
#    return int(reversed_str)
def reverse_num(num: int):
    return int(str(num)[::-1])


def is_palindromic(num: int):
    # check if number is same as reversed number
    return num == reverse_num(num)

# we can check if function works
# print(is_palindromic(199))
# print(is_palindromic(1991))


def algorithm_196(num: int, max_iterations=100, verbose=True):
    reversed = reverse_num(num)
    iteration = 0
    while num != reversed and iteration < max_iterations:
        iteration += 1
        num += reversed
        reversed = reverse_num(num)
        if verbose:
            print(f'{iteration} {num}')

    return num == reversed, num, iteration


inp = int(input('Give me a some number: '))

find, num, iter = algorithm_196(inp, verbose=True)


if find:
    print(
        f'Palindromic number found in the {iter} iteration with value \n{num}')
else:
    print('Palindromic number not found!')
