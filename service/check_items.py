import sys
import os
import subprocess
import json
import psutil

def check_system(req):

    system_server = sys.platform
    service = os.popen("cat /etc/services").read()
    dns = os.popen("cat /etc/resolv.conf").read()
    qtd_users = os.popen("getent passwd | wc -l").read()
    ssh = os.popen("systemctl status ssh.service").read()

    json_server_items = {
        "system": system_server.replace('\n', ''),
        "path_archive_python": (os.getcwd()),
        "qtd_users": qtd_users.replace('\n', ''),
        "dns": dns.replace('\n', ''),
        "ssh_info" : ssh.replace('\n', ''),
        "cpu" : psutil.cpu_percent(1),
        "virtual_memory": psutil.virtual_memory(),
        "users": psutil.users()
    }

    app_json = json.dumps(json_server_items)

    return app_json, 200

    print("result.json created in /archives")