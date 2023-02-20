empty_tuple = ()
my_sisters = ("Pili", "Maleni")
my_brothers = ("Jorge", "Pascual")
siblings = my_sisters + my_brothers
print(len(siblings))
siblings_list = list(siblings)
siblings_list.append("Vicente")
siblings_list.append("Magdalena")
my_family = tuple(siblings_list)
print(my_family)

s1, s2, b1, b2, p1, p2 = my_family
print(s1, s2, b1, b2, p1, p2)
fruit_tuple = ("banana", "apple", "orange")
veggie_tuple = ("cabbage", "cucumber", "potato")
meat_tuple = ("pork", "chicken", "salmon")
food_tuple= fruit_tuple + veggie_tuple + meat_tuple
print(food_tuple)
food_list = list(food_tuple)
print(food_list[0:3])
print(food_list[-4:-1])
del(food_tuple)

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

