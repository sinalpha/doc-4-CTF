from scapy.all import *

#open a pcap file
pcap = rdpcap("")

#show UDP info in the file 
print(pcap[UDP])
 
#show all UDP info in the file
for p in pcap[UDP]:
  p.show()

#show all IP inside the UDP info 
for p in pcap[UDP]:
  try:
    p[IP].show()
  except InderError:
    continue
