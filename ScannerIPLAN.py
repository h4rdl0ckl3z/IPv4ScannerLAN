import socket
from datetime import datetime
IPGw = input("Enter the IP Default Gateway : ")
IPGw1 = IPGw.split('.')
Dot = '.'
IPGw2 = IPGw1[0] + Dot + IPGw1[1] + Dot + IPGw1[2] + Dot
Start = int(input("Enter the Starting Number : "))
End = int(input("Enter the Last Number : "))
Time1 = datetime.now()
def Scanner(addr):
    Computer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = Computer.connect_ex((addr, 135))
    if result == 0:
        return(1)
    else:
        return(0)
def Start1():
    for ip in range(Start, End+1):
        addr = IPGw2 + str(ip)
        if (Scanner(addr)):
            print("IPv4 Address :", addr, "Online")
        else:
            print("IPv4 Address :", addr, "Offline")
Start1()
Time2 = datetime.now()
Total = Time2 - Time1
print("Scanning completed in :", Total)