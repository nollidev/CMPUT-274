# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

# "local" is the local address of the email
def verify_local(local):
    result = True # algorithm assumes innocent until proven guilty
    
    # for each character, evaluate if it's a permitted character
    for char in local:
        number = ord(char.lower())
        
        # the first range of numbers are all the lowercase numbers in ascii
        # the second range of numbers are all the numbers and permitted punctuation
        # refer to an ascii reference table for clarity
        if (number >= 97 and number <= 122) or (number >= 45 and number <= 57 and not number == 47):
            continue # affirm valid character, move on to next character
        else: result = False; break # does not evaluate further if condition met
            
    return result

# "tld" refers to the top-level domain
def verify_tld(tld):
    result = False # algorithm assumes guilty until proven innocent
    validDomains = ["com", "ca", "org", "net", "gov", "edu"]
    
    for domain in validDomains:
        if tld == domain: result = True; break # does not evaluate further
    
    return result

# "sld" refers to the second-level domain
# if true, string is forbidden
def verify_forbiddeness(sld):
    result = False # innocent until proven guilty
    forbiddenDomains = ["scam", "spam", "fakeemail", "trashmail", "pleasenotspam", 
                       "therealtaylorswift", "sendmoney"]
    
    for term in forbiddenDomains:
        if term == sld: result = True; break # does not evaluate further
    
    return result

def validate_email(email):
    result = "Valid" # innocent until proven guilty
    
    while True: # run until guilt assigned or analysis complete
        if email.count("@") != 1: result = "Invalid"; break # must contain exactly one "@"
        
        firstSplit = email.split("@")
        local, domain = firstSplit[0], firstSplit[-1]
        
        if verify_local(local) == False: result = "Invalid"; break
        if domain.count(".") < 1: result = "Invalid"; break # must contain at least one "."

        secondSplit = domain.split(".")
        topLvlDomain, secondLvlDomain = secondSplit[-1], secondSplit[0]

        if verify_tld(topLvlDomain) == False: result = "Invalid"; break
        if verify_forbiddeness(secondLvlDomain) == True: result = "Forbidden"; break

        break # if program reaches this point, email is valid

    print(result)

def main():
    # Takes in the input and stores the email addresses in a list
    emails = list(input().split())

    # Validate each email here
    for email in emails:
        validate_email(email)

if __name__ == "__main__":
    main()