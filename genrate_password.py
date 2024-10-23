import random
import string
def generate_password(length):
    if length < 8 :
        print("Please Enter Password length above 7. ")
    else :
        print("Password : " + ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)))

length = int(input("Enter the desired length of the password: "))
generate_password(length)