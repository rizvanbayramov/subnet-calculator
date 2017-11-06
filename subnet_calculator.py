def SUBNET(mask, IP): #for calculation network ID
    block_size = 256 - mask
    for i in range (128):
        if block_size * i <= IP < block_size * (i+1):
            subnet = block_size * i
            return subnet

def BROADCAST(mask, IP): #for calculation broadcast ID
    block_size = 256 - mask
    for i in range (128):
        if block_size * i <= IP < block_size * (i+1):
            subnet = (block_size * (i+1)) - 1
            return subnet


print 'Please enter your IP address information in the ',
print 'following format: x.x.x.x/xx'			

IP = raw_input ('Your IP address: ')
IP = IP.split('.')
IP = IP[:-1] + IP[-1].split('/')

a,b,c,d,e = int(IP[0]), int(IP[1]), int(IP[2]), int(IP[3]), int(IP[4])

subnet_mask = '1' * e + '0' * (32-e)
mask1 = int(subnet_mask[:8],2)
mask2 = int(subnet_mask[8:16],2)
mask3 = int(subnet_mask[16:24],2)
mask4 = int(subnet_mask[24::],2)

if mask1 != 255:
    IP1, IP2, IP3, IP4 = SUBNET(mask1, a), 0, 0, 0
    BR1, BR2, BR3, BR4 = BROADCAST(mask1, a), 255, 255, 255
elif mask2 != 255:
    IP1, IP2, IP3, IP4 = a, SUBNET(mask2, b), 0, 0
    BR1, BR2, BR3, BR4 = a, BROADCAST(mask2, b), 255, 255
elif mask3 != 255:
    IP1, IP2, IP3, IP4 = a, b, SUBNET(mask3, c), 0
    BR1, BR2, BR3, BR4 = a, b, BROADCAST(mask3, c), 255
elif mask4 != 255:
    IP1, IP2, IP3, IP4 = a, b, c, SUBNET(mask4, d)
    BR1, BR2, BR3, BR4 = a, b, c, BROADCAST(mask4, d)
	

print '\n\n'
print 'Your Network ID is:',
print '{}.{}.{}.{}'.format(IP1,IP2,IP3,IP4)
print 'Your Broadcast ID is:',
print '{}.{}.{}.{}'.format(BR1,BR2,BR3,BR4)

print 'You Subnet Mask is: ' ,
print '{}.{}.{}.{}'.format(mask1 , mask2 , mask3 , mask4)
print '\n\n'