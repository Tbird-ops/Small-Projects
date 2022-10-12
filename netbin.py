# Tristan's networking toolkit

# Used to break apart IP octets
def ip_breaker(addr=0):
    if addr == 0:
        addr = input("Enter IP address: ")
    octets = addr.split(".")
    return octets

# Build IP address from octets
def ip_builder(octets):
    ipaddr = ''
    for i in octets:
        ipaddr += i
        ipaddr += "."
    ipaddr = ipaddr[:-1]
    return ipaddr

# Translate IP octets into full address
def to_bin(addr=0):
    octs = ip_breaker(addr)
    bin_octs = []
    for element in octs:  ## compare octet bitwise
        mask = 128
        temp = ''
        for i in range(8):
            if(int(element) & mask): ## Check current mask against octet
                temp += '1'
            else:
                temp += '0'
            mask = mask >> 1
        bin_octs.append(temp)
    output = ip_builder(bin_octs)
    return output

# Translate binary IP addr to decimal IP octets
def from_bin(addr=0):
    bin_octs = ip_breaker(addr)
    octs = []
    for element in bin_octs:
        val = str(int(element, 2))
        octs.append(val)
    output = ip_builder(octs)
    return output

# Show CIDR bitwise 
def cidr(slant=0):
    if slant == 0:
        slant = int(input("Enter slant: /"))
    bin = []
    temp = ''
    for i in range(slant):  ## Build 1's up to slant
        temp += "1"
        if i % 8 == 7:
            bin.append(temp)
            temp = ''
    for x in range(slant, 32): ## Fill rest of address bits with 0's
        temp += "0"
        if x % 8 == 7:
            bin.append(temp)
            temp = ''
    addr = ip_builder(bin)
    return addr

# Show total and range of usable IPs
def usable_ip():
    rang = input("Enter address with slant: ").split("/")  ## ex 192.168.1.0/24
    
    ## Math behind total usable addr
    hostbits = 32 - int(rang[1]) 
    usable = 2**hostbits - 2

    ## Determine max IP addr
    temp = list(to_bin(rang[0]))
    for i in range(int(rang[1])+1, 35):
        if temp[i] != '.':
            temp[i] = "1"
    high = from_bin("".join(temp))

    return "Usable: {}, Range: {} - {}".format(usable, rang[0], high)

# Show Subnet for given CIDR range
def subnet():
    mask = cidr()
    addr = from_bin(mask)
    return addr


def main():
    while True:
        ret = None
        print("1.) To Binary        4.) Usable IPs\n2.) From Binary      5.) Subnet Mask\n3.) CIDR             6.) Quit\n")
        choice = int(input("Enter option: "))

        if choice == 1:
            ret = to_bin()
        elif choice == 2:
            ret = from_bin()    
        elif choice == 3:
            ret = cidr()    
        elif choice == 4:
            ret = usable_ip()
        elif choice == 5:
            ret = subnet()
        elif choice == 6:
            break
        else:
            print("Error")
        
        print("\n",ret, end="\n\n")

if __name__ == "__main__":
    main()