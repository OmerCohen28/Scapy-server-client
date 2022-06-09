from scapy.all import *
from scapy.layers.inet import *

p = IP(dst="10.100.102.3")/TCP(sport=50100,dport=50003,flags="")/"payload"

print(type(p[IP].src))