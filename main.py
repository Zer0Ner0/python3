# # Calculate age

# name = 'Amir Mazlan'
# birthday = input("What year were you born?")
# age = 2022 - int(birthday)

# print(f'Your age is {age}')

# # ---------------------------------------------------------------------------------------

# # Password Checker

# uname = input('Your username is?')
# pword = input('Your password is?')
# pword_len = len(pword)
# secret = '*' * pword_len

# print(f'{uname}, your password {secret} is {pword_len} letters long')

# # ---------------------------------------------------------------------------------------

# # Array/List

# string = 'hellooo'
# print(string[0:5:2])

# amazon_cart = ['notebooks', 'sunglasses', 'shoes', 'laptop', 'keyboard']

# amazon_cart[0] = 'toys'
# new_cart = amazon_cart[:]
# new_cart[0] = 'table'

# print(new_cart)
# print(amazon_cart)

# # ---------------------------------------------------------------------------------------

# # Array in Array

# matrix = [[1, 5, 1], [0, 1, 0], [1, 0, 1]]
# print(matrix[0][1])

# # ---------------------------------------------------------------------------------------

# # Array Method

# basket = ['a', 'b', 'c', 'd', 'e']

# # Add Array
# new_list = basket.append('f')
# print(new_list)
# print(basket)
# basket.insert(3, 'ca')
# print(basket)
# basket.extend(['g', 'z', 'c', '0', 'm', 'y'])
# print(basket)

# # Remove Array
# new_list = basket.pop()
# print(basket)
# print(new_list)
# new_list = basket.pop(0)
# print(basket)
# print(new_list)
# new_list = basket.remove('ca')
# print(basket)
# print(new_list)
# # new_list = basket.clear()
# # print(basket)
# # print(new_list)

# ind = basket.index('e')
# print(ind)
# ind = basket.index('g', 0, 6)
# print(ind)
# print('f' in basket)
# print('F' in basket)
# print(basket.count('c'))
# print(sorted(basket))
# print(basket)
# basket.sort()
# print(basket)
# basket.reverse()
# print(basket)

# # ---------------------------------------------------------------------------------------

# # Common Array Patterns

# print(list(range(101)))

# sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'AMIR'])
# print(new_sentence)

# # ---------------------------------------------------------------------------------------

# # Array Unpacking

# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# # ---------------------------------------------------------------------------------------

# # Dictionary

# dictionary = {'a': [1, 2, 3], 'b': 'Hello', 'x': True}

# my_list = [{
#     'a': True,
#     'b': [1, 2, 3],
#     'x': 'Hello'
# }, {
#     'a': [4, 5, 6],
#     'b': 'Bye',
#     'x': False
# }]
# print(dictionary['a'][1])
# print(my_list[0]['b'][2])

# from datetime import date

# today = date.today()
# user = {'name': "Amir", 'age': int(today.year) - 1994, 'sex': "Male"}
# # use .get to avoid error if no key found
# # if not found output will be None
# print(user.get('age', 'None'))
# print('address' in user)
# print('name' in user.keys())
# print('Male' in user.values())
# print(user.items())
# print(user.update({'age': 55}))
# print(user)
# print(user.update({'status': 'Married'}))
# print(user)
# print(user.pop('age'))
# print(user)

# user2 = dict(name='Aimi')
# print(user2)
# user2 = user.copy()
# print(user2)
# print(user.clear())
# user.clear()
# print(user)

# # ---------------------------------------------------------------------------------------

# # Tuple

# my_tuple = (1, 2, 3, 4, 5, 5)
# # Can't change data in tuple
# # my_tuple[1] = 'z'
# print(my_tuple[1])
# print(5 in my_tuple)

# new_tuple = my_tuple[2:4]
# print(new_tuple)

# x, y, z, *other = (1, 2, 3, 4, 5, 5)
# print(x)
# print(y)
# print(z)
# print(other)

# print(my_tuple.count(5))
# print(my_tuple.index(5))
# print(len(my_tuple))

# # ---------------------------------------------------------------------------------------

# # Sets
# my_list = [1, 2, 3, 4, 5, 5]
# my_set = {1, 2, 3, 4, 5, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10}
# my_set.add(100)
# my_set.add(2)
# # can't add and read duplicate
# print(my_set)
# # To remove duplicate in array change array to set
# print(set(my_list))
# new_list = list(my_set)
# # change to Array get index
# print(new_list)
# print(new_list[2])

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
# # isdisjoint means nothing in common
# print(my_set.isdisjoint(your_set))
# print(my_set.union(your_set))
# my_set = {4, 5}
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))

# # ---------------------------------------------------------------------------------------

# # Conditional Logic

# is_old = False
# is_licensed = True

# if is_old and is_licensed:
#     print('You are old enough to drive!')
# # Short Circuiting
# elif is_old or is_licensed:
#     print('You are not old enough but have license!')
# else:
#     print('You are not old enough and don\'t have license!')

# # ---------------------------------------------------------------------------------------

# # Condition Expression

# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)
# print(not False)

# # ---------------------------------------------------------------------------------------

# # Logical Exercise

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print("You are a master magician")
# elif is_magician or is_expert:
#     print("At least you're getting there")
# elif not is_magician:
#     print("You need magic powers")

# # ---------------------------------------------------------------------------------------

# # Loops
# from datetime import date

# user = {
#     'name': "Amir",
#     'age': int(date.today().year) - 1994,
#     'sex': "Male",
#     'can_swim': False
# }

# for key, value in user.items():
#     print(key, value)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# # ---------------------------------------------------------------------------------------

# # Counter
# # my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0

# for number in range(1, 11):
#     counter += number

# print(counter)

# for _ in range(0, 2, 1):
#     print(list(range(1, 11)))

# # ---------------------------------------------------------------------------------------

# # Enumerate

# for i, char in enumerate(list(range(100))):
#     if char == 99:
#         print(f'index of {char} is: {i}')

# # ---------------------------------------------------------------------------------------

# # While
# item = 0

# while item <= 80:
#     if item <= 35:
#         print(f'Item: {item}. Long way to go')
#         item += 1
#     elif item <= 70:
#         print(f'Item: {item}. We can go futher.')
#         item += 1
#     else:
#         print(f'Item: {item}. We are done')
#         break

# # ---------------------------------------------------------------------------------------

# # GUI

# picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
#            [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

# for row in picture:
#     for col in row:
#         if (col == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')
# print('')

# for row in picture:
#     for col in row:
#         if (col == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')
# print('')

# # ---------------------------------------------------------------------------------------

# # Check duplicate

# my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate = []

# for value in my_list:
#     if my_list.count(value) > 1:
#         if value not in duplicate:
#             duplicate.append(value)

# print(duplicate)

# # ---------------------------------------------------------------------------------------

# # Function

# def show_tree():
#     '''Info: This function print tree image'''
#     picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0],
#                [0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1],
#                [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

#     for row in picture:
#         for col in row:
#             if (col == 1):
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print('')
#     print('')

# loop = 0
# x = 1
# while loop <= x:
#     show_tree()
#     # print info
#     print(show_tree.__doc__)
#     loop += 1

# # Default Keyword =
# def say_hello(name='Flash', emoji='##'):
#     '''Info: This function print Hello with name and emoji'''
#     print(f'Hello {name} {emoji}')

# # Keyword
# say_hello(name='Amir', emoji=':-)')
# # Call Keyword
# say_hello()

# # ---------------------------------------------------------------------------------------

# # Return

# def sum(num1, num2):
#     return num1 + num2

# print(sum(10, 5))

# # ---------------------------------------------------------------------------------------

# # Function Exercise

# def highest_even(list):
#     even = []
#     for numb in list:
#         if numb % 2 == 0:
#             even.append(numb)
#     return max(even)

# print(highest_even([10, 2, 3, 24, 8, 11]))

# # ---------------------------------------------------------------------------------------

# # Scope - What variables do I have access to?

# total = 0

# def count():
#     global total
#     total += 1
#     return total

# count()
# count()
# print(count())

# def outer():
#     x = "local"

#     def inner():
#         # nonlocal - parent local
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)

# outer()

# # 1 - start with local
# # 2 - Parent local?
# # 3 - global
# # 4 - built in python functions

# # ---------------------------------------------------------------------------------------

# # Modules

# import utility

# print(utility.minus(24, 2))

# # ---------------------------------------------------------------------------------------

# # Error Handling

# while True:
#     try:
#         age = int(input('What is your age? '))
#         print(10 / age)
#     except ValueError:
#         print('Please enter a number')
#         continue
#     except ZeroDivisionError:
#         print("Please enter age higher than 0")
#         break
#     else:
#         print('Thank You')
#     finally:
#         print('ok, i am finally done')
#     print('can you see me?')

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)

# print(sum(1, '2'))

# # ---------------------------------------------------------------------------------------

# #File I/O

# my_file = open('test.txt')

# print(my_file.read())
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readlines())

# my_file.close()

# #OR Below
# #Mode R=Read W=Write A=Append r+=read & write
# with open('test.txt', mode = '') as my_file:
#   text = my_file.write('hey it\'s me!')
#   print(my_file.readlines())

# try:
#   with open('app/sad.txt', mode='r') as my_file:
#     print(my_file.write())
# except FileNotFoundError as err:
#   print('file does not exist')
#   raise err
# except IOError as err:
#   print('IO Error')
#   raise err

# # ---------------------------------------------------------------------------------------

#Exercise All in One