#!/usr/bin/python3
# -*- coding: utf-8 -*-
"Scan the subnet for active iMACRT modules."


import socket
import select


def scan(brd_addr='<broadcast>', timeout=2):
    """Scan for responding iMACRT modules.
    Will use the broadcast address 'brd_addr' for scanning.

    Send the datagram "0 1" to 8001 port."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except AttributeError:
        # Some systems don't support SO_REUSEPORT
        pass
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setblocking(False)

    sock.bind(('0.0.0.0', 8001))
    sock.sendto(b"0 1", (brd_addr, 8001))
    response = []
    while True:
        readables, writable, excp = select.select([sock, ], [], [], timeout)
        if not readables:
            # Timeout
            break
        for readable in readables:
            data, sender_addr = readable.recvfrom(1024)
            if data != b'0 1':
                response.append((data, sender_addr))
    return response


def sort(scan_result):
    "Returns list of ('iMACRT_name', 'ip_address')."
    return [(data.decode('ascii').split('\x00')[0].split(' ')[-1], addr[0])
            for data, addr in scan_result]
