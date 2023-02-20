for i in range(0, 10):
	print("loquesea")
count = 0
while count < 11:
	print("otra cosa")
	count += 1 

for i in range(0, 8):
	print("#" * i)

print("")

for i in range(0, 8):
   for j in range(8, 9):
      print("#" * j)


print("")
for i in range(0,11):
	print(f"", i, "X", i, "=", i * i)

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
	print(i)

for i in range(0, 101):
	if i % 2 == 0:
		print(i)

for i in range(0, 101, 2):
	print(i)

algo = 0
for i in range(0, 101):
	algo += i
print(f"sum of all numbers is", algo)

evens = 0
odds = 0
for i in range(0, 101):
	if i % 2 == 0:
		evens += i
	else:
		odds += i

print(f"The sum of all evens is ", evens, "and the sum of odd is ", odds)

fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit_list = []
for fruit in fruit_list:
	reversed_fruit_list = [fruit] + reversed_fruit_list
print(reversed_fruit_list)

