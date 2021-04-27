# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# if elif else statement
print("IF ? ELIF ? ELSE")
name = 'Havic'
if name == 'Chandan':
    print('Good Morning Chandan.')
elif name == 'Aryan':
    print('Have a good Day Aryan.')
else:
    print('Intruder Alert! Unknown Entity')

# For loop
print("FOR LOOP")
loop_list = [1,2,3,4,5,6,7,8,9,10]
for num in loop_list:
    if num%2:
        print(f'Odd Number: {num}')
    elif num%2 == 0:
        print(f'Even Number: {num}')

sum_list = 0
for num in loop_list:
    sum_list = sum_list + num

print(sum_list)

for letter in 'Hello World':
    print(letter)

tup = (1,2,3,4,5)
for item in tup:
    print (item)

print('\n')
loop_list2 = [(1,2,3),(4,5,6),(7,8,9)]
print(len(loop_list2))
for item in loop_list2:
    print(item)
# tupple unpacking
for a,b,c in loop_list2:
    print (a)

# Dictionary: unsorted key value list
d = {'k1':1,'k2':2,'k3':3,'k4':4}
for dictionary in d:
    print(dictionary)
for dictionary in d.items():
    print(dictionary)
for value in d.values():
    print(value)
for key,value in d.items():
    print(value)


# pass (Do Nothing At All [Place Holder];
# continue (To of the closest enclosing loop);
# break (exists the closest enclosed loop)
print("PASS ? CONTINUE ? BREAK")
a = [1,2,3,4,5]
for item in a:
    pass
for item in a:
    if item == 2:
        continue
    if item == 4:
        break
    print(item)

# While loop
print("WHILE LOOP")
x = 0
while x < 5:
    print(f'The Current value of x = {x}')
    x += 1
    if x == 5:
        break
else:
    print(f'x is equal to {x}')

# Operators
print("OPERATOR")
for num in range(10):
    print(num)
for num in range(2,10):
    print(num)
for num in range(0,15,2):
    print(num)
print(list(range(0,11,2)))

index_count = 0
word = 'abcdefghi'
for letter in word:
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1
for item in enumerate(word):
    print(item)
for index,letter in enumerate(word):
    print(letter)

zipList1 = [1,2,3,4,5,6,7]
zipList2 = ['a','b','c','d','e','f','g']
zipList3 = [100,99,98,97]
for item in zip(zipList1,zipList2):
    print(item)
for item in zip(zipList1,zipList2,zipList3):
    print(item)
print(list(zip(zipList1,zipList2)))

print('x' in [1,2,3])
print(2 in [1,2,3])
print('mykey' in {'mykey':234})
inDict = {'mykey':234}
print(234 in inDict.keys())
print(234 in inDict.values())

min_max_list = [10,20,30,40,50,10000]
print(min(min_max_list))
print(max(min_max_list))

from random import shuffle
shuffle_list = [1,2,3,5,6,7,8,22,4,556,7,42,32,4,77,331]
shuffle(shuffle_list)
print(shuffle_list)

from random import randint
print(randint(0,100))
ran_num = randint(0,100)

result = input('Enter a Number here: ')
print(result)
print(type(result))
print(int(result))
print(float(result))

result2 = int(input('Enter another number: '))
print(result2)
print(type(result2))

# List Comprehensions - a quick way to create a list; alternative for: creating a for loop and .append() to make list
loop_Str = 'Hello'
comp_list = []
for letter in loop_Str:
    comp_list.append(letter)
print(comp_list)

comp_list2 = [letter for letter in loop_Str]
print(comp_list2)

comp_list3 = [num**2 for num in range(0,20,2)]
print(comp_list3)
comp_list4 = [num**2 for num in range(0,20) if x%2==0]
print(comp_list4)

celcius = [0,10,20,34.5]
fahrenheit = [(9/5*temp + 32) for temp in celcius]
print(fahrenheit)

double_loop_list = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(double_loop_list)


