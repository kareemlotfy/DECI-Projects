# Question 1
# Validates input types.
def name(a,b,c):
	if type(a) == int and type(b) == int and type(c) == str:
		print("Input is Valid")
	else:
		print("None")

name(1,2,"name")


# Question 2
# Basic calculator operations.
def calculator(a,b,c):
	num1 = a 
	num2 = b 
	operator = c 
	if operator == 'add':
		sum = num1 + num2
		return sum
		
	elif operator == 'subtract':
		sum = num1 - num2 
		return sum
	elif operator == 'multiply':
		sum = num1 * num2
		return sum
	elif operator == 'division':
		sum = num1 / num2 
		return sum

print(calculator(3,5,'add'))
print(calculator(3,5,'subtract'))
print(calculator(3,5,'multiply'))
print(calculator(3,5,'division'))


# Question 5
# Classifies age into categories.
def age(num):
	if num<=10:
		print('Child')
	elif num>10 and num<21:
		print('Teenager')
	else:
		print('Adult')

age(4)
age(20)
age(40)

# Question 3
# Counts vowels in a string.
def count_vowles(a):
	ctr = 0 
	vowles = ['a', 'e', 'i', 'o','u']
	for i in a:
		if i in vowles:
			ctr = ctr +1 
	print(ctr)


count_vowles("azcbobobegghak")

# Question 4


	