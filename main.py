import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


word = input("what is your name? ").upper()
new_dict = [phonetic_dict[letter] for letter in word]
print(new_dict)
