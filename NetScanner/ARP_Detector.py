import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface = interface , store = False , prn = packet_sniifer)

def packet_sniifer(packet):
    if packet.haslayer(scapy.ARP)and packet[scapy.ARP].op == 2 :
        print(packet.show())


sniff()