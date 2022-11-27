# Python3.10

# Project: Find Missing Number in an List data-type

def MissingNumber(number):

	n = set(number)
	lenght = len(number)
	output = []
	for i in range(1,number[-1]):
		if i not in n:
			output.append(i)
	return output

number_list = [1,30]
print(MissingNumber(number_list))