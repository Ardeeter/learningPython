# **********SMALL**********


# #1 Madlib Function
# def madlib (name, subject):
#     print (f"{name}'s favorite subject is {subject}.")

# name1 = input("Please enter a name: ")
# subject1 = input("Please enter a subject: ")

# madlib(name1, subject1)

# #2 Celsius to Fahrenheit Conversion
# def celsiusToFahrenheit (celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(fahrenheit)

# celsius1 = int(input("Please enter degrees in Celsius: "))
# celsiusToFahrenheit(celsius1)

#3 Fahrenheit to Celsius Conversion
# def fahrenheitToCelsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     print(celsius)

# fahrenheit1 = int(input("Please enter degrees in Fahrenheit: "))
# fahrenheitToCelsius(fahrenheit1)

# #4 is_even Function
# def is_even(number):
#     if number != 0 and number % 2 == 0:
#         return True    
#     else:
#         return False

# number1 = int(input("Please enter a number: "))
# print (is_even(number1))

#5 is_odd Function
# def is_odd(number):
#         if number != 0:
#             return not(is_even(number))

# number1 = int(input("Please enter a number: "))
# print(is_odd(number1))

#6 only_evens Function
# def only_evens(listOfNumbers):
#     listOfEvens = []
#     for number in listOfNumbers:
#         if is_even(number) == True:
#             listOfEvens.append(number)
#     return listOfEvens

# listOfNumbers1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(only_evens(listOfNumbers1))

# #7 only_odds Function
# def only_odds(listOfNumbers):
#     listOfOdds = []
#     for number in listOfNumbers:
#         if is_odd(number) == True:
#                 listOfOdds.append(number)
#     return listOfOdds

# listOfNumbers1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(only_odds(listOfNumbers1))


# **********MEDIUM**********


#1 Find the Smallest Number
# def smallest(listOfNumbers):
#     sortedNumbers = sorted(listOfNumbers)
#     return sortedNumbers[0]

# OR

# def smallest(listOfNumbers):
#     minNumber = min(listOfNumbers)
#     return minNumber

# OR

# def smallest(listOfNumbers):
#     result = listOfNumbers[0]
#     for number in listOfNumbers:
#         if number < result:
#             result = number
#     return result


# listOfNumbers1 = [-1, 4, 8, 2, 9, 3, 10, 6, 15, 34, 0]
# print(smallest(listOfNumbers1))

#2 Find the Largest Number
# def largest(listOfNumbers):
#     sortedNumbers = sorted(listOfNumbers)
#     return sortedNumbers[-1]

# OR

# def largest(listOfNumbers):
#     maxNumber = max(listOfNumbers)
#     return maxNumber

# OR

# def largest(listOfNumbers):
#     result = listOfNumbers[0]
#     for number in listOfNumbers:
#         if number > result:
#             result = number
#     return result

# listOfNumbers1 = [4, 8, 2, 9, 3, 10, 6, 15, 34, 0]
# print(largest(listOfNumbers1))

#3 Find the shortest String
# def shortest(listOfStrings):
#     minString = min(listOfStrings, key=len)
#     return minString

# OR

# def shortest(listOfStrings):
#     result = listOfStrings[0]
#     for string in (listOfStrings):
#         if len(string) < len(result):
#             result = string
#     return result

# listOfStrings1 = ["hi", "hello", "bye", "goodbye"]
# print(shortest(listOfStrings1))

#4 Find the Longest String
# def longest(listOfStrings):
#     maxString = max(listOfStrings, key=len)
#     return maxString

# OR

# def longest(listOfStrings):
#     result = listOfStrings[0]
#     for string in listOfStrings:
#         if len(string) > len(result):
#             result = string
#     return result

# listOfStrings1 = ["hi", "hello", "bye", "goodbye"]
# print(longest(listOfStrings1))


# **********LARGE**********


# # #1 Tic-Tac-Toe
# def move(board, location, player):
