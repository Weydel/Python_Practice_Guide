# Python program for try & except

a = 10

# Normal exception capturing
try:
	result = a/0
except:
	print("Some error occured !!")


# # Capture all exceptions
try:
	print("Before divsion")
	result = a/0
	print("After divsion")
except Exception as err:
	print("Failed Execution - ",str(err))


# # Capture sepecific exception
try:
	print("Before divsion")
	result = a/0
	print("After divsion")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))


arr_list = [1,2,3,4,5]

try:
	print("10th Element - ",arr_list[9])
except Exception as err:
	print("Failed Execution - ",str(err))


name = input("Enter your name : ")
age = int(input("Enter your age : "))


try:
	if (age<18):
		raise Exception("Can not register for this application, Age must be greater than 18 !!")