empty_list = []
five_item_list = [True, 3j, 3.8, 6, "rata"]
print(len(five_item_list))
print(five_item_list[0], five_item_list[2], five_item_list[4])
mixed_data_types = ("Zento Bernabéu Pérez", 36, 1.78, "single", "Elche")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
it_companies.insert(3, "JetBrains")
it_companies[0] = it_companies[0].upper()
print(it_companies)
print(";  ".join(it_companies))
print("Apple" in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies)
new_it_list = it_companies[0:3]
print(new_it_list)
last_three = it_companies[4:8]
print(last_three)
third_company = it_companies[3]
print(third_company)
del it_companies[0]
print(it_companies)
del it_companies[3]
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
full_stack = front_end
print(full_stack)
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)


#level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[0], ages[9])
ages.append(ages[0])
ages.append(ages[9])
print(ages[6])
print(sum(ages) / len(ages))
print(ages[11] - ages[0])
# I dont understand whats been asking for in this last point



