#easy
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

print(merge_dictionaries(dict1, dict2))

#medium
from collections import defaultdict

def word_frequencies(text):
    words = text.split()
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    return dict(freq)

text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))

def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)

contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")

print(contacts)

