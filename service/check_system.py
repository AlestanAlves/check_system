import sys
import os
import subprocess
import json
import psutil
import struct
from uuid import getnode as get_mac

def check_system(req):

    system_server = sys.platform
    service = os.popen("cat /etc/services").read()
    dns = os.popen("cat /etc/resolv.conf").read()
    qtd_users = os.popen("getent passwd | wc -l").read()
    ssh = os.popen("systemctl status ssh.service").read()

    mac = str(hex(get_mac()))
    mac = mac[2:]
    while len(mac) < 12:
        mac = '0' + mac
    macb = b''
    for i in range(0, 12, 2):
        m = int(mac[i:i + 2], 16)
        macb += struct.pack('!B', m)

    json_server_items = {
        "system": system_server.replace('\n', ''),
        "path_archive_python": (os.getcwd()),
        "qtd_users": qtd_users.replace('\n', ''),
        "dns": dns.replace('\n', ''),
        "ssh_info" : ssh.replace('\n', ''),
        "cpu" : psutil.cpu_percent(1),
        "virtual_memory": psutil.virtual_memory(),
        "users": psutil.users(),
        "mac": str(macb, 'utf-8', 'ignore')
    }

    app_json = json.dumps(json_server_items)

    return app_json, 200

    print("json created")