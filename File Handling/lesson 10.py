# From Andalusian Scholars to Digital Archives: The Evolution of Communication

# Andalusian Scholars: Basic print statement
# The pursuit of knowledge begins, echoing the wisdom of Andalusian scholars.
print("Greetings from Andalusia! The legacy of knowledge lives on.")

# The Great Libraries: Writing to a text file (Preserving knowledge)
with open("andalusian_scroll.txt", "w") as file:
    file.write("Scholars like Ibn Rushd and Al-Zahrawi changed the world with their wisdom.\n")

# Scribes and Manuscripts: Reading from a text file (Accessing knowledge)
with open("andalusian_scroll.txt", "r") as file:
    print("\nKnowledge from the scroll:", file.read())

# The Printing Press of Andalusia: Appending new data (Sharing new wisdom)
with open("andalusian_scroll.txt", "a") as file:
    file.write("The printing press allowed ideas to spread far and wide.")

# The Scientific Renaissance: Writing in CSV format (Structured knowledge)
import csv

with open("andalusian_science.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Field", "Scholar", "Contribution"])
    writer.writerow(["Astronomy", "Ibn Firnas", "Innovative flight experiments."])

# The Digital Archive: Using JSON format (Preserving the legacy in the modern era)
import json

knowledge = {
    "field": "Medicine",
    "scholar": "Al-Zahrawi",
    "contribution": "Pioneered surgical tools and techniques."
}

with open("andalusian_legacy.json", "w") as json_file:
    json.dump(knowledge, json_file)

# Reading from the JSON file (Accessing the digital archive)
with open("andalusian_legacy.json", "r") as json_file:
    print("\nMessage from the digital archive:", json.load(json_file))

# Ensuring proper knowledge preservation
print("\nThe wisdom of Andalusia is preserved in text, CSV, and JSON formats!")
