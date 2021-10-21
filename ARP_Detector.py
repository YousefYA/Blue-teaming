from termcolor import colored
import os
import winsound
import pyfiglet
def get_mac(ip):
    arp = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    packet = broadcast/arp
    answered = scapy.srp(packet , timeout = 1 , verbose = False)[0]
    return answered[0][1].hwsrc


def sniff():
    scapy.sniff( store = False , prn = packet_sniifer)
    # we used scapy sniff function inorder to sniff on traffic and prn to recall our function

def packet_sniifer(packet):
    if packet.haslayer(scapy.ARP)and packet[scapy.ARP].op == 2 :
    # here we used .haslayer to check for ARP packets and ARP layer then print them in deatials using .show() function
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if real_mac != response_mac :
                winsound.Beep(500, 1000)
                print(colored("[+] You are Under Attack", "red" , attrs=["bold"]))
        except IndexError:
            pass

        #print(packet.show())
os.system("cls")
text = pyfiglet.figlet_format("MITM-Detect")
text_color = colored(text , "cyan" , attrs=["bold"])
print(text_color)
sniff()
