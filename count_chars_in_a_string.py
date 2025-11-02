text = input()
occurrences = {}
for char in text:
    if char != " ":
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
for char, occurrences in occurrences.items():
    print(f"{char} -> {occurrences}")

