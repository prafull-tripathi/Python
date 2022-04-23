# Python Program to Reverse a List using Recursion

# Define a Function
def reverse_list(NumList, i, j):
    if(i < j):
        NumList[i], NumList[j]= NumList[j], NumList[i]


NumList = []
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " %i))
    NumList.append(value)

# Print the List Entered By the User
print("\nOriginal List: ",NumList)

reverse_list(NumList, 0, Number - 1)
print("\nThe Result of a Reverse List =  ", NumList)