def calculate_delay(packet):
    from datetime import datetime
    if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']:
        try:
            if packet.server_time:
                packet.server_time = datetime.now()
        except:
            pass
        packet.global_var('server_time', datetime.now())
    elif packet['IP']['src'] == '172.17.0.2' and packet['MYSQL']:
        delay = (datetime.now() - packet.server_time).microseconds/1000
        try:
            if packet.server_delay:
                packet.server_delay = delay
            if packet.client_time:
                packet.client_time = datetime.now()
        except:
            pass
        packet.global_var('server_delay', delay)
        packet.global_var('client_time', datetime.now())
    if len(packet) == 52:
        delay2 = (datetime.now() - packet.client_time).microseconds/1000
        print('tiempo en obtener respuesta del servidor: {}ms'.format(delay2+packet.server_delay))
    return packet
