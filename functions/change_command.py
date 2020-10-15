def change_command(packet):
    if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']['packet_length'] > 0:
        print(packet['MYSQL']['command'])
        packet['MYSQL']['command'] = 1
        # 5: unknown command ,  1: lost connection
        print(packet['MYSQL']['command'])
    return packet