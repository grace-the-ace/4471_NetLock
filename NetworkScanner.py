import os
#Be connected to your home network
#Run command line arp -a
os.system("arp -a > MACaddress.txt")
#Parse all the MAC addresses into a list
file=open("MACaddress.txt","r")
#read entire file of arp -a results into a string
com_line_results=file.read(-1)
#list of all the MAC addresses of all the devices on the network
list_mac_addresses=[]
#boolean if current char is part of a MAC address
part_of_MAC=False
#I have it down as a list and it includes the periods, but its
#p easy to change it to just being an interger without the periods
next_MAC=""
counter = 0	
start = False
#iterates over entire arp -a results
for c in com_line_results:
    if(c=='['):
        part_of_MAC=False
        #remove the space after the MAC address 
        next_MAC = next_MAC[:-1]
        list_mac_addresses.append(next_MAC)
        next_MAC=""
    if(part_of_MAC):
        next_MAC=next_MAC+c
    if(c==')'):
	start = True
        counter=1
    if(counter==5 and start==True):
	start=False
        part_of_MAC=True
        counter=0;
    counter += 1
#prints list of mac addresses
print(list_mac_addresses)
file.close()
