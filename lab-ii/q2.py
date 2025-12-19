paragraphs = input("Enter a paragraph: ").strip().split(" ")

word_freq = {}
for i in paragraphs:
    word_freq[i] = word_freq.get(i, 0) + 1

uw = list(set(paragraphs))
uw.sort()
count = len(uw)

print(f"Unique Words: {uw}")
print(f"Total unique words: {count}")
print(f"Word frequency : {word_freq}")
