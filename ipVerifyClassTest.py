from IPVerifyClass import IPVerify

ipClass = IPVerify()
opStr = """
Enter
    1. To Verify IP Address
    2. To Get IP Class Name
    3. To enter new IP Address
    4. To Get Host and Network Part
    0. Exit
        """
while True:
    flag = False
    ip = input("Enter IP Address= ")
    # ipClass.initializeIP(ip)
    while True:
        opt = int(input(opStr))
        if opt == 1:
            # ipClass.printVerify()
            ipClass.verifyAndPrint(ip)
        elif opt == 2:
            ipClass.printClassName(ip)
        elif opt == 3:
            # flag = False
            break
        elif opt == 4:
            mask = input("Enter Subnet Mask= ")
            ipClass.printHostAndNetworkPart(ip, mask)
        elif opt == 0:
            flag = True
            break
        else:
            print("Enter valid option")
    if flag:
        break

# ipClass.initializeIP("172.16.35.123")
# net = ipClass.networkPartOfIP("255.255.250.0")
# hst = ipClass.hostPartofIP("255.255.250.0")
# ipClass.printHostAndNetworkPart("172.16.35.123", "/12")
# print(net, hst)
