file_handle = open("words.txt")

word_counts = dict()

for line in file_handle:
    words = line.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

max_word_count = None
max_word = None
for word, count in word_counts.items():
    if max_word_count is None or count > max_word_count:
        max_word_count = count
        max_word = word

print(max_word, max_word_count)
