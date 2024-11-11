import time
from random import randint as random

password_txt = open(r"passwords_file.txt", "a")


def generate_password():
    password = ""

    name_password = input("Please, enter NAME for password: ")

    try:
        len_password = int(input("Please enter the LENGTH of the password: "))
    except:
        print("You should use only numbers to indicate length!")
        len_password = int(input("Please enter the LENGTH of the password: "))

    try:
        special_characters = int(input("Use other CHARACTERS (like '$&')? (YES - 1 | NO - 0): "))
    except:
        print("You must use only numbers to select the mode!")
        special_characters = int(input("Use other CHARACTERS (like '$&')? (YES - 1 | NO - 0): "))

    if special_characters == 1:
        characters = "qwertyuiop[]\!@#$%^&*()asdfghjkl;'zxcvbnm,./1234567890-=_+}{|:<>?"
    elif special_characters == 0:
        characters = "qwertyuiopasdfghjklxcvbnm1234567890"

    time.sleep(0.1)

    for i in range(len_password):
        password += f"{characters[random(0, len(characters)-1)]}"

    print("Loading...")
    time.sleep(0.5)

    sub_result = f"{name_password}: {password}"

    print(sub_result)

    # --------- QUESTIONS ---------
    try:
        save_or_no = int(input("Save this password? (YES - 1 | NO - 0): "))
    except:
        print("You must use only numbers to save password!")
        save_or_no = int(input("Save this password? (YES - 1 | NO - 0): "))

    if save_or_no == 1:
        print("Loanding...")
        print(sub_result, file=password_txt)
        time.sleep(0.6)
        return "Ready!"

    if save_or_no == 0:
        print("Please, repeat the data!")
        generate_password()
        return "Ready!"


print(generate_password())
