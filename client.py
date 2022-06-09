#this client's port is 50004, connecting to 50003

from scapy.all import *
from scapy.layers.inet import *

MY_PORT = 50004
DST_PORT = 50003


while True:
    payload = input("Enter message for server: ")
    p = IP(dst="10.100.102.3")/TCP(sport=MY_PORT,dport=DST_PORT,flags="")/payload
    if payload == "move":
        MY_PORT+=2
        DST_PORT +=2
    send(p,iface=get_working_if())

    capture = sniff(count=1,filter=f"tcp dst port {MY_PORT}")[0]
    print("server said: "+capture[TCP].payload.load.decode())