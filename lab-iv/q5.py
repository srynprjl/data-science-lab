'''Use the re module to write a script that searches through a paragraph and extracts all words that start with an uppercase letter (e.g., "London", "Python") to identify proper nouns or sentence starters.'''
import re

text = input("Enter a text: ")
variable = re.findall(r'\b[A-Z][a-z]*\b', text)
print(variable)

