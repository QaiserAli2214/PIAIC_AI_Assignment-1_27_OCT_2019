# Here 2 Built in functions first is taking input value from user second is casting i-e converting string into integer
Number = int(input("Enter any number"))
print("The number you entered is", Number)


# 2 Built in functions i-e finding maximum and minimum of an array
Array = [1, 2, 3, 4, 5, 6, 7, 8]
Maximum_number = max(Array)
Minimum_number = min(Array)
print("Maximum number = ", Maximum_number , "Minimum number = ", Minimum_number)


# len function finds the length of any array or string here take input user name and print its length
Name = input("Enter your first name")
Length = len(Name)
print("The length of your first name = ", Length)


# bin will print the binary value of integer the user want
Value = bin(int(input("Enter the value you want binary number of ")))
print("Binary value is ", Value)


# complex function convert a number to complex number
comp = complex(3)
print("Complex number is ", comp)