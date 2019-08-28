Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> to_do = []
>>> def add():
	x = input("What do you have to do?")
	x = str(x)
	global to_do
	to_do = to_do.append(x)
	print("Added to the list!")

	
>>> add()
What do you have to do?Spend 2-4 hours learning this code, Python
Added to the list!
>>> add()
What do you have to do?Get groceries from Ralphs
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    add()
  File "<pyshell#7>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'NoneType' object has no attribute 'append'
>>> add()
What do you have to do?"Get groceries from Ralphs"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    add()
  File "<pyshell#7>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'NoneType' object has no attribute 'append'
>>> add()
What do you have to do?Go to Ralphs
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    add()
  File "<pyshell#7>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'NoneType' object has no attribute 'append'
>>> to_do
>>> print("to_do)
      
SyntaxError: EOL while scanning string literal
>>> to_do = []
>>> add()
What do you have to do?spend time coding this
Added to the list!
>>> add()
What do you have to do?go to ralphs
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    add()
  File "<pyshell#7>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'NoneType' object has no attribute 'append'
>>> to_do = []
>>> def add():
	x = input("What do you have to do?")
	x = str(x)
	global to_do
	to_do = to_do.append(x)
	return to_do
	print("Added to the list!")

	
>>> to_do = []
>>> add()
What do you have to do?learn to code
>>> to_do
>>> to_do = [""]
>>> add()
What do you have to do?spend time coding
>>> def add():
	x = input("What do you have to do?")
	x = str(x)
	global to_do
	to_do = to_do.append(x)
	print("Added to the list!")

	
>>> to_do = ['']
>>> add()
What do you have to do?Spend time coding
Added to the list!
>>> to_do
>>> to_do[0]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    to_do[0]
TypeError: 'NoneType' object is not subscriptable
>>> to_do
>>> print(to_do)
None
>>> to_do = ["Spend 2 to 4 hours coding"]
>>> add()
What do you have to do?go to ralphs
Added to the list!
>>> to_do
>>> len(to_do)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    len(to_do)
TypeError: object of type 'NoneType' has no len()
>>> to_do[0] = "Spend time learning this code"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    to_do[0] = "Spend time learning this code"
TypeError: 'NoneType' object does not support item assignment
>>> to_do = ''
>>> add()
What do you have to do?Learn to code
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    add()
  File "<pyshell#26>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'str' object has no attribute 'append'
>>> def add():
	x = input("What do you have to do?")
	x = str(x)
	to_do = to_do.append(x)
	print("Added to the list!")

	
>>> add()
What do you have to do?go
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    add()
  File "<pyshell#41>", line 4, in add
    to_do = to_do.append(x)
UnboundLocalError: local variable 'to_do' referenced before assignment
>>> def add():
	global to_do
	x = input("What do you have to do?")
	x = str(x)
	to_do = to_do.append(x)
	print("Added to the list!")

	
>>> to_do = ["Get this shit done"]
>>> to_do[0]
'Get this shit done'
>>> add()
What do you have to do?go to ralphs
Added to the list!
>>> to_do
>>> print(to_do)
None
>>> to_do[1]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    to_do[1]
TypeError: 'NoneType' object is not subscriptable
>>> to_do
>>> to_do[0]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    to_do[0]
TypeError: 'NoneType' object is not subscriptable
>>> add()
What do you have to do?go to the mall
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    add()
  File "<pyshell#44>", line 5, in add
    to_do = to_do.append(x)
AttributeError: 'NoneType' object has no attribute 'append'
>>> rappers = ["biggie", "tupac", "mac miller", "nas", "jay-z"]
>>> rappers
['biggie', 'tupac', 'mac miller', 'nas', 'jay-z']
>>> def add():
	global to_do
	x = input("What do you have to do?")
	x = str(x)
	to_do.append(x)
	print("Added to the list!")

	
>>> to_do = []
>>> add()
What do you have to do?Learn this shit
Added to the list!
>>> to_do
['Learn this shit']
>>> add()
What do you have to do?take a moment to think about your life 6 months from now
Added to the list!
>>> to_do
['Learn this shit', 'take a moment to think about your life 6 months from now']
>>> def add(obj):
	global obj
	
SyntaxError: name 'obj' is parameter and global
>>> def add(object)
SyntaxError: invalid syntax
>>> def add(x)
SyntaxError: invalid syntax
>>> def add(x):
	y = input("What do you want to add?")
	y = str(y)
	x.append(y)
	print("Added to your list!")

	
>>> rockstars = []
>>> add(rockstars)
What do you want to add?Steven Tyler
Added to your list!
>>> rockstars
['Steven Tyler']
>>> add(to_do)
What do you want to add?fuck this is awesome
Added to your list!
>>> to_do
['Learn this shit', 'take a moment to think about your life 6 months from now', 'fuck this is awesome']
>>> todo_today = []
>>> add(todo_today)
What do you want to add?Make an iced coffee
Added to your list!
>>> add(todo_today)
What do you want to add?Check your email
Added to your list!
>>> add(todo_today)
What do you want to add?Work on you sides for class
Added to your list!
>>> todo_today
['Make an iced coffee', 'Check your email', 'Work on you sides for class']
>>> 
