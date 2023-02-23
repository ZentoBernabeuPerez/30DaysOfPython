from functools import reduce
#the three of them needs a function and a list as parameters, map returns the result of all elements of the list through the function, 
#filter returns the elements that matches the function
#reduce returns only one parameter instead a list


#higher order functions are functions that receive or return another functions
#while closures are functions that have a function inside of them and return those functions
#decorators are functions that we can use to change things of another functions

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def function_to_map(n1):
	total = n1 + 5
	return total

number_list = map(function_to_map, numbers)
print(list(number_list))


def function_to_reduce(word1, word2):
	new_name = word1[0:5] + word2[2:4]
	return new_name


gen_name = reduce(function_to_reduce, names)
print(gen_name)

for i in countries:
	print(i) 


for i in names:
	print(i)


for i in numbers:
	print(i)


def decorator_function(function):
	def wrapper(*some):
		print("this thing happens before the function")
		algo = function(*some)
		print("this will be showed after the function")
	return wrapper


@decorator_function
def no_idea(something, otracosa):
	upper_something = something.upper()
	print(upper_something, otracosa) 


no_idea("a ver si esto funciona", "loco, loco")


def to_upper(something):
	uppered = something.upper()
	return uppered

new_country_list = map(to_upper,countries)
print(list(new_country_list))

def to_square(num):
	square_num = num ** 2
	return square_num

new_num_list = map(to_square, numbers)
print(list(new_num_list))

new_name_list = map(to_upper, names)
print(list(new_name_list))

def land_countries(country):
	if "land" in country:
		return True
	return False

land_countries_list = filter(land_countries, countries) 
print(list(land_countries_list))

def six_characters(country):
	if len(country) == 6:
		return True
	return False


six_characters_list = filter(six_characters, countries) 
print(list(six_characters_list))


def six_characters_or_more(country):
	if len(country) >= 6:
		return True
	return False


six_characters_or_more_list = filter(six_characters_or_more, countries) 
print(list(six_characters_or_more_list))

def function_to_filter(word):
	if "E" in word:
		return True
	return False

countries_list = filter(function_to_filter, countries)
print(list(countries_list))

def to_map(n1):
	n = n1 * n1
	return n

def to_filter(n1):
	if n1 % 2 == 0:
		return True 
	return False

def to_reduce(n1, n2):
	return n1 + n2

