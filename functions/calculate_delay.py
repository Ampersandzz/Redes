def calculate_delay(packet):
    from datetime import datetime
    if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']:
        try:
            if packet.time:
                packet.time = datetime.now()
        except:
            pass
        packet.global_var('time', datetime.now())
    elif packet['IP']['src'] == '172.17.0.2':
        delay = (datetime.now() - packet.time).microseconds * 2 /1000
        print("{}ms".format(delay))
    return packet
