min_age = 18
your_age = int(input("Say your age: "))
if your_age >= min_age:
	print("You can drive")
else:
	print(f"You need", min_age - your_age, "years more to drive.")

other_age = int(input("Say the age you want to be compared to: "))

if your_age > other_age:
	if your_age - other_age == 1:
		print("You are 1 year older than other age")
	else:
		print(f"You are", your_age - other_age, "years older than other age")
elif other_age > your_age:
	if other_age - your_age == 1:
		print("You are 1 year older than other age")
	else:
		print(f"You are", other_age - your_age, "years younger than other age")
else:
	print("You are both the same age")

n1 = int(input("say first number: "))
n2 = int(input("say second number: "))

if n1 > n2:
	print(f"number", n1, "is greater than", n2)
elif n2 > n1:
	print(f"number", n1, "is less than", n2)
else:
	print("both numbers are equal")

your_score = int(input("Give me your score: "))
if your_score > 100 or your_score < 0:
	print("not possible score")
elif your_score in range(90, 101):
	print("You have an A")
elif your_score in range(80, 90):
	print("You have an B")
elif your_score in range(60, 80):
	print("You have an C")
elif your_score in range(50, 60):
	print("You have an D")
elif your_score in range(0, 50):
	print("You have an F")

month = input("What month we are now?(only 3 first letters please) ")
if month == "dec" or month == "jan" or month == "feb":
	print("It's winter time!")
elif month == "mar" or month == "apr" or month == "may":
	print("It's spring!")
elif month == "jun" or month == "jul" or month == "aug":
	print("It's summer!")
elif month == "sep" or month == "oct" or month == "nov":
	print("Its autumn!")
else:
	print("not a month, sorry")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Add a fruit to the list: ")
if new_fruit in fruits:
	print("That fruit is already on the list")
else:
	fruits.append(new_fruit)
print(fruits)

person={
    'first_name': 'Zento',
    'last_name': 'Bernabéu',
    'age': 36,
    'country': 'Spain',
    'is_married': False,
    'skills': ['Kotlin', 'Python', 'SQL', 'Git', 'Android Studio'],
    'address': {
        'street': 'false street',
        'zipcode': '1234'
    	}
    }

if "skills" in person.keys():
   	print(person["skills"][2])
if "Python" in person["skills"]:
	print("Python")

if "Git" in person["skills"] and "SQL" in person["skills"] and  "Python" in person["skills"] and "Kotlin" in person["skills"] and "Android Studio" in person["skills"]:
	print("Full stack dev")
elif "Kotlin" in person["skills"] and "Android Studio" in person["skills"]:
	print("Mobile dev")
elif "Python" in person["skills"] and "SQL" in person["skills"]:
	print("Data scientist")

if "is_married" == True and "country" == "Finland":
	print("Asabeneh Yetayeh lives in Finland. He is married.")
else:
	print(f"This guy is ", person["first_name"], person["last_name"], "he lives in ", person["country"], "and he is not married")