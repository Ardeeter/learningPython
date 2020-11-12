# #**********SMALL**********

# #1 Hello You!
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# #2 HELLO YOU!
# name = input("WHAT IS YOUR NAME? ")
# nameCap =  name.upper()
# print (f"HELLO, {nameCap}!\nYOUR NAME HAS {len(name)} LETTERS IN IT! AWESOME!") 

# #3 Madlib
# print("Please fill in the blanks below: \n____(name)____'s favorite subject in school is ___(subject)___." )
# name = input("What is a name? ")
# subject = input("What is a subject:? ")
# print(f"{name}'s favorite subject in school is {subject}.")

# #4 Day of the Week
# day = int(input('Day (0-6)? '))
# if day == 0:
#     print("Sunday")
# if day == 1:
#     print("Monday")
# if day == 2:
#     print("Tuesday")
# if day == 3:
#     print("Wednesday")
# if day == 4:
#     print("Thursday")
# if day == 5:
#     print("Friday")
# if day == 6:
#     print("Saturday")

# #5 Work or Sleep In?
# day = int(input('Day (0-6)? '))
# if day == 0 or day == 6:
#     print("Sleep in")
# else:
#     print("Go to work")

# # 6 Celsius to Fahrenheit
# temp = int(input("Temperature in Celsius: "))
# fahrenheit = (temp * 9/5) + 32
# print(f"{fahrenheit} F")

# # 7 Looping from 1 to 10
# for i in range(1,11):
#     print(i)

# #8 n to m
# start = int(input("Start from: "))
# end = int(input("End on: "))
# for i in range(start,(end + 1)):
#     print(i)

# #9 Print a Square
# for i in range(5):
#     for x in range(5):
#         print("*", end="")
#     print()

# #10 Print a Square II
# n = int(input("How big is the square? "))
# for i in range(n):
#     for x in range(n):
#         print("*", end="")
#     print()

# #**********MEDIUM**********

# #1 Tip Calculator
# total = float(input("Total bill amount? "))
# service = input("Level of service? ")

# if service == "good":
#     tip = float(total * .20)
#     final = tip + total

# elif service == "fair":
#     tip = float(total * .15)
#     final = tip + total

# elif service == "bad":
#     tip = float(total * .10)
#     final = tip + total

# tip = ("%.2f" % tip)
# final = ("%.2f" % final)

# print (f"Tip amount: ${tip}\nTotal amount: ${final}")

# # 2 Tip Calculator 2
# total = float(input("Total bill amount? "))
# service = input("Level of service? ")
# numOfSplit = int(input("Split how many ways? "))

# if service == "good":
#     tip = float(total * .20)
#     final = tip + total
#     split = final / numOfSplit


# elif service == "fair":
#     tip = float(total * .15)
#     final = tip + total
#     split = final / numOfSplit

# elif service == "bad":
#     tip = float(total * .10)
#     final = tip + total
#     split = final / numOfSplit

# tip = ("%.2f" % tip)
# final = ("%.2f" % final)
# split = ("%.2f" % split)

# print (f"Tip amount: ${tip}\nTotal amount: ${final}\nAmount per person: $ {split}")

# #3 How many coins?
# coins = 0
# anwser = "yes"
# while anwser == "yes":
#     print(f"You have {coins} coins.")
#     anwser = input("Do you want another? ")
#     coins += 1

# print("Bye")

# #4 Print a Box
# width = int(input("Width? "))
# height = int(input("Height? "))

# for i in range(height):
#     for j in range(width):
#         if i == 0 or i == (height - 1) or j == 0 or j == (width - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# #5 Print a Triangle
# for i in range(4):
#     print(' '*(4-i) + '*'*(2*i+1))

# #6 Multiplication Table
# x = 1
# for i in range (1,11):
#     for j in range(1,11):
#         total = i*j
#         print(f"{i} X {j} = {total}")
#     print()
    


