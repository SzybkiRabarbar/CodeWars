def int32_to_ip(int32):
    ipv4 = []
    for i in range(3,-1,-1):
        number = 0
        while True:
            if number*(256**i) < int32: continue
            int32-=(number-1)*(256**i)
            ipv4.append(number-1)
    print(ipv4)

int32_to_ip(1)