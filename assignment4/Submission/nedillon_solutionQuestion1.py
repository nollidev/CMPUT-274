# Name: Nathan Edillon 
# ccid: nedillon 
# studentId: 1826864 
# operating system: Fedora Linux 41
# python version: 3.13.0 

def alphabetical_sort(tupl):
    return tupl[0] # to sort the key-value pairs below, we refer to the key's index

def frequency_sort(tupl):
    return tupl[1] # to sort the key-value pairs below, we refer to the value's index

def analyze_character_frequencies(text):
    text_lower_alphanumeric = "".join([char for char in text.lower() if char.isalpha()]) # returns a string of all alphanumeric lowercase characters
    char_count = {char:0 for char in text_lower_alphanumeric} # mapping of each character initialized with zero occurrences
    for char in text_lower_alphanumeric: char_count[char] += 1 # add one for each character's occurrence in the string
    tuples = []
    for tupl in char_count.items(): tuples.append(tupl) # put each tuple from .items() into a proper list (so we can access its items)
    if len(tuples) == 0: return [] # for inputs with no alphanumeric characters
    else:
        tuples.sort(key=alphabetical_sort) # sort the mappings alphabetically
        tuples.sort(reverse=True,key=frequency_sort) # sort the mappings from greatest to least frequent
        return [tupl[0] for tupl in tuples] # final desired list 

def main():
    text = input()
    print(analyze_character_frequencies(text))

if __name__ == "__main__":
    main()
