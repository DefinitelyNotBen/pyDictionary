import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def check(s):
    s = s.lower()

    if s in data:
        return data[s]

    elif len(get_close_matches(s, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(s, data.keys())[0]
    else:
        return "Word not found, please check input"

word = input("Please enter a word: ")

print(check(word))