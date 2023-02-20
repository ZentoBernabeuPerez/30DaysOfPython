it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Huawei", "Logitech", "Android", "Jetbrains"])
it_companies.remove("Facebook")
print(it_companies)
print("Difference between remove and discard is that discard will not raise an error if the item is not in the set")


C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
D = B.union(A)
print(C)
print(D)
print(A.symmetric_difference(B))
del A
del B
del C

age_set = set(age)
print(age_set)

print("Strings are chains of characters, list are a bunch of data listed it can be from any data type, tuple is the same as list but they are inmutable.\n Sets are like list but they cannot have the same item twice")
phrase = "I am a teacher and I love to inspire and teach people"
separate_words = set(phrase.split())
unique_words = set(separate_words)
print(separate_words)
print(len(separate_words))