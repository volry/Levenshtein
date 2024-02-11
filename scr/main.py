from fuzzywuzzy import process

names = [
    "Абдурашвидова Диана",
    "Абдурашвидова Диана Магомедовна",
    "Абдурашвідова Діана Магомедівна",
    "Абду Диана Магомедовна",
    "Абдурашвидова Диана Могамедовна",
    "Абдурашвідова Діана",
    "Абдурашвидова Діана"
]

# Calculate the total Levenshtein distance of each name to all others
total_distances = {name: sum(process.extractOne(name, [n for n in names if n != name])[1] for n in names if n != name) for name in names}

# Identify the name with the smallest total distance to all others
most_accurate_name = min(total_distances, key=total_distances.get)

print(f"Most accurate name: {most_accurate_name}")
