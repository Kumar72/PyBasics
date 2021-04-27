import string

print(2 % 2)
print(8 % 3)

# HELP Function will help provide details on any methods / functions (Documentation)
helplist = [1, 2, 3, 4]
help(helplist.insert)

# Functions
print('**************** FUNCTIONS ****************')


# def Keyword + correct indentation + proper structure (snake casing for naming any function)
def name_of_function(name='Default'):
    '''
    Comment code for the given function
    you can set default so that no error message is thrown
    :return: Hello with name parameter
    '''
    return f'Hello {name}'


print(name_of_function('Chandan'))
print(name_of_function())


def sum_func(num1, num2):
    return num1 + num2


sum_result = sum_func(21, 72)
print(sum_result)


def even_check(num):
    return num % 2 == 0


print(even_check(21))


def even_checklist(num_list):
    even_num = []

    for num in num_list:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
    # return [num%2==0 for num in num_list]


print(even_checklist([1, 3, 5, 7, 8]))

stock_prices = [('APPL', 125), ('GOOG', 150), ('TSLA', 210)]
for ticker, price in stock_prices:
    print(price + (0.1 * price))

work_hours = [('Jasmyn', 500), ('Havic', 365), ('Aryan', 420), ('Sherlock', 720)]


def employee_check(work_hrs):
    current_max = 0
    employee_of_month = ''
    for associate, hours in work_hrs:
        if hours > current_max:
            current_max = hours
            employee_of_month = associate
    return (employee_of_month, current_max)


tuple_result = employee_check(work_hours)
name, hours = employee_check(work_hours)
print(tuple_result)
print(f'Employee of the Month {name}', f'with {hours} hours')

shuffle_list = [num for num in range(0, 10)]
from random import shuffle

shuffle(shuffle_list)
print(shuffle_list)


def shuffle_list_func(num_list):
    shuffle(num_list)
    return num_list


shuffle_result = shuffle_list_func(shuffle_list)
print(shuffle_result)

xo_list = ['', 'O', '']


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number (0,1,2): ')
    return int(guess)


def check_guess(grid, guess):
    if grid[guess] == 'O':
        print('Correct')
    else:
        print('Wrong guess!')
        print(grid)


shuffled_xo_list = shuffle_list_func(xo_list)


# guess = player_guess()
# check_guess(shuffled_xo_list, guess)


# Functional Parameters: *args = arguments and **kwargs = key word arguments -- A way to accept an arbitrary number
# of arguments and keyword arguments without having to pre-define a bunch of params in your function call
def five_percent_on_args(*args):
    # args can be any other key word (ex. spam) making it an arbitrary choice, as long as it follows the *
    # treats all argument inside the *args as tuple
    print(args)
    # Returns 5% of the sum for as many argument being passed.
    return sum(args) * 0.05


print(five_percent_on_args(40, 60, 2, 243))


def fruit_is_key_word(**kwarg):
    # use **kwargs to build a dictionary of key value pair; again the key word is arbitrary choice,
    # as long as it follows the ** -- indicating this is a dictionary
    print(kwarg)
    if 'fruit' in kwarg:
        print('My fruit of choice is {}'.format(kwarg['fruit']))
    else:
        print('I did not find any fruit here')


print(fruit_is_key_word(fruit='mango'))
print(fruit_is_key_word(fruit='banana', veggie='mushrooms'))


def func_param_test(*args, **kwargs):
    # Very useful when working with libraries and dealing with arbitrary arguments
    # Note: since we passed args before kwargs, we need to maintain the order when we call the function
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[2], kwargs['food']))


# maintain the order thus if you add 100 at the end you will be adding an arg after kwarg which will result in err
print(func_param_test(7, 21, 11, 3, 72, fruit='orange', food='tacos', animal='dog'))


# Coding Exercise 1: return even values in a list given any set of integer arguments
def tuple_to_list(*args):
    alist = []
    for element in args:
        if element % 2 == 0:
            alist.append(element)
    return alist


tuple_to_list(1, 2, 3, 4, 5, 6)


# Coding Exercise 2: take in a string & return a matching string where every even letter is UC and odd letter is LC
def word_alterations(word):
    newWord = ''
    for letter in word:
        if len(newWord) % 2:
            newWord += letter.upper()
        else:
            newWord += letter.lower()
    # Make all odd character in String Lower Case
    return newWord


print(word_alterations('Anthropomorphism'))


# WarmUp 1: Lesser of 2 evens: function returns lesser of two given num, if both are even
#               But returns the greater if on or both are odd

def lesser_of_two_evens(num1, num2):
    # If both numbers are even
    if num1 % 2 == 0 and num2 % 2 == 0:
        # return num1 if num1 < num2 else num2
        return min(num1, num2)
    else:
        # return num1 if num1 > num2 else num2
        return max(num1, num2)


# Test WarmUp 1
print('WarmUp 1')
print(lesser_of_two_evens(2, 5))
print(lesser_of_two_evens(8, 72))
print(lesser_of_two_evens(99, 21))


# WarmUp 2: Animal Crackers: function takes in 2 words, returns true if both words begin with same letter
def animal_cracker(word):
    word_list = word.lower().split()

    # first = word_list[0]
    # second = word_list[1]
    # return first[0] == second[0]
    return word_list[0][0] == word_list[1][0]


# Test Warmup 2
print('WarmUp 2')
print(animal_cracker('Levelheaded Llama'))
print(animal_cracker('Crazy Kangaroo'))
print(animal_cracker('Crazy cat'))


# WarmUp 3: Makes Twenty: Given 2 values, return true if sum = 20 or if one value is 20; else return false.
def makes_twenty(num1, num2):
    return num1 + num2 == 20 or num1 == 20 or num2 == 20
    # if num1 + num2 == 20:
    #     return True
    # elif num1 == 20 or num2 == 20:
    #     return True
    # else:
    #     return False


# Test WarmUp 3:
print('WarmUp 3')
print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# Level 1: Old McDonald: Function to capitalize the first and nth letter of a name
def old_mcdonald(name_str, position):
    first_part = name_str[:position]
    second_part = name_str[position:]
    return first_part.capitalize() + second_part.capitalize()


# Test Level 1.1:
print('Level 1.1')
print(old_mcdonald('mcdonald', 2))


# Level 1: Master Yoda: Given Sentence, return the reversed sentence
def master_yoda(sentence):
    word_list = sentence.lower().split()
    # reversed_wordlist = word_list[::-1]
    # print(reversed_wordlist)
    word_list.reverse()
    # reversed_sentence = ''

    # for word in word_list:
    #     reversed_sentence += word + ' '
    # return reversed_sentence.capitalize()
    return ' '.join(word_list).capitalize()


# Test Level 1.2
print('Level 1.2')
print(master_yoda('I am home'))
print(master_yoda('We are ready'))


# Level 1: Almost there: Given integer, return True if n is within 10 of either 100 or 200 else False
def almost_there(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)


# Test Level 1.3
print('Level 1.3')
print(almost_there(90))
print(almost_there(104))
print(almost_there(209))
print(almost_there(150))


# Level 2: Find 33: Given an array of values, return true if it contains 3 next to another 3
def find_33(nums):
    val1 = 0
    val2 = 0
    for num in nums:
        if num == 3 and val1 != 3:
            val1 = 3
        elif val1 == 3 and num == 3:
            val2 = 3
        else:
            val1 = 0
    return val1 == val2 == 3


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def out_33(nums):
    for i in range(0, len(nums) - 1):
        # we are slicing 2 values from nums array and comparing it with our expected output
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


# Test Level 2.1
print('Level 2.1')
print(find_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(out_33([3, 1, 3]))


# Level 2: Paper Doll: Given String, return a string where for every character in the string, there are 3 characters
def paper_doll(word):
    output = ''
    for letter in word:
        output += letter * 3
    return output


# Test Level 2.2
print('Level 2.2')
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# Level 2: Black Jack: Given 3 integer between 1-11, return sum if less than 21, BUST if greater than 21
#                      if the BUST contains an 11, reduce value to 1 and re-evaluate
def black_jack(card1, card2, card3):
    total = sum([card1, card2, card3])
    if 11 in [card1, card2, card3] and total > 21:
        total -= 10

    if total <= 21:
        return total
    else:
        return 'BUST'


# Test Level 2.3
print('Level 2.3')
print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))


# Level 2: Summer of 69: Return the sum of the nums in the given array; ignore section of num starting with 6 -> 9
#                        Return 0 for no numbers; Note: every list with a 6 will have a 9
def summer_69(nums):
    total = 0
    add = True
    for i in range(0, len(nums)):
        if nums[i] != 6 and add:
            total += nums[i]
        elif nums[i] == 6:
            add = False
        elif nums[i] == 9:
            add = True

    return total


def sum_69(nums):
    total = 0
    add = True

    for num in nums:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


# Test Level 2.4
print('Level 2.4')
print(summer_69([1, 3, 5]))  # 9
print(summer_69([4, 5, 6, 7, 8, 9]))  # 9
print(summer_69([2, 1, 6, 9, 11]))  # 14
print(sum_69([2, 1, 6, 9, 11]))  # 14


# Challenge: Spy Game: Write a function that takes a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0, 0, 7, 'X']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


# Test Challenge
print('Challenge 1')
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False


# Challenge: Count Prime: A function to return all the prime number given an end number; 0 and 1 != prime numbers
def count_prime(num):
    if num < 2:
        return 0
    counter = 0
    prime_values = [2]
    i = 3
    while i <= num:
        # check to see if i is prime until the input num
        # check to see if x is prime for only odd num therefore we use the step size of 2
        # for y in range(3, i, 2):
        for y in prime_values:
            if i % y == 0:
                i += 2
                break
        else:
            prime_values.append(i)
            i += 2
    print(prime_values)
    return len(prime_values)


# Test Challenge
print('Challenge 2')
print(count_prime(10))
print(count_prime(21))
print(count_prime(100))  # 25

# LAMBDA Expression Map and Filter
print('Lambda Function')


# With Maps we only pass in the function name, not name() to execute the func; because the Map function takes care of it
# Else it will throw a 'TypeError'
# Map applies the given function to the list of object provided

def lambda_sqfunc(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(lambda_sqfunc, my_nums):
    print(item)
print(list(map(lambda_sqfunc, my_nums)))
# Lambda Expression Execution
print(list(map(lambda num: num ** 2, my_nums)))


def splicer(strname):
    if len(strname) % 2 == 0:
        return 'EVEN'
    else:
        return strname[0]


names = ['Aryan', 'Aladin', 'Crank', 'Leo']

print(list(map(splicer, names)))
print(list(map(lambda x: x[0], names)))
print(list(map(lambda x: x[::-1], names)))


def check_even(num):
    return num % 2 == 0


my_numbers = [1, 2, 3, 4, 5, 6]

# Filter function will take in a boolean function and apply it to your list of data
print(list(filter(check_even, my_numbers)))
# Lambda Expression Execution
print(list(filter(lambda num: num % 2, my_numbers)))

# RESOURCES: More Problems like this on Eulerproject


# REVIEW: Nested Statement and Scope
# LEGB Rule Format: Local, Enclosing Functional Locals, Global, Built-In
# L > names assigned within a function (def or lambda)
var = lambda num: num ** 2


# E > names in the local scope of any and all enclosing function (def or lambda), from inner to outer
def greet():
    # Checked for name in the enclosed function
    enclosed_name = 'Havic - Enclosed Name'

    def hello():
        # name not defined in local
        print('Hello ' + enclosed_name)

    hello()


greet()
# G > (module) names assigned at the top-level of a module file, or declared global in a def within the file
global_name = 'Aryan - Global Name'


def greet_global():
    global global_name
    # name not defined in enclosed local
    global_name = 'Havic - Enclosed Local Override on global function'

    def hello():
        global global_name
        # name not defined in local
        global_name = 'Crank - Local Override on global function'
        print('Hello ' + global_name)

    hello()


print(global_name)
greet_global()
# we just changed to global value in the function by using the global keyword -- but don't use this
print(global_name)


# Alternative
#  global_name = greet_global(global_name)
# B > (python) names pre-assigned in the build-in names module: open, range , Syntax Error, ...


# HW 1: Compute Volume of Sphere  = 4/3 (Pi)r^3
def volume_of_sphere(radius):
    return (4 / 3) * 3.14 * radius ** 3


print(volume_of_sphere(2))


# HW 2: Check if given number is in between the range provided (high and low)
def range_check(num, low, high):
    return num in range(low, high + 1)


print(range_check(5, 2, 7))
print(range_check(3, 1, 10))


# HW 3: Calculate the number of Upper case and Lower case letters in a given statement
def case_sensitivity(statement):
    case_dictonary = {'upper': 0, 'lower': 0, 'punctuation': 0}
    # or
    upperCase = 0
    lowerCase = 0
    punctuationMark = 0

    for letter in statement:
        if letter.isupper():
            upperCase += 1
            case_dictonary['upper'] += 1
        elif letter.islower():
            lowerCase += 1
            case_dictonary['lower'] += 1
        else:
            punctuationMark += 1
            case_dictonary['punctuation'] += 1

    print(f'Original Statement: {statement}')
    print(f'Number of upper case Characters: {upperCase}')
    print(f'Dictionary: upper case Characters: {case_dictonary["upper"]}')
    print(f'Number of lower case Characters: {lowerCase}')
    print(f'Dictionary: lower case Characters: {case_dictonary["lower"]}')


print(case_sensitivity('Hello Mr. Rogers, how are you this fine Tuesday?'))


# HW 4: Take a list and return only the unique elements from the list
def unique_list(list1):
    # return list(set(list1))
    unique_values = []
    for num in list1:
        if num not in unique_values:
            unique_values.append(num)
    return unique_values


print(unique_list([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9]))


# HW 5: Palindrome
def palindrome(phrase):
    phrase = phrase.replace(' ', '')
    return phrase == phrase[::-1]


print(palindrome('nurses run'))


# HW 6: Pangrams
def pangram(statement, alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    statement = statement.replace(' ', '').lower()
    statement_set = set(statement)
    return statement_set == alphabet_set


print(pangram('The quick brown fox jumps over the lazy dog'))
print(pangram('Pangrams are words or sentences containing every letter of the alphabet at least once'))

