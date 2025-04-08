import sys
import csv

def main():
    while True:
        choice = input("Login, Register or Quit? ").casefold()
        match choice:
            case "login":
                login()
                logged_in()
                break
            case "register":
                register()
                break
            case "quit":
                print("Program quitted")
                sys.exit()
            case _:
                continue

################################################################### need to change this to use source.csv
def login():
    # username part
    while True:
        found = False
        username = input("Username: ")
        with open("plain_text.txt", "r") as file:
            for line in enumerate(file):
                if line[1].split(",")[0] == username:
                    print("username found")
                    found = True
                    position = line[0]
                    break
        
        #flag thing should probably fix it coz its bad ish but it works
        if found:
            break
        else:
            print("username not found")
    

    #password part
    while True:
        found = False
        password = input("Password: ")
        with open("plain_text.txt", "r") as file:            
            #black magic but somehow i got the password from the text file
            if line[1].split(",")[1].rstrip() == password:
                print("correct password")
                found = True
                break

        if found:
            break
        else:
            print("username not found")

def logged_in():
    while True:
        choice = input("Change password or logout? ").casefold()
        match choice:
            case "change password":
                change_password()
                break
            case "logout":
                print("Logged out")
                print("Program quitted")
                sys.exit()
                break
            case _:
                continue


def register():
    while True:
        done = False
        username = input("Enter your username: ")
        with open("plain_text.txt", "r") as file:
            for line in file:
                if line.split(",")[0].rstrip() == username:
                    print("Username already taken")
            done = True

        if found:
            break
        else:
            print("username not found")

    password = input("Enter your password: ")

def change_password():
    print("change password")

main()