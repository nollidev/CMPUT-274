# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux
# python version: 3.12.6

def verify_local(local):
    # for each character, evaluate if its ascii code is 
    # attributed to any of the permitted characters
    for char in local:
        number = ord(char.lower())
        if number < 97 or number > 122:
            code = "Invalid"
            break
        else:
            code = "Valid"
    return code

def verify_suffix(d_suffix):
    valid_domains = ["com", "ca", "org", "net", "gov", "edu"]
    for domain in valid_domains:
        pass

def validate_email(email):
    # Add your implementation in here
    code = "Valid"
    while True:
        if email.count("@") != 1: code = "Invalid"; break
        
        first_split = email.split("@")
        local, domain = first_split[0], first_split[-1]
        
        if verify_local(local) == "Invalid": code = "Invalid"; break
        if email.count(".") == 0: code = "Invalid"; break

        second_split = domain.split(".")
        top_lvl_d, d_suffix = second_split[0], second_split[-1]

        if verify_suffix(d_suffix) == "Invalid": break

        break

    print(code)

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
