# function to validate username
def validate_username(username):
    if (username and username.isalpha()):
       return True
    else:
        return False
    
     
 
    

def validate_password(password):
    has_letter = False
    has_digit = False
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True


    if has_letter and has_digit:
        print("The string contains both letters and digits.")
    else:
        print("The string does not meet both criteria.")
    

username = input("Enter Username: ")

result = validate_username(username)
if(result):
    print("Üsername is Valid")
else:
    print("Invalid Username")


password = input("Enter Password: ")
validate_password(password)

