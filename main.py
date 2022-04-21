#Calculate age

#name = 'Amir Mazlan'
#birthday = input ("What year were you born?")
#age = 2022 - int(birthday)

#print(f'Your age is {age}')

#---------------------------------------------------------------------------------------

#Password Checker

#uname = input('Your username is?')
#pword = input('Your password is?')
#pword_len = len(pword)
#secret = '*' * pword_len

#print(f'{uname}, your password {secret} is {pword_len} letters long')

#---------------------------------------------------------------------------------------

#Array/List

string = 'hellooo'
print(string[0:5:2])

amazon_cart = [
  'notebooks',
  'sunglasses', 
  'shoes',
  'laptop',
  'keyboard'
]

amazon_cart[0] = 'toys'
new_cart = amazon_cart[:]
new_cart[0] = 'table'

print(new_cart)
print(amazon_cart)