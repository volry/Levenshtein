from fuzzywuzzy import process, fuzz
import pandas as pd

def find_most_accurate_name_and_calculate_similarity(names):
    # Step 1: Find the most accurate name without using list comprehensions
    total_distances = {}
    for name in names:
        total_distance = 0
        for other_name in names:
            if name != other_name:
                distance = process.extractOne(name, [other_name])[1]
                total_distance += distance
        total_distances[name] = total_distance

    most_accurate_name = min(total_distances, key=total_distances.get)

    # Step 2: Create a DataFrame with original names
    df = pd.DataFrame(names, columns=['Original Name'])
    df['Most Accurate Name'] = most_accurate_name

    # Step 3: Add a similarity score column without list comprehensions
    similarity_scores = []
    for original_name in df['Original Name']:
        similarity = fuzz.ratio(original_name, most_accurate_name)
        similarity_scores.append(similarity)
    
    df['Similarity Score'] = similarity_scores

    return df

# List of names with errors
names = [
    "Абдурашвидова Диана",
    "Абдурашвидова Диана Магомедовна",
    "Абдурашвідова Діана Магомедівна",
    "Абду Диана Магомедовна",
    "Абдурашвидова Диана Могамедовна",
    "Абдурашвідова Діана",
    "Абдурашвидова Діана"
]

# Example usage of the function
df = find_most_accurate_name_and_calculate_similarity(names)
print(df.to_string(index=False))

