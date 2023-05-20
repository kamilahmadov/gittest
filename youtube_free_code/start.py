# Working with Lines

phrase = "Kamil is learning \nPython"    # \n to make new line
print(phrase)

phrase = "Kamil is learning Python"
print(phrase.lower())                    # .lower() to lowercase
print(phrase.upper())                    # .upper() to uppercase
print(phrase.islower())                  # islower() to chechk is it lower
print(len(phrase))                       # to check number of symbols
print(phrase[0])                         # to take exact symbol
print(phrase.index("K"))                 # to take index (the order number)
print(phrase.index("earn"))              # always show index where starts
print(phrase.replace("Kamil", "Ibrahim"))

# Working with Numbers

num = 5
print(abs(num))
print(pow(4, 6))                          # возвести в степень
print(max(4, 6))                          # to show bigger
print(min(4, 6))
print(round(4.65))

from math import *                        # to make below command work

print(floor(3.7))                         # round down
print(ceil(3.7))                          # round up
print(sqrt(25))                           # квадратный корень

# Working with lists

friends = ["Kamil", "Ayhan", "Tarhan"]
ages = [23, 24, 25]
friends.extend(ages)                     # to extend

friends.append("Musa")                   # to add new element to the end
friends.insert(1, "Zaur")                # to add element in particular position
friends.remove("Zaur")                   # to remove element
friends.clear()                          # to clear all elements
friends.pop()                            # to remove last element of the list
print(friends.index("Ayhan"))            # to check position of element
friends.count("Kamil")                   # to count the number of element in the list
friends.sort()                           # to sort list in alphabetic order
friends.reverse()                        # to reverse
friends.copy()                           # to copy

# Working with tupples

coordinates = (4, 5)
"""coordinates[0] = 10 - this will not gonna work because you cannot change tuple"""

# Functions

def say_hi():                        # basic function
    print("Hello friend!")

say_hi()

def say_hi(name):                    # function + 1 parametre
    print("Hello!" + name)

say_hi("Kamil")

def say_hi(name, age):               # function + 2 parametres
    print("Hello! " + name, "you are " + age)

say_hi("Kamil", "23")
say_hi("Tarhan", "25")

def say_hi(name, age):
    print("Hello! " + name, "you are " + str(age))   #converted age

say_hi("Kamil", 23)
say_hi("Tarhan", 25)

# Return in Functions

def cube(num):
    return num*num*num

print(cube(3))

# If Statement

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short man")
elif is_tall and not(is_male):
    print("You are male but not tall")
else:
    print("You are not tall and a male")

# If Statements and Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
# Advanced calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")

# Dictionaries

months_conversations = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(months_conversations["Jan"])            # to have an acces to key of "Jan"
print(months_conversations.get("Jan"))        # the same thing but with feature, when we enter something what
print(months_conversations.get("Jul"))        # is not in our dictionary it shows us "None"
print(months_conversations.get("Jul", "Not in our dictionary"))

# While Loops

i = 1
while i <= 10:                                # loop will be reapeated till condition "i <= 10" is "True"
    print(i)
    i += 1

print("Done with loop!")

# Building a Guessing Game

secret_word = "180"                      #simple game
guess_count = 0
guess = ""

while guess != secret_word:
    guess = input("Guess my height: ")

print("You Win!")


secret_word = "180"                       # modyfied game
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess my height: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses! You Lost!")
else:
    print("You Win!")

# For Loop

for letter in "Kamil is learning":
    print(letter)

friends = ["Kamil", "Ayhan", "Tarhan"]
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First number")
    else:
        print("Not a first number")


# Exponent Function

print(2**3)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = base_num * result
    return result

print(raise_to_power(3, 5))

# 2D Lists and Nested Loops

num_grid = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8],
    [0]
]

print(num_grid[2][2])

for row in num_grid:
    for col in row:
        print(col)

# Building a translator


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeuio":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
    

print(translate(input("Enter your word: ")))

# Try except

try:
    number = int(input("Enter your number: "))
    print(number)

except:
    print("Invalid Input")


try:
    answer = 10/0
    number = int(input("Enter your number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
    

# Readind Files

open("employees.txt", "r")                  # open in reading mode
open("employees.txt", "w")                  # open in writing mode
open("employees.txt", "a")                  # to add info to the file (not possible to modify existing info)
open("employees.txt", "r+")                 # open in reading and writing mode

employee_file = open("employees.txt", + "r")

print(employee_file.readable())             # to check is it readable
print(employee_file.read())                 # to read

print(employee_file.readline())             # to read first line
print(employee_file.readline())             # every next time to check next line
print(employee_file.readlines())            # taking all lines and putting in a list
print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

# Writing in Files

employee_file = open("employee.txt", "a")

employee_file.write("Toby - Human Resources")         # to add new
employee_file.write("\nKelly - Customer Service")     # to add to a new line


employee_file = open("employee.txt", "w")             # when "w" it will overwrite in a file (text before will be removed)
employee_file.write("Toby - Human Resources")

employee_file = open("employee.txt1", "w")            # will create a new file

# Modules and Pip

"""import usefull_tools

print(usefull_tools.roll_dice(10))"""

# Classes and Objects (Object Functions)

from student import Student
student1 = Student("Jim", "Business", 3.1, False)
studen2 = Student("Pam", "Art", 2.5, True)

"""Needed to create student class!!!!!!!"""

print(student1.gpa)

print(student1.in_honor_roll())

# Building a Multiple Choise Quiz

from Question import Question

question_promts = [
    "What colors are apples?\n(a) Red/Green(b) Purple\n(c) Orange \n\n",
    "What colors are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What colors are strawberies\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

# Inheritance
