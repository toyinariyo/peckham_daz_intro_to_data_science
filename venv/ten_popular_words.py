import string

file_path = r"C:\GitHub\peckham_daz_intro_to_data_science\peckham_daz_intro_to_data_science\venv\beatrix_potter_fierce_bad_rabbit.txt"

with open(file_path, 'r') as file:
    text = file.read().lower()

for char in string.punctuation:
    text = text.replace(char, '')

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("Top 10 most common words:")
for word, count in top_words:
    print(f"{word}: {count}")
