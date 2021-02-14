import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def check(s):
    s = s.lower()

    if s in data:
        return data[s]

    # Check if there are any close matches to the given response
    elif len(get_close_matches(s, data.keys())) > 0:
        # if there are then loop over values, checking with user if that is the one they wanted
        for key in get_close_matches(s, data.keys()):
            check = input(f"Did you mean {key} instead? Y/N ")

            if check.lower() == "y" :
                return data[key]

        # if nothing is found then return not found 
        return "Word not found, please check input"
    else:
        return "Word not found, please check input"

word = input("Please enter a word: ")

print(check(word))