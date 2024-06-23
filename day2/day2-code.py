# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:27:08 2023

@author: clari
"""

import re

# Read in file
with open("day2/input.txt", 'r') as file:
    input = file.read()

## Part 1

# Set maximum number of blocks in the bag
max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# Empty list of games
impossible_games = []
possible_games = []

for i, line in enumerate(input.strip().split("\n")):
    colours = re.findall(r'(\d+) (red|green|blue)', line)
    for col in colours:
        if max_colours[col[1]] < int(col[0]):
            impossible_games.append(i)
    if i not in impossible_games:
        possible_games.append(i+1)

part1_answer = sum(possible_games)

print(part1_answer)

## Part 2 
min_reds = []
min_greens = []
min_blues = []

reds = []
greens = []
blues = []

powers = []

for i, line in enumerate(input.strip().split("\n")):
    colours = re.findall(r'(\d+) (red|green|blue)', line)
    for col in colours:
        if col[1] == "red":
            reds.append(int(col[0]))
        if col[1] == "green":
            greens.append(int(col[0]))
        if col[1] == "blue":
            blues.append(int(col[0]))
    min_reds.append(max(reds))
    min_greens.append(max(greens))
    min_blues.append(max(blues))
    reds = []
    greens = []
    blues = []

for j in range(len(min_reds)):
    powers.append(min_reds[j] * min_greens[j] * min_blues[j])

part2_answer = sum(powers)

print(part2_answer)
