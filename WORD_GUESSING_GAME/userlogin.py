username = 'dev'
password = 'devhaspass'

attempts = 3



while(attempts > 0):
    usernameInput = input("enter your username: ")
    passwordInput = input ("enter a pass: ") 

    if(usernameInput == username) and (passwordInput == password):
        print("you are right")
        break
    else:
        attempts -= 1
        print("you are wrong!!")
        print(f"you have got {attempts} attempts left!")
        # break


if(attempts == 0):
    print("you have reached max limit, kindly contact the admin")