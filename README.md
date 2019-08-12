# Black-Rose
![Screenshot](http://s8.picofile.com/file/8347875142/BlackRose.png) 

Black-Rose is a cross platform python remote access torjan which
allows you to access the command line of windows and linux series with unicast, multicast and broadcast methods.

## What is Remote Access Trojan (RAT)

A Remote Access Trojan (RAT, sometimes called Creepware) is a type of malware that controls a system through a remote network connection. A RAT is typically installed without the victim's knowledge, often as payload of a Trojan horse, and will try to hide its operation from the victim and from security software and other anti-virus software

![Screenshot](http://s8.picofile.com/file/8347874750/BasicRatDesign.png)

## What is reverse shell

![Screenshot](http://s9.picofile.com/file/8347873500/ReverseShell.png)

## What is Addressing methods

### Unicast addressing

Uses a one-to-one association between a sender and destination: each destination address uniquely identifies a single receiver endpoint.

![Screenshot](http://s8.picofile.com/file/8347875968/Unicast.png)

### Multicast addressing

uses a one-to-many-of-many or many-to-many-of-many association, datagrams are routed simultaneously in a single transmission to many recipients.

![Screenshot](http://s9.picofile.com/file/8347876276/Multicast.png)

### Broadcast addressing

uses a one-to-all association, a single datagram from one sender is routed to all of the possibly multiple endpoints associated with the broadcast address.

![Screenshot](http://s9.picofile.com/file/8347876242/Broadcast.png)

## Challenge–response authentication protocol

In computer security, challenge–response authentication is a family of protocols in which one party presents a question ("challenge") and another party must provide a valid answer ("response") to be authenticated.

The simplest example of a challenge–response protocol is password authentication, where the challenge is asking for the password and the valid response is the correct password.

Clearly an adversary who can eavesdrop on a password authentication can then authenticate itself in the same way. One solution is to issue multiple passwords, each of them marked with an identifier. The verifier can ask for any of the passwords, and the prover must have that correct password for that identifier. Assuming that the passwords are chosen independently, an adversary who intercepts one challenge–response message pair has no clues to help with a different challenge at a different time. 

![Screenshot](http://s5.picofile.com/file/8369396650/Chapter9_html_36614039.jpg)

## Base features

- Multi-threading
- Error handling
- Keylogger
- Screenshot
- Webcam-snapshot
- Reporting
- Reverse shell with Unicast,Multicast,Broadcast addressing
- Works with MySQL database
- Download/Upload file
- Scan famous ports of protocols (You can add another port to the list)

## Modules used

### For Black-Rose

| **First Col**  | **Second Col** |
| ------------- | ------------- |
| Subprocess  | Queue           |
| Threading   | Time            |
| Colorama    | Json            |
| Platform    | Sys             |
| MySQLdb     | OS              |
| Socket      | PrettyTable     |
| Urllib2     | Termcolor       |
| Ctypes      | Getpass         |
| Netifaces   | Hashlib         |
| Base64      | Hmac            |
| UUID        | Crypto          |

### For Rose

| **First Col**  | **Second Col** |
| ------------- | ------------- |
| Subprocess    | Json           |
| Platform      | Sys            |
| Requests      | OS             |
| Getpass       | Pygame         |
| Urllib2       | Pygame.camera  |
| Socket        | PyScreenshot   |
| Hmac          | Pyxhook        |
| Time          | Win32api       |
| Win32console  | Win32gui       |
| PyHook        | Pythoncom      |
| MSS           | Hashlib        |
| Base64        | Crypto


## Notes - Black-Rose

1. Change the IP address and port number on line 1411.
2. Set your database configuration on line 1429.
3. The keylogging operation ends when your target presses the end button, then you can download the corresponding file from the target      system.
4. The keys are encrypted by the base64 algorithm. You must to decrypt it.

## Notes - Rose

1. Change the IP address and port number on line 451

## Help

| **Command** | **Description** |
| ------- | ----------- |                                      
| help or ? | Show this message |         
| show info |  Show all connected targets information. |  
| show list | Show all connected targets |   
| show sysinfo | Show system information |
| show interfaces | Show all connected interfaces information |
| show database | Show all stored data in mysql database |
| about | What is Black-Rose and who is the author of it |                         
| store | Store data in mysql database |                
| clear | Fresh terminal |
| portscan | Scan famous ports of protocols (You can add another port to the list) |
| select | Reverse shell with unicast addressing |
| range | Reverse shell with multicast addressing |
| broadcast | Reverse shell with broadcast addressing |
| download | Download file from target system |
| upload | File upload to victim system |
| database | View data stored in the database |
| keylogger | Keylogging |
| screenshot | Take screenshot |
| webcapture | Take picture with target webcam |

## Installation & Usage

```markdown
### For Windows

STEP-0. Download it
STEP-1. pip install --upgrade pip
STEP-2. Installing MySQL-python-1.2.3.win32-py2.7, pycrypto-2.6.1.win32-py2.7
STEP-3. Run Modules.py
STEP-4. pip install -r Black-Rose-Requirements.txt (If built)
STEP-5. Register: python BRR.py
STEP-6. Decode IV, AES KEY, Shared Secret KEY in python interpreter
STEP-7. Copy IV, AES KEY, Shared Secret KEY in Rose.py
STEP-8. Run Black-Rose.py

### For Linux

STEP-0. sudo git clone https://github.com/Sha2ow-M4st3r/Black-Rose.git
STEP-1. pip install --upgrade pip
STEP-2. Run Modules.py
STEP-3. pip install -r Black-Rose-Requirements.txt (If built)
STEP-4. Register: python BRR.py
STEP-5. Decode IV, AES KEY, Shared Secret KEY in python interpreter
STEP-6. Copy IV, AES KEY, Shared Secret KEY in Rose.py
STEP-7. Run Black-Rose.py

```

## Screenshot

### On windows

![Screenshot](http://s3.picofile.com/file/8369397226/Screenshot_4.png)


### On Linux

![Screenshot](http://s2.picofile.com/file/8369397292/Screenshot_7.png)


**Never forget: You Can't Run From Your Shadow. But You Can Invite It To Dance**
