import sys
import os
import subprocess

system_server = sys.platform
service = os.popen("cat /etc/services").read()
dns = os.popen("cat /etc/resolv.conf").read()
system_info = os.popen("lsb_release -a").read()
qtd_users = os.popen("getent passwd | wc -l").read()
ssh = os.popen("systemctl status ssh.service").read()

json_server_items = {
    "system": system_server,
    "path_archive_python": (os.getcwd()),
    "qtd_users": qtd_users,
    "dns": dns,
    "system_info" : system_info,
    "ssh_info" : ssh
}

print(json_server_items)