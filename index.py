### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.

# userName = input("Enter your name: ")
# while userName != "q":
#    # if userName == "":
#     print(userName)
#     #you have to update the value in the condition
  




### Problem 3:
# Create a program that takes user input in a while loop. If they enter 1, print 1. If they enter 2, print 2. If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.
# 
# userNumber = input("Press 1, 2, 3, or q to quit: ")
# while userNumber != "q":
#     if userNumber == "1":
#         print("1")
#         print(userNumber)
#     elif userNumber == "2":
#         print("2")
#     elif userNumber == "3":
#         print("3")
#     else:
#         print("ERROR")
# # you have to update the value in the condition

### Problem 4:
# # Create a program that takes the user input until they enter 'q'. You should store all of their input and separate the input with a comma. Once they enter 'q', print all of the comma separated words they entered.
userInput = input("Enter a word. ")
listN = ""
while userInput != "q":
   listN = listN + "," + userInput
   userInput = input("Enter a word. ")
print(listN)