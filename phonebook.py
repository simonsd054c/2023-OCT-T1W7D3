from pprint import pprint

'''
List of dictionaries where each dictionary - detail of particular contact

[
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "12312312",
            "mobile": "213124"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Melbourne",
        "phone": {
            "home": "4123412",
            "mobile": "21312"
        }
    }
]
'''

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "12312312",
            "mobile": "213124"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Melbourne",
        "phone": {
            "home": "4123412",
            "mobile": "21312"
        }
    }
]

pprint(phonebook)

name = input("Enter name: ")
address = input("Enter address: ")
home = input("Enter home: ")
mobile = input("Enter mobile: ")

# # Create a dictionary
# contact_to_add = {
#     "name": name,
#     "address": address,
#     "phone": {
#         "home": home,
#         "mobile": mobile
#     }
# }

# # Append that to the list
# phonebook.append(contact_to_add)

# Append by creating a dictionary on the fly
phonebook.append(
    {
        "name": name,
        "address": address,
        "phone": {
            "home": home,
            "mobile": mobile
        }
    }
)

pprint(phonebook)


# Find a number in the phonebook

number_to_find = input("Enter a number to find: ")

def find_number(number):
    for phone_entry in phonebook:
        for phone_number_key in phone_entry["phone"]:
            print(phone_entry["phone"][phone_number_key])
            if (number == phone_entry["phone"][phone_number_key]):
                print("Number found")
                return
    
    print("Number not found")


find_number(number_to_find)