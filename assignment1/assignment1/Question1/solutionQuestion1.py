# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

def verify_local(local):
    # for each character, evaluate if it's a permitted character
    result = "Valid"
    for char in local:
        number = ord(char.lower())
        # the first range of numbers are all the lowercase numbers in ascii
        # the second range of numbers are all the numbers and permitted punctuation
        if (number >= 97 and number <= 122) or (number >= 45 and number <= 57 and not number == 47):
            continue
        else: result = "Invalid"; break
            
    return result

def verify_tld(tld):
    result = "Invalid"
    valid_domains = ["com", "ca", "org", "net", "gov", "edu"]
    for domain in valid_domains:
        if tld == domain: result = "Valid"; break
    return result

def verify_forbiddeness(sld):
    result = "Valid"
    forbidden_domains = ["scam", "spam", "fakeemail", "trashmail", "pleasenotspam", 
                       "therealtaylorswift", "sendmoney"]
    for term in forbidden_domains:
        if term == sld: result = "Forbidden"; break
    return result

def validate_email(email):
    # Add your implementation in here
    result = "Valid"
    while True:
        if email.count("@") != 1: result = "Invalid"; break
        
        first_split = email.split("@")
        local, domain = first_split[0], first_split[-1]
        
        if verify_local(local) == "Invalid": result = "Invalid"; break
        if domain.count(".") < 1: result = "Invalid"; break

        second_split = domain.split(".")
        second_lvl_d, top_lvl_d = second_split[0], second_split[-1]

        if verify_tld(top_lvl_d) == "Invalid": result = "Invalid"; break
        if verify_forbiddeness(second_lvl_d) == "Forbidden": result = "Forbidden"; break

        break

    print(result)

def main():
    # Takes in the input and stores the email addresses in a list
    emails = list(input().split())

    # Validate each email here
    for email in emails:
        validate_email(email)
        # print(email)
    # print(emails)

if __name__ == "__main__":
    main()
