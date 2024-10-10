# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string(string):
    peskyPunctuation = [".", ",", "!", "?", "\'"]
    
    for punctuation in peskyPunctuation:
        string = string.replace(punctuation, "")
    
    return string

#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string(string):
    newString = ""
    splicedString = string.split()
    
    for i in range(len(splicedString)): # from first to last elmt in list splicedString
        if newString != "": newString += " " # add space where necessary
        newString += splicedString[~i] # from last to first elmt in list, add word into string newString
    
    return newString

#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates(string):
    newString = ""
    splicedString = string.split()
    nonDuplicates = []
    
    for word in splicedString:
        if word not in nonDuplicates: nonDuplicates.append(word)
    
    for word in nonDuplicates:
        if newString != "": newString += " " # add space where necessary
        newString += word
    
    return newString
    
#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length(string):
    characterCounts = []
    sentence = string.split()
    for word in sentence: characterCounts.append(len(word)) # assign the character count of each word
    characterCounts.sort()
    size = len(characterCounts)
    
    # the following is the algorithm that uses the median formula
    if size % 2 == 0: 
        median = (characterCounts[(size + 1) // 2] 
                + characterCounts[(size // 2)]) // 2
    else: median = characterCounts[(size + 1) // 2]
    
    return median

def main():
    inputString = input()

    cleanInputString = clean_input_string(inputString)
    
    reversedString = reverse_string(cleanInputString)
    print(reversedString)
    
    reversedStringWithoutDuplicates = remove_duplicates(reversedString)
    print(reversedStringWithoutDuplicates)
    
    medianWordLength = calculate_median_length(reversedStringWithoutDuplicates)
    print(medianWordLength)

    
if __name__ == "__main__":
    main()