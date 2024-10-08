# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string(string):
    newString = string
    peskyPunctuation = [".", ",", "!", "?", "\'"]
    for punctuation in peskyPunctuation:
        newString = newString.replace(punctuation, "")
    return newString

#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string(string):
    newString = ""
    splicedString = string.split()
    for i in range(len(splicedString)):
        if newString != "": newString += " "
        newString += splicedString[~i]
    return newString

#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates(string):
    newString = ""
    string_list = string.split()
    for word in string_list:
        if newString != "": newString += " "
        if word not in newString: newString += word
    return newString        
    
#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length(string):
    #Add your implementation here
    pass

def main():
    inputString = input()

    cleanInputString = clean_input_string(inputString)
    # print(cleanInputString)
    
    reversedString = reverse_string(cleanInputString)
    print(reversedString)
    
    reversedStringWithoutDuplicates = remove_duplicates(reversedString)
    print(reversedStringWithoutDuplicates)
    
    medianWordLength = calculate_median_length(reversedStringWithoutDuplicates)
    print(medianWordLength)

    
if __name__ == "__main__":
    main()

