#! /usr/bin/python

import platform
import os

# Create requirements file
def Requirements(Module):
    try:
        if "Linux" in platform.platform():
            File = open(os.getcwd() + "/Black-Rose-Requirements.txt", "a")
            File.write(Module + "\n")
            File.close()
            return
        elif "Windows" in platform.platform():
            File = open(os.getcwd() + r"\Black-Rose-Requirements.txt", "a")
            File.write(Module + "\n")
            File.close()
            return
        else:
            print "Sorry, Operating system not defined."
    except IOError:
        print "Can't open requirements file."


def Black_ROSE():
    print "Installing MySQLdb"
    print "Installing PyCrypto"

    # Checking modules
    try:
        import colorama
    except ImportError:
        Requirements("colorama")
    try:
        import ctypes
    except ImportError:
        Requirements("ctypes")
    try:
        from termcolor import colored
    except ImportError:
        Requirements("termcolor")
    try:
        import subprocess
    except ImportError:
        Requirements("subprocess")
    try:
        import threading
    except ImportError:
        Requirements("threading")
    try:
        import netifaces
    except ImportError:
        Requirements("netifaces")
    try:
        import platform
    except ImportError:
        Requirements("platform")
    try:
        import urllib2
    except ImportError:
        Requirements("urllib2")
    try:
        import getpass
    except ImportError:
        Requirements("getpass")
    try:
        import socket
    except ImportError:
        Requirements("socket")
    try:
        import Queue
    except ImportError:
        Requirements("Queue")
    try:
        import time
    except ImportError:
        Requirements("time")
    try:
        import json
    except ImportError:
        Requirements("json")
    try:
        import hashlib
    except ImportError:
        Requirements("hashlib")
    try:
        import base64
    except ImportError:
        Requirements("base64")
    try:
        import hmac
    except ImportError:
        Requirements("hmac")
    try:
        import uuid
    except ImportError:
        Requirements("uuid")
    try:
        from prettytable import PrettyTable
    except ImportError:
        Requirements("prettytable")
    try:
        import sys
    except ImportError:
        Requirements("sys")
    try:
        import os
    except ImportError:
        Requirements("os")

Black_ROSE()