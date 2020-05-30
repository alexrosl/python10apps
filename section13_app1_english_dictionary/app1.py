import json
from difflib import get_close_matches

data = json.load(open("data.json"))
message_doesnt_exist = "The word doesn't exist. Please double check it."


def translate(w, dictionary):
    w = w.lower()
    # dict_lower = dict((k.lower(), v) for k,v in dictionary.items())
    matches = get_close_matches(w, dictionary.keys(), cutoff=0.8)
    if w in dictionary:
        return dictionary[w]
    elif w.title() in dictionary:
        return dictionary[w.title()]
    elif w.upper() in dictionary:
        return dictionary[w.upper()]
    elif len(matches) > 0:
        yes_no = input("Found a similar word %s. Do you want to translate it? Y/N: " % matches[0])
        if yes_no.upper() == "Y":
            return dictionary[matches[0]]
        elif yes_no == "N":
            return message_doesnt_exist
        else:
            return "We didn't understand your entry."
    else:
        return message_doesnt_exist


word = input("Enter word: ")
output = translate(word, data)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
