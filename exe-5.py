password = input("Enter password ")
def validator_password(password):
    is_valid = True
    digits = 0
    if not 6 <= (len(password)) <=10 :
        print("password must be betwwen 6 and 10 char")
        is_valid = False
    
    if not password.isalnum():
            print("Password must consist only of letters and digits")
            is_valid = False
    for i in password:
        if i.isdigit():
            digits +=1
          
    if digits < 2:
            print("Password must have at least 2 digits")
            is_valid = False

    if is_valid :
        print("Password is valid")
validator_password(password)   