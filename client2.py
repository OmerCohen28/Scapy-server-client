from scapy.all import *
from scapy.layers.inet import *


start = IP(dst="10.100.102.3")/TCP(sport=50100,dport=50003,flags="")/"hello"
print(start[IP].show())
print(start[TCP].payload.load.decode())
send(start,iface=get_working_if())