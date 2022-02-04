class IPVerify:
    def __init__(self):
        super(IPVerify, self).__init__()
        # self.octetLst = []
        # self.subnetMaskLst = []

    # def __initializeIP(self, ip: str):
    #     self.octetLst.clear()
    #     [self.octetLst.append(i) for i in ip.split(".")]
    #     return self.octetLst

    def __initializeIP(self, ip: str):
        lst = []
        [lst.append(i) for i in ip.split(".")]
        if len(lst[0]) == 8:
            lst = self.__binInput(lst)
        return lst

    @staticmethod
    def __binInput(lst):
        lst2 = []
        [lst2.append(str(int(i, 2))) for i in lst]
        return lst2

    # @staticmethod
    def __initializeMask(self, mask: str):
        m = mask.split(".")
        l = len(m)
        if l == 4:
            # t = deque()
            t = []
            try:
                for i in m:
                    num = int(i)
                    if 256 > num >= 0:
                        t.append(str(num))
                    else:
                        return None
                return t
            except:
                return None
        elif l == 1:
            mask = self.CIDRtoDefaultNotation(m[0])
            m = mask.split(".")
            return m
            # print()
        else:
            return None

    @staticmethod
    def CIDRtoDefaultNotation(mask: str):
        """Convert subnet mask notation from CIDR to default """
        mask = int(mask[1:])
        q = int(mask / 8)  # no. of complete octet in mask
        r = int(mask % 8)  # bit size of incomplete octet in mask
        c = 1  # no. of incomplete octet in mask
        l1 = [8] * q
        l1.append(r)
        if r == 0:
            c = 0  # if size is zero, then change no. of incomplete octet to 0
            l1.pop()  # remove

        l2 = [0] * (4 - q - c)
        # noofSetBitForEachOctetinMask = deque()
        noofSetBitForEachOctetinMask = []
        [noofSetBitForEachOctetinMask.append(i) for i in l1]
        [noofSetBitForEachOctetinMask.append(i) for i in l2]
        # print(noofSetBitForEachOctetinMask)
        newMask = []
        for i in noofSetBitForEachOctetinMask:
            octet = "0b"
            for _ in range(i):
                octet += "1"
            for _ in range(8 - i):
                octet += "0"
            newMask.append(str(int(octet, 2)))
        return ".".join(newMask)
        # print(".".join(newMask))

    @staticmethod
    def __firstCheck(octetlst: list):
        try:
            for octet in octetlst:
                o = int(octet)
                if o > 255 or o < 0:
                    return False
            return True
        except:
            return False

    @staticmethod
    def __secondCheck(lst: list):
        for octet in lst:
            i = octet[0]
            if i == "0" and len(octet) > 1:
                return False
        return True

    def verify(self, lst: list):
        """Verify ipv4 address"""
        if len(lst) == 4:
            first = self.__firstCheck(lst)
            if first:
                if self.__secondCheck(lst):
                    return True
                    # print("Valid IP Address")
                else:
                    return False
                    # print("Invalid IP Address")
            else:
                return False
        else:
            return False
            # print("Invalid IP Address")

    # def printVerify(self):
    #     if self.verify(self.octetLst):
    #         print("Valid IP Address")
    #     else:
    #         print("Invalid IP Address")
    def verifyAndPrint(self, ipv4_add: str):
        """Verify ipv4 address and print valid/Invalid """
        ls = self.__initializeIP(ipv4_add)
        if self.verify(ls):
            print("Valid IP Address")
        else:
            print("Invalid IP Address")

    def findClassName(self, ipv4_add: str):
        """Return class name if valid ipv4 address otherwise return None"""
        ls = self.__initializeIP(ipv4_add)
        if self.verify(ls):
            i = int(ls[0])
            if 127 >= i >= 0:
                return "A"
            elif 191 >= i >= 128:
                return "B"
            elif 223 >= i >= 192:
                return "C"
            elif 239 >= i >= 224:
                return "D"
            elif 255 >= i >= 240:
                return "E"
        else:
            return None

    def printClassName(self, ipv4_add: str):
        """Print class name if valid ipv4 address otherwise print invalid """
        j = self.findClassName(ipv4_add)
        if j is not None:
            print("Class Name is {}".format(j))
            print("Default Mask= {}".format(self.defaultMask(j)))
        else:
            print("Invalid IP Address")

    def networkPartOfIP(self, ipv4_add: str, subnetmask: str):
        """Return network part of ipv4 address"""
        # maskOct = subnetmask.split(".")
        # ipOctet = ipv4_add.split(".")
        maskOct = self.__initializeMask(subnetmask)
        ipOctet = self.__initializeIP(ipv4_add)
        netPart = []
        if not (maskOct is None):
            if self.verify(ipOctet):
                for i in range(4):
                    t1 = int(ipOctet[i])
                    t2 = int(maskOct[i])
                    t = t1 & t2
                    # t = int(hex(int(self.octetLst[i])) and hex(int(maskOct[i])), 0)
                    # if not t == 0:
                    netPart.append(str(t))
                return ".".join(netPart)
            else:
                raise Exception("Invalid ipv4 address")
        else:
            raise Exception("Invalid Subnet Mask")

    def hostPartofIP(self, ipv4_add: str, subnetmask: str):
        """Return host part of ipv4 address"""
        # maskOct = subnetmask.split(".")
        # ipOctet = ipv4_add.split(".")
        maskOct = self.__initializeMask(subnetmask)
        ipOctet = self.__initializeIP(ipv4_add)
        hostPart = []
        if not (maskOct is None):
            if self.verify(ipOctet):
                for i in range(4):
                    t1 = int(ipOctet[i])
                    t2 = (~ int(maskOct[i]))
                    t = t1 & t2
                    hostPart.append(str(t))
                return ".".join(hostPart)
            else:
                raise Exception("Invalid ipv4 address")
        else:
            raise Exception("Invalid Subnet Mask")

    def printHostAndNetworkPart(self, ipv4_add: str, mask: str):
        """Print Host and Network part of ipv4 address"""
        netPart = self.networkPartOfIP(ipv4_add, mask)
        hostPart = self.hostPartofIP(ipv4_add, mask)
        print("Network Part of IPv4 Address= {}".format(netPart))
        print("Host Part of IPv4 Address= {}".format(hostPart))

    @staticmethod
    def defaultMask(cl: str):
        if cl == "A":
            return "255.0.0.0"
        elif cl == "B":
            return "255.255.0.0"
        elif cl == "c":
            return "255.255.0.0"
        else:
            return "None"


