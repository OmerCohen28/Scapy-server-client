#this client's port is 50003, connecting to 50004
MY_PORT = 50003
DST_PORT = 50004
from scapy.all import *
from scapy.layers.inet import IP,TCP
while True:
    capture = sniff(count=1,filter=f"tcp dst port {MY_PORT}")[0]
    print(capture.summary())
    print(capture[TCP].payload.load.decode())

    if capture[TCP].payload.load.decode() == "move":
        MY_PORT+=2
        DST_PORT+=2
    
    give_back = IP(dst="10.100.102.3")/TCP(dport = DST_PORT,flags="",sport=MY_PORT)/capture[TCP].payload.load.decode()
    send(give_back,iface=get_working_if())

