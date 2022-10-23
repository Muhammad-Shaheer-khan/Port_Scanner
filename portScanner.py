import socket
from threading import Thread
import time

# For check if no any port is open
lst = []

def connection_scan(target, port_num):
    
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((target, port_num))
        print("[+] {} tcp port is open.\n".format(port_num))
        lst.append(1)
        conn.close()
    except OSError:
        pass

def port_scan(target, port_num):
    try:
        targetIP = socket.gethostbyname(target)
        connection_scan(targetIP, port_num)
    except OSError:
        print("[x] Cannot resolve {}: Unknown host\n".format(target))

while True:
    try:
        print("\n"+"*"*27)
        IP = input("Enetr IP address or host name:\t")
        portStart = int(input("Enter starting port for scanning:\t"))
        portEnd = int(input("Enter end port for scanning:\t"))
        print("*"*27, "\n")
        print("Ports is scanning...\n")
        start = time.time()
        for Port in range(portStart, portEnd+1):
            t = Thread(target=port_scan, args=(IP, Port))
            t.start()
            
        break
    except:
        print("please give valid info. Try again\n")

if len(lst) == 0 :
    print("No port is open of {} IP/host.".format(IP))
end = time.time()
print("Time Consume during port scanning is: {:.2f} sec.".format(end-start))