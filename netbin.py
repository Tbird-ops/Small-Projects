# Tristan's networking toolkit

# Used to break apart IP octets
def ip_breaker(addr=0):
    if addr == 0:
        addr = input("Enter IP address: ")
    return addr.split(".")  ## break up octets

# Build IP address from octets
def ip_builder(octets):
    return '.'.join(octets)  ## send back full address

# Translate IP octets into full address
def to_bin(addr=0):
    octets = ip_breaker(addr)
    binary_octets = []
    for octet in octets:  ## compare octet bitwise
        temp = ''
        for i in range(8):
            mask = 128 >> i
            if(int(octet) & mask): ## Check current mask against octet
                temp += '1'
            else:
                temp += '0'
        binary_octets.append(temp)
    return ip_builder(binary_octets)

# Translate binary IP addr to decimal IP octets
def from_bin(addr=0):
    binary_octets = ip_breaker(addr)
    octets = [str(int(oct,2)) for oct in binary_octets]  ## translate each octet into a decimal string
    return ip_builder(octets)

# Show CIDR bitwise 
def cidr(slant=0):
    if slant == 0:
        slant = int(input("Enter slant: /"))
    bin = ["1" if i < slant else "0" for i in range(32)]    ## build out all bits
    bin = [''.join(bin[i * 8:(i+1) * 8]) for i in range(4)] ## break bits up into 8 bit strings
    return ip_builder(bin)

# Show total and range of usable IPs
def usable_ip():
    addr, slant = input("Enter address with slant: ").split("/")  ## ex 192.168.1.0/24
    slant = int(slant)

    ## Math behind total usable addr
    host_bits = 32 - int(slant) 
    usable = 2**host_bits - 2

    ## Determine max IP addr
    temp = list(to_bin(addr))
    for i in range(slant+(slant//8), 35):
        print("i {}  temp[i] {}".format(i, temp[i]))
        if temp[i] != '.':
            temp[i] = "1"
    high = from_bin("".join(temp))

    return "Usable: {}, Range: {} - {}".format(usable, addr, high)

# Show Subnet for given CIDR range
def subnet():
    mask = cidr()
    return from_bin(mask)


def main():
    while True:
        ret = None
        print("1.) To Binary        4.) Usable IPs\n2.) From Binary      5.) Subnet Mask\n3.) CIDR             6.) Quit\n")
        choice = int(input("Enter number for selection: "))

        match choice:
            case 1:
                ret = to_bin()
            case 2:                
                ret = from_bin()    
            case 3:                
                ret = cidr()   
            case 4:                
                ret = usable_ip()
            case 5:                
                ret = subnet()
            case 6:
                break
            case _:
                print("Option invalid. Please select number\n")
        
        print("\n",ret, end="\n\n")

if __name__ == "__main__":
    main()