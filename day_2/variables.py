#Day 2: 30 Days of programming
first_name = "Zento"
last_name ="Bernabéu Pérez"
full_name = first_name + last_name
country = "Japan"
city = "Tokyo"
age = 36
year = 1987
is_married = False
is_light_on = True
algo, otra_cosa, una_cosa_mas = "kotlin", "Rata", "Candy"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(algo))
print(type(otra_cosa))
print(type(una_cosa_mas))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two + num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

area_of_circle = 3.14 * (30 ** 2)
circum_of_circle = 3.14 * 30
print(area_of_circle)
print(circum_of_circle)
user_radius = int(input("Please write the radius: "))
user_area_of_circle = 3.14 * (user_radius ** 2)
print(user_area_of_circle)
user_first_name = input("Please write your name: ")
user_last_name = input("Please write your last name: ")
user_country = input("Please write your country: ")
user_age = input("Please write your age: ")

print(user_first_name + user_last_name + user_country + user_age)
help("keywords")