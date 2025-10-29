#  Python
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

# Essential Python Topics

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

  <img width="830" height="173" alt="image" src="https://github.com/user-attachments/assets/e42dff23-7635-4b2c-9f0a-f59a01eaf71d" />


# if...else Statement

It is used when you want two possible outcomes — one if the condition is true, and another if it’s false.

    if condition:
    # code to run when condition is True
    else:
    # code to run when condition is False

  <img width="803" height="185" alt="image" src="https://github.com/user-attachments/assets/c7c5a11e-0138-4884-922d-c6e6023b9518" />


# if...elif...else Statement

 Used when there are multiple conditions to check.

    if condition1:
    # code runs if condition1 is True
    elif condition2:
    # code runs if condition1 is False and condition2 is True
    else:
    # code runs if all above conditions are False

  <img width="818" height="295" alt="image" src="https://github.com/user-attachments/assets/6f31b1a0-abf5-4593-bffc-e85ec1ecfe6d" />


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

<img width="836" height="263" alt="image" src="https://github.com/user-attachments/assets/10f7718a-71de-4446-9781-40deee21cc07" />


# Nested if Statements

 You can place an if inside another if.

 <img width="773" height="244" alt="image" src="https://github.com/user-attachments/assets/b123ef94-86c4-4e36-9f89-7e5122d5dc8b" />

#  Functions and Modules:

 # Function?

 A function is a block of code that performs a specific task.

 # Why We Use Functions

  To avoid writing the same code many times
  
  To make the code easier to read and manage
  
  To divide big programs into smaller parts
  
  To reuse the code

    def function_name(parameters):
    # code to execute
    return result

<img width="520" height="164" alt="image" src="https://github.com/user-attachments/assets/6a729d45-a7be-4350-8666-13bb5fad073c" />

# Modules in Python
    
A module is simply a Python file (.py) that contains functions, variables, or classes which you can use in other programs.

# Why we use module

To organize your code into multiple files.

To reuse code in other programs.

To import Python’s built-in functionalities easily.

    import module_name

<img width="713" height="267" alt="image" src="https://github.com/user-attachments/assets/73119bf2-be9c-43e5-ab55-a2994c56c2c4" />
  
# Packages in Python

A package is a collection of modules grouped together in a folder

A package folder must contain a special file named __init__.py (even if it’s empty).

This file tells Python that the folder is a package.

    package_name/
    │
    ├── __init__.py        # Marks this folder as a package
    ├── module1.py         # Module 1
    ├── module2.py         # Module 2
    └── main.py            # Program that uses the package

    

# Data Structures: 

Data Structures are ways to store and organize data in a program so that they can be used efficiently.

# List - Working with list and list operations

 A list is an ordered, changeable (mutable) collection of items.

    list_name = [item1, item2, item3]

<img width="370" height="64" alt="image" src="https://github.com/user-attachments/assets/1668aca1-aa48-409a-b74f-1d2c4d03ddfa" />

# By using list Operations

 <img width="614" height="403" alt="image" src="https://github.com/user-attachments/assets/0f767f7a-3c74-4937-a8d8-f8eb23c1973b" />

# Dictionaries — Understanding Key-Value Pairs

 A dictionary stores data in key-value pairs

     dictionary_name = {key1: value1, key2: value2}

<img width="520" height="196" alt="image" src="https://github.com/user-attachments/assets/01857b7f-acc8-4d37-be3f-5b666d1df08e" />

<img width="468" height="307" alt="image" src="https://github.com/user-attachments/assets/7dbe5f8c-6f38-4a9e-a428-327822cc78dc" />

# Tuples — Introduction and Immutability

A tuple is an ordered, immutable (unchangeable) collection.

     tuple_name = (item1, item2, item3)

<img width="500" height="208" alt="image" src="https://github.com/user-attachments/assets/540a8494-9ebf-4beb-aced-ac2f12d0a24c" />

# Sets — Working with Sets and Set Operations

A set is an unordered collection of unique items.

It automatically removes duplicates.

 Syntax:
      
      set_name = {item1, item2, item3}

<img width="521" height="260" alt="image" src="https://github.com/user-attachments/assets/7fb8fccb-9df6-4959-94da-551bf4ef74ab" />

# File Handling in Python

File handling allows you to create, read, write, and modify files directly from your Python programs.

 # Reading and Writing Files: Manipulating Files Using Python

     file = open("filename", "mode")

  <img width="445" height="154" alt="image" src="https://github.com/user-attachments/assets/e6278882-73ec-48d8-884d-2d7fe769e828" />

# Object-Oriented Programming (OOP)
 
  Object-Oriented Programming (OOP) is a programming approach that organizes code around objects.

# It helps you to:

  Structure your code clearly

  Reuse code easily

  Make large programs easier to manage and extend

# Classes and Objects: Introduction to classes and objects in Python. 

# What is a Class?
 
  A class is like a blueprint or template for creating objects.

  It defines data(attributes) and function(method) that describes the  behaviour of  an object.

  For example, a class  Car defines what all cars have (color, model, speed) and what they can do (start, stop).

 # What is an Object?

   An object is an instance of a class — a real example created from the class blueprint.

   
     class ClassName:
    # attributes and methods
    def __init__(self):
        # constructor - runs when an object is created
        pass

    def method_name(self):
        # behavior of object
        pass

  <img width="664" height="130" alt="image" src="https://github.com/user-attachments/assets/14f8aeb8-5111-42f1-86b9-2625a06a2427" />

  <img width="736" height="115" alt="image" src="https://github.com/user-attachments/assets/ca50ab2f-253c-4463-8d88-80815ccb28f7" />

#  Inheritance: Understanding inheritance and polymorphism. 

 # What is Inheritance?

  Inherit means to get something from someone else.

  Inheritance means one class can inherit properties and methods from another class.

  It helps to reuse code and avoid duplication.

  Parent (Base/Super) Class: The class whose properties are inherited.
 
  Child (Derived/Sub) Class: The class that inherits properties.

    class Parent:
    # parent class code

    class Child(Parent):
    # child class inherits from Parent

<img width="736" height="115" alt="image" src="https://github.com/user-attachments/assets/25112b5d-1f30-4fa8-bd7f-a53560cf1a78" />

# Using super() to Access Parent Class

 



  

  

  












  


 





   
