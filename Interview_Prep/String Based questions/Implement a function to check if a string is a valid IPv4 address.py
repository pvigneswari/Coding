def validIpv4(ip):
    parts = ip.split('.')
    if(len(parts) != 4):
        return False
    
    for part in parts:
        if(int(part)):
            if (0 > int(part) > 255):
                return False
            if(part[0]==0 and len(part)>1):
                return False
        else:
            return False
    return True
print(validIpv4('192.01.9.110'))