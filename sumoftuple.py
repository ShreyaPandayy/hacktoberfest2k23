def summation(test_tup):

	# Converting into list
	test = list(test_tup)

	# Initializing count
	count = 0

	# for loop
	for i in test:
		count += i
	return count


# Initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))
