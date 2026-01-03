#1
var='hello'
print(var)
num=1
print(num)
val = True
print(type(val))
print(type(var))
print(type(num))

#string


test = 'welcome to aileela' 
print(test)
print(len(test))
print(test[0:5])

print(test.upper())
print(test.lower())

print(test.count('e'))
print(test.find('o'))
print(test.replace('aileela', 'python'))

msg = '   Hello World    '
print(msg)
print(msg.strip())

print(test.split(','))

name=test+msg
print(name)


name = '{}{}'.format(test, msg)
print(name)

name = f'{test} {msg}'
print(name)


num1=45
num2=18

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num2 / num1)   # division sometimes may result in float
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder
print(num2 % num1)


# Use help() function to get brief info about all the methods supported by a data type (or claass)

#help(str)   

# If you only need a list of supported functions, use dir() instead of help()

#dir(str)

# To see what a function exactly does, use ?

str.title  # title is one function supported by string

#If Else based on comparison operators
x = 4
y = 3
if x > y:             # if is followed by condition which is followed by :    # That's standard syntax
  print('yes, x is indeed greater than y') 


 
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')


#list
tem=[1,'om',2.4,'mango']
print(tem)
print(tem[2])
print(tem[0:2])
print(tem[-1])

print(tem.append('T.E'))
print(tem.pop())

#print(tem.sort())

for i in tem:
    print(i)

#Nested list
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))