# Python
  Python is a programming language that lets you tell a computer what to do. It is easy to read, write, and understand, making it great for beginners and professionals alike.
 
   
   <img width="727" height="101" alt="image" src="https://github.com/user-attachments/assets/1131a335-ed91-40e2-8ac4-2cd820b3f686" />

 # Introduction to Programming
   Programming is the process of giving instructions to a computer so that it can perform tasks. These instructions are written in a programming language. Learning programming helps you automate tasks, solve problems, and create software.

 # Basic Programming Concepts
  # Variables 
  A variable is a storage space in a computer's memory that holds data. You can change its value while the program is running.
                 
    name = "Satwika"   # stores text
    age = 22          # stores a number
    height = 5.3       # stores a decimal number

 name → stores a string

  String:- A string is a piece of text in python, like words, sentences, or any characters.

age → stores an integer

 Integer :- An integer is a whole number 

height → stores a float
  
  Float:- A float is a number with a decimal point

# Data Types    
  A data type in Python tells the computer what kind of value a variable holds. It helps Python understand how to use the data (for calculations, storing text, making decisions, etc.). Different operations are valid for different types.

| Data Type               | Description          | Example                      |
| ----------------------- | -------------------- | ---------------------------- |
| **Integer (`int`)**     | Whole numbers        | 10, -5, 0                    |
| **Float (`float`)**     | Decimal numbers      | 3.14, -0.5                   |
| **String (`str`)**      | Text                 | "Hello", "Satwika"           |
| **Boolean (`bool`)**    | True or False values | True, False                  |
| **List (`list`)**       | Collection of items  | [1, 2, 3], ["a", "b"]        |
| **Tuple (`tuple`)**     | Immutable collection | (1, 2, 3)                    |
| **Dictionary (`dict`)** | Key-value pairs      | {"name": "Satwika", "age": 22} |

<img width="813" height="145" alt="image" src="https://github.com/user-attachments/assets/7072b5fd-36a2-446b-8c12-da578d1c1cd2" />


# Integer 
   An integer (often called int) is a whole number — a number without any decimal point.
It can be positive, negative, or zero.
   
    # examples of integers
    a = 10        # positive integer
    b = -3        # negative integer
    c = 0         # zero

# Float (float)  

decimal numbers: 3.14, -0.5     
   
 A float (short for floating-point number) is a number that has a decimal point.
 It is used when you need fractional or precise values, not just whole numbers.           
 
<img width="736" height="104" alt="image" src="https://github.com/user-attachments/assets/dc43670a-e551-486e-9226-ad78a994e489" />

# String (str) 
  
  text enclosed in quotes: "hello"

  A string is a sequence of characters enclosed in quotes.

         name = "Satwika"
         language = 'Python'
         print(name)
         print(language)

     
        text = "Hello"
        print(type(text))
       # Output: <class 'str'>


 # Boolean (bool)
 
   True or False

  A Boolean (in Python, type bool) is a data type that can have only two possible values:
✅ True or ❌ False

Booleans are used to represent yes/no, on/off, right/wrong, or 1/0 type of logic.

       is_student = True
       is_adult = False

       print(is_student)   # True
       print(type(is_student))   # <class 'bool'>

# List 

ordered, changeable sequence:

Lists are used to:

  Store multiple values in one place.

  Easily add, remove, update, or access data.

    fruits = ["apple", "banana", "cherry"]

    print(fruits[0])   # apple
    print(fruits[1])   # banana
    print(fruits[2])   # cherry

# Tuple 
  
  Ordered, immutable sequence:

  A Tuple in Python is a collection of items
       
  Tuples are immutable, meaning you cannot change, add, or remove items once created.

     tuple1 = (1, 2, 3)
     tuple2 = (4, 5, 6)
     combined = tuple1 + tuple2
     print(combined)
    # Output: (1, 2, 3, 4, 5, 6)

 # Dictionary (dict) 
   
  key → value pairs:

  A Dictionary in Python is a collection of data stored in key–value pairs.

  Dictionaries are written inside curly braces { }.

     # Example 1: Simple dictionary
     person = {
    "name": "John",
    "age": 25,
    "city": "New York"
    }

    # Example 2: Mixed data types
    student = {
    "name": "Emma",
    "age": 19,
    "marks": [85, 90, 92],
    "is_passed": True
    }

    # Example 3: Empty dictionary
    data = {}

  # Set 
  
  unordered collection of unique items:

  A Set in Python is a collection of unique and unordered items.

  Need to store unique values only.

  Want to perform mathematical operations like union, intersection, and difference.

  Don’t care about the order of elements.

     empty = {}
     print(type(empty))  # <class 'dict'>

    empty_set = set()
    print(type(empty_set))  # <class 'set'>


# Conditionals 
   
  Decision making

  Conditionals are statements that allow a program to make decisions based on certain conditions.

  if

  elif (else if)

  else

# if Statement

  The if statement allows a program to check a condition and execute a block of code only if that condition is True.

  age = 20

 if age >= 18:
   
  print("You are eligible to vote.")

  # if-else Statement

  When you want one action for True and another for False.

  age = 15

       if age >= 18:
       print("You are eligible to vote.")
        else:
        print("You are not eligible to vote.")

  # if-elif-else Statement
    
  Used when you want to test multiple conditions.

    marks = 88

    if marks >= 90:
    print("Grade: A")
    elif marks >= 75:
    print("Grade: B")
    elif marks >= 50:
    print("Grade: C")
    else:
    print("Grade: F")

# Essential Python Topics:

# Data structures deep dive

List: ordered, mutable. Methods: .append(), .extend(), .pop(), .insert(), slicing.

.append() - To add a single new element to the end of a list

 .extend() - To add several items to the end of the list at once.

 .pop() - To remove an element (default: last one) and optionally store or print it.

 .insert() - To insert a new element at a certain index in the list.

 slicing - To get or replace a subset (portion) of a list — without changing the whole list.

 Tuple: ordered, immutable—good for fixed records like coordinates.

 Dict: .get(key, default), iterate .items(), .keys(), .values().

 Set: fast membership, use set operations .union(), .intersection().

 # Introduction to Python: Overview of Python programming language.

Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991.

It’s designed to be easy to read, simple to write, and powerful enough to build almost anything — from web apps to AI systems.

# What is Python?

 A python is a high level programmimg language and helps us to communicate with computer.

# Why we use Python?

  We use Python because it’s simple, flexible, and powerful — perfect for both beginners and experts.

# Uses of Python?

 Python is used in web apps , Data Science , AI , Automation etc.

# Control Flow (if, else, elif)

#  Using conditional statements for decision-making

 Control flow means deciding which part of the code should run based on a condition.

# using conditional statements — if, elif, and else.

# If Statement

  If statement is used to run code only when a condition is true.

  Syntax
    
     if condition:
    # code to run when condition is True

# if...else Statement

It is used when you want two possible outcomes — one if the condition is true, and another if it’s false.

    if condition:
    # code to run when condition is True
    else:
    # code to run when condition is False

# if...elif...else Statement

 Used when there are multiple conditions to check.

    if condition1:
    # code runs if condition1 is True
    elif condition2:
    # code runs if condition1 is False and condition2 is True
    else:
    # code runs if all above conditions are False

# Example with Multiple Conditions

 You can use logical operators (and, or) inside conditions.

     if condition1 and condition2:
    # code runs if both conditions are True

    elif condition1 or condition2:
    # code runs if at least one condition is True

     elif not condition:
    # code runs if the condition is False

    else:
    # code runs if none of the above are True

# Nested if Statements

 You can place an if inside another if.

 





   
