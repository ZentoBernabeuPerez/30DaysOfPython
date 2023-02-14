phrase1 = "Thirty " + "Days " + "Of " + "Python"
print(phrase1)

phrase2 = "Coding " + "For " + "All"
print(phrase2)

company = phrase2

print(company)

print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.index("Coding"))
print(company.replace("Coding", "Python"))
print(company.replace("All", "Everyone"))
print(company.index("C"))
print(company.index("F"))
print(company.rfind("i"))
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))
print("You cannot end a sentence with because because because is a conjunction"[31:54])

#28 yes
#29 no

print(" Coding For All "[1:-1])

#31 the second one
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(python_libraries)
print(result)
print("I am enjoying this challenge. \nI just wonder what is next.")
print("Name \tAge \tCountry \tCity \nZento \t36 \t\tSpain \t\tElche")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius ", radius, " is ", area, " meters square.")

print("8 + 6 =", 8 + 6)
print("8 - 6 =", 8 - 6)
print("8 * 6 =", 8 * 6)
print("8 / 6 =", 8 / 6)
print("8 % 6 =", 8 % 6)
print("8 // 6 =", 8 // 6)
print("8 ** 6 =", 8 ** 6)