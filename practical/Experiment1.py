#variables
x = 21
print(x)
print(type(x))
print()

y=3.14
print(y)
print(type(y))
print()

name = "pavani"
print(name)
print(type(name))
print()

#conditional statements
age = 17
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
print()

#loops
for i in range(20):
    print(i)
print()

count = 3
while count < 6:
    print(count)
    count += 1
print()

#operators
a=21
b=3
print("Addition:", a + b)
print()
print("Subtraction:", a - b)
print()
print("Multiplication:", a * b)
print()
print("Division:", a / b)
print()
print("OR operator:", a|b)
print()
print("AND operator:", a&b)
print()

#lists(mutable)
movies = ["sita ramam", "Dragon", "lenin"]
print(movies)
movies.append("OG")
print(movies)
print()

#tuples(immutable)
fruits = ("mango", "apple", "guava")
print(fruits)
print()

#dictionaries
person = {
    "name": "Pavani",
    "age": 18,
    "city": "Hyderabad"
}
print(person)
print()