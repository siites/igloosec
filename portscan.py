from functools import partial
from multiprocessing import Pool
import socket

multicount = 10
fastPort = [21,22,23,80,8080,443,3389,1443,3306]
allPort = range(1, 65536)

def ping(host, port):
    try:
        socket.socket().connect((host, port))
        print(str(port) + " Open")
        return port
    except:
        pass

def scan_ports(host, scanMode):
    if scanMode == "fast":
        portype=fastPort
    elif scanMode == "all":
        portype=fastPort
    else:
        exit()

    p = Pool(multicount)
    ping_host = partial(ping, host)
    return filter(bool, p.map(ping_host, fastPort))

def main():
    hostAddress = raw_input("Scan Target IP: ")
    scanMode = raw_input("Scan Mode Select (all or fast): ")
    hostIP  = socket.gethostbyname(hostAddress)

    if hostIP is None:
        exit()

    print("\nScanning start " + hostIP + " ...")
    ports = list(scan_ports(hostIP, scanMode))
    print("\nDone.")

    print(str(len(ports)) + " ports openned")
    print(ports)

if __name__ == "__main__":
    main()
