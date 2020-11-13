# *********HOMEWORK*********

# #1 Multiply Vectors
# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# total = ""
# newList = []

# for element in list1:
#     for numb in list2:
#         if list1.index(element) == list2.index(numb):
#             total = element*numb
#             newList.append(total)
# print(f"{list1} x {list2} = {newList}")

# #2 Matrix Addition
# twoDimList1 = [ [1, 3], [2, 4] ]
# twoDimList2 = [ [5, 2], [1, 0] ]
# result = [ [0, 0], [0, 0] ]


# for outterIndex in range(len(twoDimList1)):
#     for innerIndex in range(len(twoDimList1[outterIndex])):
#         result[outterIndex][innerIndex] = twoDimList1[outterIndex][innerIndex] + twoDimList2[outterIndex][innerIndex]

# print(result)

# #3 Matrix Addition II
# twoDimList1 = [ [1, 3], [2, 4], [5, 7], [2, 2], [8, 1] ]
# twoDimList2 = [ [5, 2], [1, 0], [3, 4], [6, 9], [0, 7] ]
# result = []

# for outterIndex in range(len(twoDimList1)):
#     listOfSums = []
#     for innerIndex in range(len(twoDimList1[0])):
#             result.append(twoDimList1[outterIndex][innerIndex] + twoDimList2[outterIndex][innerIndex])
#     listOfSums.append(result)
# print(listOfSums)

#4 De-dup
# listWithDup = [1, 2, 2, 6, 3, 9, 0, 6, 3, 1]
# removingDup = set(listWithDup)
# listWithoutDup = list(removingDup)

# print(listWithoutDup)

# #5 Leetspeak
# normalString = input("Please input a paragraph of text: ")
# upperString = normalString.upper()
# upperList = list(upperString)
# newLetter = ""
# newList = []
# leetString = ""

# for letter in upperList:
#     if letter == "A":
#         newLetter = 4
#         newList.append(newLetter)
#     elif letter == "E":
#         newLetter = 3
#         newList.append(newLetter)
#     elif letter == "G":
#         newLetter = 6
#         newList.append(newLetter)
#     elif letter == "I":
#         newLetter = 1
#         newList.append(newLetter)
#     elif letter == "O":
#         newLetter = 0
#         newList.append(newLetter)
#     elif letter == "S":
#         newLetter = 5
#         newList.append(newLetter)
#     elif letter == "T":
#         newLetter = 7
#         newList.append(newLetter)
#     else:
#         newLetter = letter
#         newList.append(newLetter.lower())

# # leetString = "".join(newList)  -- did not work
# leetString = "".join([str(character) for character in newList])

# print(leetString) 

# #6 Long-long Vowels
# string1 = input ("Please enter word: ")
# list1 = list(string1)
# newList = []
# newString = ""
# vowels = ['a', 'e', 'i', 'o', 'u']
# last_char = None

# for i in range(len(string1)):
#     if i!= 0 and string1[i] in vowels and string1[i] == string1[i - 1]:
#         newString += string1[i] * 3
#     newString += string1[i]
    
# print(newString)

# #7 Caesar Cipher
# normString = input("Please enter string: ")
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# decipherString = ""

# for letter in normString:
#     if letter != " ":
#         index = alphabet.index(letter)
#         new_index = (index + 13) % 26
#         new_char = alphabet[new_index]
#     else:
#         new_char = " "
#     decipherString += new_char    

# print(decipherString)















