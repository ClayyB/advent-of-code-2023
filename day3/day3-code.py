import re

# Read in file
with open("day3/test.txt", 'r') as file:
    input = file.read()

regex_numbers = "\d+"
regex_symbols = "[^\d\.]"

symbol_adj = []
digit_positions = []

# Find the positions of all of the symbols and all positions adjacent
for i, line in enumerate(input.strip().split("\n")):
    for symbol in re.finditer(regex_symbols, line):
        column = symbol.start()
        for row in range(i-1, i+2):
            for col in range(column-1, column+2):
                symbol_adj.append((row, col))

print(symbol_adj)

# Find positions of all of the numbers
for j, line in enumerate(input.strip().split("\n")):
    for number in re.finditer(regex_numbers, line):
        print("Row:", j, "Number:", number.start(), number.end())
        first_digit = number.start()
        last_digit = number.end()
        position = list(range(first_digit, last_digit))
        digit_positions.append(position)

print(digit_positions)
# Check if any of the digits of a number appear in any of the symbol_adj positions
