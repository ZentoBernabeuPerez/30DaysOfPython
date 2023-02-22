from random import sample
from random import randint
from random import shuffle

characters = "abcdefghijklmnopqrstuvwxyz1234567890"
characters_list =[]
for character in characters:
	characters_list.append(character)

def random_user_id():
	random_id = "".join(sample(characters_list, 6))
	return random_id

print("random id: ") 
print(random_user_id())


def random_id_gen_by_user():
	number_of_characters = int(input("¿how many characters do you want in your id? "))
	number_of_ids = int(input("¿how many ids do you want? "))
	random_id_list = []
	random_id =""
	for i in range(0, number_of_ids):
		random_id = "".join(sample(characters_list, number_of_characters))
		random_id_list.append(random_id)
	for i in range (0, len(random_id_list)):
		print(random_id_list[i])


print("the random id by user: ") 
random_id_gen_by_user()
print("till here")
print("")


def rgb_color_gen():
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	print(f"rgb(", red, ",", green, ",", blue, ")")

print("this a rgb color")
rgb_color_gen()


def generate_colors(mode, num):
	characters_for_hex = "abcdef1234567890"
	characters_list_for_hex =[]
	for chara in characters_for_hex:
		characters_list_for_hex.append(chara)
		random_color = []
	for i in range(0, num):
		if mode == "hexa":
			hexa_rgb = random_sample = "".join(sample(characters_list_for_hex, 6))
			random_color.append(hexa_rgb)
		elif mode == "rgb":
				red = randint(0, 255)
				green = randint(0, 255)
				blue = randint(0, 255)
				rgb_rgb = (red, green, blue)
				random_color.append(rgb_rgb)

	for i in range (0, num):
		print(f"", mode, random_color[i])


		
print("the hexa or rgb generator")
generate_colors("hexa", 5)
generate_colors("rgb", 8)

def shuffled_list(lista):
	shuffle(lista)
	return lista

print(shuffled_list(characters_list))

def array_of_seven_numbers():
	random_array = []
	while len(random_array) < 7:
		number = randint(0, 9)
		if number not in random_array:
			random_array.append(number)
	return random_array

print(array_of_seven_numbers())

