dog = {}
dog["name"] ="Rata"
dog["age"] = 1
dog["breed"] = "Not Known"
dog["legs"] = 4
dog["color"] = "FFFFFF"
student = {"first_name":"zento", "last_name":"bernabéu", "gender":"male", "age":36, "skills":"cooking"}
print(dog)
print(student)
print(len(student))
print(type(student["skills"]))
student["skills"] = ("cooking", "coding", "languages")
print(student["skills"])
student_keys = student.keys()
student_values = student.values()
print(student_keys)
print(student_values)
print(student.items())
del(student["age"])
print(student)
del(student)
