import re

phone_regex = '^(\+\d{1,2}[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
phone_number = input("enter phone number")

match = re.search(phone_regex, phone_number)
if match:
    print(phone_number, "matched")
else:
    print(phone_number, "not matched")