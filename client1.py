from scapy.all import *
from scapy.layers.inet import *

def send_to_buddy():
    pass



print("start")
capture = sniff(count=1,filter="tcp dst port 50003")
capture.show()
print(capture.sport)
print("end")


