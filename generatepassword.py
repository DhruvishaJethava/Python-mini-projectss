import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefhijkmnopqrstuwxyz!@#$%^&*(){}[]_-"
lenght_password=int(input("Enter the Lenght of the Password "))
a="".join(random.sample(password,lenght_password))
print(f"your password is {a}")
