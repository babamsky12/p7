
def required_password(password):
    symbols = ['!', '”', '#', '$', '%', '&', '’', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '|', ']', '^', '_', '`', '}', '{', '~']
    value = True

    if len(password) <= 15:
        print ("Password must contain 16 characters.")
        value = False

    if not any (char.isupper() for char in password):
        print("The password must contain capital letters.")
        value = False

    if not any (char.isdigit() for char in password):
        print("The password must contain capital letters.")
        value = False
    
    if not any (char in symbols for char in password):
        print("Password must contain at least one symbol.")
        value = False

    return value

def log_in():
    password = input("Enter your password: ")
    if (required_password(password)):
        print("The password is valid.")
    else:
        print("The password is invalid.")


log_in_menu = log_in()
    
    

    

