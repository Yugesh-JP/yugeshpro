from spellchecker import SpellChecker
import csv

spell = SpellChecker()
corrected, suggestion = ([] for _ in range(2))

# find those words that may be misspelled
with open('Auto Check Python file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for text in csv_reader:
        misspelled = spell.unknown(text)

        for word in misspelled:
            # Get the one `most likely` answer
            correct = spell.correction(word)
            print(correct)
            corrected.append(correct)

            # Get a list of `likely` options
            suggest = spell.candidates(word)
            print(suggest)
            suggestion.append(suggest)

with open("new.csv", 'w',  newline='') as newfile:
    fieldnames = ['correction', 'suggestion']
    writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    writer.writeheader()
    for corrected, suggestion in zip(corrected, suggestion):
        writer.writerow({'correction': corrected, 'suggestion': suggestion})
