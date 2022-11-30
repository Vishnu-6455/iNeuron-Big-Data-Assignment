# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# ```
string_1 = 'iNeuron'
print(string_1*4)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
number_1 = int(input("Enter number to check whether it is odd or even:"))
if number_1 % 2 == 0:
    print(number_1," is even")
else:
    print(number_1," is odd")

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age = int(input("Enter age:"))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")


# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
temp = 0
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 2 == 0:
        temp = temp + i
print(temp)

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
number_1 = int(input("Enter 1st number to check the greatest among them:"))
number_2 = int(input("Enter 2nd number to check the greatest among them:"))
number_3 = int(input("Enter 3rd number to check the greatest among them:"))
if number_1 > number_2 and number_1 > number_3:
    print(number_1," is greatest among ", number_1, number_2, number_3)
elif number_2 > number_3:
    print(number_2," is greatest among ", number_1, number_2, number_3)
else:
    print(number_3," is greatest among ", number_1, number_2, number_3)

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
list1 = []
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        list1.append(i)
print(list1)
