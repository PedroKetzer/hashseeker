import os
import sys
import base64
import hashlib
import subprocess


if len(sys.argv) <= 2:
        print ("Incorrect use")
        print ('How to use: '"filename + hashfile + wordlist")
        print ("Example: hashseeker.py hash.txt wordlist.txt")
        sys.exit()
else:

#checking for previous files
    print("Checking for previous files")
if os.path.exists("md5file"):
    print ("Previous md5file detected, removing it")
    os.remove("md5file")
else:
    print ("Previous md5file not detected")

if os.path.exists("base64file"):
    print ("Previous base64file detected, removing it")
    os.remove("base64file")
else:
    print ("Previous base64file not detected")

if os.path.exists("sha1file"):
    print ("Previous sha1file detected, removing it")
    os.remove("sha1file")
else:
    print ("Previous sha1file not detected")

#Start
hasharg = (sys.argv[1])
print ("Start the engines!")

#hash wordlist into md5 and outputing to a file
with open((sys.argv[2]), mode="r", encoding="utf-8") as fm:
    for line in fm:
        line = line.rstrip("\r\n")
        result = hashlib.md5(line.encode())
        file1 = open('md5file', 'a')
        sys.stdout = file1
        print(result.hexdigest())
file1.close()

#hash wordlist into base64 and outputing to a file
with open('md5file', mode="r") as b:
    for line in b:
        line = line.rstrip("\r\n")
        result = base64.b64encode(line.encode('UTF-8')).decode('ascii')
        file2 = open('base64file', 'a')
        sys.stdout = file2
        print (f"{result}")
file2.close()

#hash wordlist into sha1 and outputing to a file
with open('base64file', mode="r", encoding="utf-8") as fs:
    for line in fs:
        line = line.rstrip("\r\n")
        result = hashlib.sha1(line.encode())
        file3 = open('sha1file', 'a+')
        sys.stdout = file3
        print(result.hexdigest())
file3.close()

#bash variables
var1 = sys.argv[1]
var2 = sys.argv[2]
#using bash for now on
subprocess.call(['./linefinder.sh', var1, var2])