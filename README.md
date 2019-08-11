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

## Features

- Multi-threading
- Error handling
- Keylogger
- Screenshot
- Webcam-snapshot
- Report
- Clear tracking
- Kill switch
- Reverse shell with unicast addressing
- Reverse shell with multicast addressing
- Reverse shell with broadcast addressing
- Store data in mysql database 
- View data stored in the database
- See a list of connected targets
- View a list of connected targets information
- Download file from target system
- File upload to target system
- View the total number of connected targets
- View the target’s geographic location on the map
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
| Ctypes      | Gmplot          |

### For Rose

| **First Col**  | **Second Col** |
| ------------- | ------------- |
| Subprocess    | Json           |
| Platform      | Sys            |
| Requests      | OS             |
| Getpass       | Pygame         |
| Urllib2       | Pygame.camera  |
| Socket        | PyScreenshot   |
| Ctypes        | Pyxhook        |
| Time          | Win32api       |
| Win32console  | Win32gui       |
| PyHook        | Pythoncom      |
| MSS           | ----           |


## Notes

1. Change the IP address and port number on line 305 and 306.
2. The keylogging operation ends when your target presses the end button, then you can download the corresponding file from the target      system.
3. The blackrose database must be built before it is executed. (**Ex: create database blackrose;**)
4. If the database has a password, you must enter it in line 843.
5. It is not necessary to remind you that the MySQL database must be installed.
6. For **Windows** operating systems, libraries **MySQLdb and PyHook** must be **installed**.

## Help

| **Command** | **Description** |
| ------- | ----------- |                                      
| help or ? | Show this message |         
| info | View a list of connected targets information |  
| list | See a list of connected targets |   
| about | What is Black-Rose and who is the author of it |       
| location | View the target's geographic location on the map |                    
| store | Store data in mysql database |                
| counter | View the total number of connected targets |
| shutdown | Kill switch |
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

## Installation

```markdown
### For Windows

0. Download it
1. pip install --upgrade pip
2. Installing MySQL-python-1.2.3.win32-py2.7
2. pip install -r Black_Rose_requirements && pip install -r Windows_Rose_requirements

### For Linux

0. sudo apt-get install python-mysqldb
1. sudo pip install --upgrade pip
2. sudo git clone https://github.com/Sha2ow-M4st3r/Black-Rose.git
3. cd Black-Rose
4. sudo pip install -r Black_Rose_requirements.txt && pip install -r Linux_Rose_requirements.txt.txt
```

## Usage

```markdown
- Attacker system: Black-Rose.py
- Target system: Rose.py
```

## Screenshot

### On windows

![Screenshot](http://s8.picofile.com/file/8347888000/Main_page.png)


### On Linux

![Screenshot](http://s8.picofile.com/file/8347894542/Linux_Main_Page.png)


**Never forget: You Can't Run From Your Shadow. But You Can Invite It To Dance**
