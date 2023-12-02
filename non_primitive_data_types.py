# List - collection of data - mutable (changed) - indexed

list_of_numbers = [ 12, 35, 21, 6, 78 ]
#                   0   1   2   3   4

print(list_of_numbers[2])

list_of_numbers[4] = 62

print(list_of_numbers)

list_of_numbers.append(35)

print(list_of_numbers)

list_of_numbers.pop()

print(list_of_numbers)



# Tuple - collection of data - immutable (cannot change) - indexed

days_of_the_week = ( "Monday", "Tuesday", "Wednesday" )
#                       0           1           2

print(days_of_the_week[1])

# days_of_the_week[1] = "Friday"     cannot do this




# Set - collection of data - mutable (change) - not indexed - no repeated items

names = { "John", "Mike", "Mark", "Jane", "Mike", "Mike", "Mark" }
print(names)

names.add("Steve")
print(names)

names.remove("John")
print(names)

names.add("Jane")
print(names)

print("Jane" in names)
print("Simon" in names)

# Set operations - similar to mathematics set operations

a = { 1, 2, 3, 4, 5 }
b = { 4, 5, 6, 7, 8 }

u = a.union(b) # A union B = B union A = b.union(a)
print(u)

i = a.intersection(b) # A intersection B = B intersection A = b.intersection(a)
print(i)

dab = a.difference(b) # A - B
print(dab)

dba = b.difference(a) # B - A
print(dba)



# Dictionaries - collection of data - mutable(change) - key value pair - keyed

person1 = {
    "name": "Steve",
    "surname": "Smith",
    "age": 34,
}

print(person1)
print(person1["name"])
print(person1.get("age"))
# print(person1["address"])
print(person1.get("address", "No address at the moment"))

person1["address"] = "Sydney"
print(person1)

person1["age"] = 35
print(person1)

# Loops

print("Loop started below: \n")
for key in person1:
    print(f"Key: {key}")
    print(f"Value: {person1[key]}\n")