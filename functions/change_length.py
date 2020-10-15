def change_length(packet):
    if packet['IP']['src'] == '172.17.0.3':
        print(packet['IP']['len'], packet['MYSQL']['packet_length'])
        packet['MYSQL']['packet_length'] = 57
        print(packet['IP']['len'], packet['MYSQL']['packet_length'])
    return packet