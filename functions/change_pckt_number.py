def change_pckt_number(packet):
    if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']['packet_length'] > 0:
        print(packet['MYSQL']['packet_number'])
        packet['MYSQL']['packet_number'] = 16
        print(packet['MYSQL']['packet_number'])
    return packet