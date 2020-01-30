#!/usr/bin/env python2.7


import dpkt, socket



print("Enter valid file name")
inp=raw_input()
f = open(inp)
pcap = dpkt.pcap.Reader(f)


syn = {}
syn_ack={}
curPacket = 0


for ts, buf in pcap:
    curPacket += 1


    try:
        eth = dpkt.ethernet.Ethernet(buf)
    except (dpkt.dpkt.UnpackError, IndexError):
        continue

    ip = eth.data
    if not ip:
        continue

    tcp = ip.data
    if type(tcp) != dpkt.tcp.TCP:
        continue


    sender = socket.inet_ntoa(ip.src)
    receiver = socket.inet_ntoa(ip.dst)


    if(tcp.flags& dpkt.tcp.TH_SYN!=0 and tcp.flags& dpkt.tcp.TH_ACK!=0):

        if (receiver not in syn_ack):
            syn_ack[receiver] = 0
        syn_ack[receiver] += 1
    elif(tcp.flags& dpkt.tcp.TH_SYN!=0):

        if (sender not in syn):
            syn[sender] = 0
        syn[sender] += 1

    # print(curPacket,sender,receiver)



for s,v in syn.iteritems():
    if s in syn_ack and syn[s] >= (syn_ack[s] * 3):
        print("Found")
        print(s)
    if(s not in syn_ack):
        print("Found only syn")
        print(s)
 

