original_file_path =  r"C:\GitHub\peckham_daz_intro_to_data_science\peckham_daz_intro_to_data_science\venv\beatrix_potter_fierce_bad_rabbit.txt"
new_file_path = r"C:\GitHub\peckham_daz_intro_to_data_science\peckham_daz_intro_to_data_science\venv\rabbit_story_edited.txt"

word_replacements = {
    'rabbit': 'tiger',
    'garden': 'jungle',
    'bad': 'vicious'
}

def replace_words(text, word_replacements):
    for old_word, new_word in word_replacements.items():
        text = text.replace(old_word, new_word)
    return text 

