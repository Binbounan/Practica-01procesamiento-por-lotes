with open(r'C:\Users\paopu\Downloads\prueba2.txt', 'r') as input_file, open(r'C:\Users\paopu\Downloads\salida.txt', 'w') as output_file:

    for line in input_file:

        content = line.split(',')

        content[0] = content[0].split('/')[0]

        ipv6_segments = [str(int(segment, 16)) for segment in content[0].split(':')]

        ipv6 = ':'.join(ipv6_segments)

        last_name = content[2] 

        ipv4_segments = [hex(int(segment))[2:].upper() for segment in content[-1].split('.')]

        ipv4 = '.'.join(ipv4_segments)

        text = ':'.join([last_name, ipv6, ipv4])

        output_file.write(text + '\n')
