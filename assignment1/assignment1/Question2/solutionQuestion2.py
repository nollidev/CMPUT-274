# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string():
    #Add your implementation here
    pass

#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string():
    #Add your implementation here
    pass

#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates():
    #Add your implementation here
    pass

#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length():
    #Add your implementation here
    pass

def main():
    inputString = input()
    
    reversedString = reverse_string()
    print(reversedString)
    
    reversedStringWithoutDuplicates = remove_duplicates()
    print(reversedStringWithoutDuplicates)
    
    medianWordLength = calculate_median_length()
    print(medianWordLength)

    
if __name__ == "__main__":
    main()

