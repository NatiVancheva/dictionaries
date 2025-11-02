phonebook = {}
while True:
    name_phone = input()
    if "-" not in name_phone:
        break
    name, phone = name_phone.split("-")
    phonebook[name] = phone

searches = int(name_phone)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        phone = phonebook[searched_name]
        print(f"{searched_name} -> {phone}")
    else:
        print(f"Contact {searched_name} does not exist.")


