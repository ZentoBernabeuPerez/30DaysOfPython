my_age = 36
my_height = 1.8
complex_number = 4j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
print(f"The area of the triangle is ", 0.5 * base * height)

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print(f"The perimeter of the triangle is ", side_a + side_b + side_c)

rectangle_length = int(input("Enter length: "))
rectangle_width = int(input("Enter width: "))
print(f"The area of the rectangle is ", rectangle_length * rectangle_width)

radius = int(input("Enter radius: "))
print(f"The area of the circle is ", 3.14 * radius * radius)
print(f"The circumference of the circle is ", 2 * 3.14 * radius)

#not doing 8 and 9 because i dont know how to calculate slopes and eucledian things :D

x = -3
y = x ** 2 + 6 * x + 9
print(y)

print(f"dragon is a ",len("dragon")," letter word.")
print(f"python is a ",len("python")," letter word.")
print(len("python") != len("dragon"))


if "on" in "python" and "on" in "dragon":
	print(True)
phrase = "I hope this course is not full of jargon"
if "jargon" in phrase:
	print("There is a lot of jargon in the course")

if "on" not in "python" and "on" not in "dragon":
	print(True)
else:
	print(False)

length_in_str = str(float(len("python")))
print(type(length_in_str))

#checking if the remainder is 0, if its 0 then the number is even. 
checked_number = int(input("Give me a number: "))
if checked_number % 2 == 0:
	print("Even number")
else:
	print("Odd number")

print(7 // 3 == int(2.7))

print(type("10") == type(10))

print(int(9.8) == 10)


hours = int(input("Enter work hours: "))
rate = int(input("Enter rate per hour: "))
print(f"Your weekly earning is ", hours * rate, "€")


years = int(input("Write you age: "))
seconds_per_year = 31536000

if years and years < 100:
	print(seconds_per_year * years)
else:
	print("not real age")


for j in range(1, 6):
	print(j, 1, j, j * j, j * j * j)
		