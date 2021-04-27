def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# .format() Method
print('This is a String {}'.format('Insert Text!'))
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
print('The {f} {f} {f}'.format(f='fox',b='brown',q='quick'))

# Float formatting "{value:width.precision f}"
result = 99/7
print(result)
print("The result was {r}".format(r=result))
print("The result was {r:3.3f}".format(r=result))

#
name = "Aryan"
print("Hello, his name is {}".format(name))
print(f'Hello, his name is {name}')

# Lists - ordered mapping for storing objects
my_list = [1,2,3]
print(type(my_list))
my_list2 = ['STRING', 1, 23.0]
print("my_list2 size: {}".format(len(my_list2)))

myList = ['one','two','three']
print("MyList [0]: "+myList[0])
print(myList[1:])

anotherList = ['four','five']
print(myList + anotherList)
new_list = myList + anotherList
print(new_list)

new_list[0] = 'ONE ALL CAPS'
print(new_list)
print(new_list.append('six'))
print(new_list)
print(new_list.pop())
popped_item = new_list.pop(0)
print(popped_item)
print(new_list)

string_list = ['a','o','i','e','u']
num_list = [21,7,72,3,420,321]
print(string_list.sort())
# None -- its a type to indicate none value; a return value for function that doesn't return anything like .sort method;
# therefore you cannot reassign this list to another variable directly like: sorted_listed = string_list.sort() // None
print(string_list)
num_list.sort()
num_list.reverse()
print(num_list)

# Dictionaries - unordered mapping for storing objects // {'key1':'value1', 'key2':'value2'} //cannot be sorted
# Use when you don't have to know the order of things or fetching the index of any items
prices_lookup = {'apple':'3.99','oranges':'2.99','milk':'4.45'}
print(type(prices_lookup))
print(prices_lookup)
print(prices_lookup['milk'])
dict = {'k1':123,'k2':[0,1,2,3],'k3':{'insideKey':100}}
print(dict['k2'])
print(dict['k3']['insideKey'])

new_dict = {'k1':string_list}
print(new_dict)
print(new_dict['k1'][3].upper())

edit_dict = {'num1':21,'num2':72}
edit_dict['num3'] = 321
edit_dict['num1'] = 3
print(edit_dict)
print(edit_dict.keys())
print(edit_dict.values())
print(edit_dict.items())

# Tuples - are similar to lists but are immutable; once an element is inside a tuple, it cannot be reassigned
# Tuples use parenthesis (1,2,3)
# Why use them? To make sure the object that you are passing around doesn't get changed.
t = (1,2,3)
print(type(t))
t2 = ('one',2)
t3 = ('a','a','c','d','e','f')
print(t3.count('a'))
print(t3.index('d'))

list_t = [1,2,3]
print(list_t)
list_t[0] = 'NEW'
print(list_t)
# t[0] = 'NEW'    //Will throw error >> TypeError: 'tuple' object does not support item assignment
print(t[0])

# Sets - unordered collections of unique elements; There can only be ONE representative of the same object
set_1 = set()
set_1.add(1)
set_1.add(2)
set_1.add(3)
set_1.add(4)
print(set_1)

set_1.add(3)
print(set_1)

set_list = [5,5,5,7,7,7,1,1,71,1,1,32,10,10,2,2,2,2,3,3,3,3,4,4,4,4]
print(set(set_list))

# Files
myFile = open('/Users/cxt6u2h/Downloads/PyBasic.txt')
print('***********  1 READ   ***********')
print(myFile.read())
print('***********  2 READ  ***********')
print(myFile.read())
print('***********  3 READ  ***********')
print(myFile.seek(0))
print(myFile.read())
print('***********  4 READ  ***********')
print(myFile.seek(0))
print(myFile.readline())
myFile.close()
# If you don't close the file, you won't be able to access the file outside of python unless you close it first
print('***********  5 READ  ***********')
# If you use the following syntax, you don't have to close the file everytime you open
with open('/Users/cxt6u2h/Downloads/PyBasic.txt') as my_new_file:
    print(my_new_file.read())

print('***********  6 READ  ***********')
with open('/Users/cxt6u2h/Downloads/PyBasic.txt', mode='r') as my_new_file:
    print(my_new_file.read())

# m => r: read; w: override write ; a:append; r+:read and write; w+:overrides existing file and creates new file
print('***********  1 APPEND  ***********')
with open('/Users/cxt6u2h/Downloads/PyBasic.txt', mode='a') as f:
    f.write('\nThis is the appended line')
with open('/Users/cxt6u2h/Downloads/PyBasic.txt', mode='r') as f:
    print(f.read())
print('***********  1 WRITE  ***********')
with open('/Users/cxt6u2h/Downloads/PyIOBasic.txt', mode='w') as f:
    f.write('Sample File created with Python')
with open('/Users/cxt6u2h/Downloads/PyIOBasic.txt', mode='r') as f:
    print(f.read())


# Boolean & None (True / False) ; Don't use (true / false)
b = None
print(b)
# Comparison Operator
print(1 > 2)
print(1 >= 2)
print(1 == 1)
print('1' == 1)
print(1.0 == 1)
print(1 != 3)
print(1 <= 2)
print(1 < 2)
print(1 < 2 > 3)

# Logical Operator
print(1 < 2 and 2 < 3)
print('h' == 'h' and 2 == 2)
print(1 == 2 or 3 == 3)

print(not(1 == 1))