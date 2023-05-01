
import random
import time


def reverse_num(num: int):
    return int(str(num)[::-1])


def is_palindromic(num: int):
    # check if number is same as reversed number
    return num == reverse_num(num)


def algorithm_196(num: int, max_iterations=10000, verbose=True):
    reversed = reverse_num(num)
    iteration = 0
    while num != reversed and iteration < max_iterations:
        iteration += 1
        num += reversed
        reversed = reverse_num(num)
        if verbose:
            print(f'{iteration} {num}')

    return num == reversed, num, iteration

# We can try reproduce some records from wikipedia
# https://en.wikipedia.org/wiki/Lychrel_number


# On 26 April 2019, Rob van Nobelen computed a new world record for the Most Delayed Palindromic Number:
# 12000700000025339936491 takes 288 iterations to reach a 142 digit palindrome
# 6634343445544188178365154497662249922269477578658488045222897505659677887769565057982225408848568757749622299422667944515638718814455443434366
find, num, iter = algorithm_196(12000700000025339936491, verbose=False)
if find:
    print(
        f'Palindromic number found in the {iter} iteration with value \n{num}')
else:
    print('Palindromic number not found!')

# On 5 January 2021, Anton Stefanov computed two new Most Delayed Palindromic Numbers:
# 13968441660506503386020 and 13568441660506503386420 takes 289 iterations to reach the same 142 digit palindrome as the Rob van Nobelen number.
find, num, iter = algorithm_196(13968441660506503386020, verbose=False)
if find:
    print(
        f'Palindromic number found in the {iter} iteration with value \n{num}')
else:
    print('Palindromic number not found!')

find, num, iter = algorithm_196(13568441660506503386420, verbose=False)
if find:
    print(
        f'Palindromic number found in the {iter} iteration with value \n{num}')
else:
    print('Palindromic number not found!')

# On December 14, 2021, Dmitry Maslov computed a new world record for the Most Delayed Palindromic Number:
# 1000206827388999999095750 takes 293 iterations to reach 132 digit palindrome
# 880226615529888473330265269768646444333433887733883465996765424854458424567699564388337788334333444646867962562033374888925516622088
find, num, iter = algorithm_196(1000206827388999999095750, verbose=False)
if find:
    print(
        f'Palindromic number found in the {iter} iteration with value \n{num}')
else:
    print('Palindromic number not found!')


def i_will_find_world_record(max_iterations=400, number_size=84):

    print('\nStart searching a new world record for the Most Delayed Palindromic Number!\n')
    my_record = 0
    world_record = 293
    cnt = 0  # only for information - count of searched numbers

    start_time = time.time()

    # we can define local function to get time from start rounded to 1 decimal place
    def get_time():
        return round(time.time()-start_time, 1)

    while True:
        # increase count of searched numbers
        cnt += 1
        # get random number of number_size bits
        num_to_try = random.getrandbits(number_size)

        find, num, iter = algorithm_196(
            num_to_try, max_iterations=max_iterations, verbose=False)

        if not find:
            continue

        if iter > world_record:
            print(
                f'New world record!!! {iter} iterations.')
            print(f'number: {num_to_try}')
            print(f'palindrome: {num}')
            print(f'{cnt} numbers searched in {get_time()} seconds')

        if iter > my_record:
            my_record = iter
            print(
                f'New my record! {iter} iterations.')
            print(f'number: {num_to_try}')
            print(f'palindrome: {num}')
            print(f'{cnt} numbers searched in {get_time()} seconds')


i_will_find_world_record()
