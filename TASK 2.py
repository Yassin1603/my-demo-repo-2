# 1. Create a string `text` with the value "Python programming is powerful and versatile."
text = "Python programming is powerful and versatile."

# 2. Perform the following string operations and print the results:

# - Extract and print the substring "programming" using slicing
print(text[7:18])

#Split the string into a list of words.
print(text.split())

#Join the list of words back into a single string using a hyphen `-` as a separator.
print(*text, sep = '-')

# 3. Create a list `numbers` containing the elements: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].
# - Use list comprehension to create a new list `squares` containing the squares of each element in `numbers`.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
squares = [number ** 2 for number in numbers]

# - Print the `squares` list.
print(squares)