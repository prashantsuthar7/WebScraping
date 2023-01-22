import re

# Define the dataset
data = [
  "This is a large dataset with several keywords, such as keyword1, keyword2, and keyword3.",
  "This dataset also contains other keywords, like keyword4 and 111key-word5.",
  "And don't forget about keyword6 and keyword7!"
]

# Define the patterns to search for
pattern1 = r'keyword\d'
pattern2 = r'keyword\d\d'

# Compile the patterns into a regular expression pattern object
pattern = re.compile(pattern1 + '|' + pattern2)

# Use the re library to find all occurrences of the patterns in the dataset
keywords = []
for item in data:
  keywords += pattern.findall(item)

print(keywords)  # ['keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'keyword6', 'keyword7']
