import nmap
import time

# Just for check open ports
lst = []

class portScanning:
    def __init__(self, IP , port) -> None:
        self.conn = nmap.PortScanner()
        self.result = self.conn.scan(IP, str(port))
        state = self.result['scan'][IP]['tcp'][int(port)]["state"]
        if state == 'open':
            print ("Port {} is open:".format(port,)+ "\n")
            lst.append(1)
class bannerGrab(portScanning):
    def __init__(self, IP, port) -> None:
        super().__init__(IP, port)
        for i, j in self.result['scan'].items():
            print("Scanned IP:",i ,"\n" )
            for k, l in j.items():
                print('  [*]',k)
                print('\t[^]',(l))

def callBanner(IP, port):
    bannerGrab(IP, port)

while True:
    try:
        print("\n"+"*"*37)
        choice = int(input("1. Port Scanning.\n2. Banner Grabbing.\n\nEnter(1/2):\t"))
        if choice == 1:
            IP = input("Enter IP :\t")
            portStart = int(input("Enter starting port for scanning:\t"))
            portEnd = int(input("Enter end port for scanning:\t"))
            print("*"*37, "\n")
            print("Ports is scanning...\n")
            start = time.time()
            for scanPort in range(portStart, portEnd+1):
                portScanning(IP, scanPort)
            end = time.time()
            if len(lst) == 0 :
                print("No port is open of {} IP.".format(IP))
            print("Time Consume during port scanning is: {:.2f} sec".format(end-start))
            bannerPermit = input("\nDo you want to look details of any particular port:(Y/n)\t")
            if bannerPermit.lower() == 'y':
                portNum = int(input('\nEnter port number:\t'))
                print ('\nBanner Grabbing...\n')
                callBanner(IP, portNum)
        
            break
        
        elif choice == 2:
            IP = input("\nEnter IP address:\t")
            portNum = int(input('\nEnter port number:\t'))
            print ('\nBanner Grabbing...\n')
            callBanner(IP, portNum)
            break
        else:
            print("Am I looking fool !. \n\tTry again")
        
    except:
        print("please give valid info. Try again\nHint: Check your IP is valid or inside your network/ Check given input.\n")



