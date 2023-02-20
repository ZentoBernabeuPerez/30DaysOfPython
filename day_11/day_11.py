def add_two_numbers(n1,n2):
	n3 = n1 + n2
	return n3

print(add_two_numbers(5, 6))

def calculate_are_of_circle(radius):
	area = 3.14 * radius * radius
	return area

print(calculate_are_of_circle(5))

def add_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total

print(add_all_nums(5, 6, 12, 7, 44, 98))

print("mir scheiss egal die fahrenheit")

def check_season(month):
	if month == "january":
		return "winter"

print(check_season("january"))

print("mir scheiss egal die slope")
print("mir scheiss egal die equation")

def print_list(lista):
	for element in lista:
		print(element)
mi_lista = ["rata", "candy", "tron"]

print_list(mi_lista)

def reverse_list(lista):
	reversed_list = []
	for element in lista:
		reversed_list = [element] + reversed_list
	return reversed_list

print(reverse_list(mi_lista))

def capitalize_item_list(lista):
	new_list = []
	for element in lista:
		new_list.append(element.capitalize())
	return new_list

print(capitalize_item_list(mi_lista))

def add_item(lista, item):
	lista.append(item)
	return lista

print(add_item(mi_lista, "kiba"))

def remove_item(lista, item):
	lista.remove(item)
	return lista

remove_item(mi_lista, "kiba")
print(mi_lista)

def sum_of_numbers(nrange):
	total = 0
	for i in range(0, nrange):
		total += i
	return total

print(sum_of_numbers(8))

def sum_of_odds(nrange):
	total = 0
	for i in range(0, nrange):
		if i % 2 != 0:
			total += i
	return total

def sum_of_evens(nrange):
	total = 0
	for i in range(0, nrange):
		if i % 2 == 0:
			total += i
	return total

print(sum_of_odds(12))
print(sum_of_evens(32))

def evens_and_odds(nrange):
	evens = 0
	odds = 0
	for i in range(0, nrange):
		if i % 2 == 0:
			evens += 1
		else:
			odds += 1

	return f"number of evens are", evens, "number of odds are", odds

print(evens_and_odds(12))

def factorial(num):
	fact = 1
	for i in range(1, num+1):
		fact = fact * i
	return fact

print(factorial(5))

lista_vacia = []

def is_empty(something):
	if len(something) == 0:
		print("is_empty")
	else:
		print("is not empty")

is_empty(mi_lista)
is_empty(lista_vacia)


