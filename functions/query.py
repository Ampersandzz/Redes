def change_query(packet):
    if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']['packet_length'] > 0:
        orig_size = len(packet['MYSQL']['query'])
        new_query = 'show databases'
        diff = len(new_query) - orig_size
        packet['MYSQL']['query'] = new_query
        packet['IP']['len'] += diff
        packet['MYSQL']['packet_length'] += diff
    return packet