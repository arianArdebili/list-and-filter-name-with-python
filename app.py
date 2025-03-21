import re  # Import regular expressions module

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):  ')
    name = input()

    # Check if the name starts with a space, special character, or number
    if re.match(r'^[^a-zA-Z]', name):  # Regex to check if the first character is NOT a letter
        print("Invalid name. Cat names must start with a letter.")
        continue

    if name == "":
        break

    catNames += [name]

print("The cats' names are: ")
for index, i in enumerate(catNames):
    print(f"{index + 1} cat name: {i}")

# Print the total number of valid cats
print(f"Total number of valid cats: {len(catNames)}")