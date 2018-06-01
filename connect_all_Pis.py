# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko

import threading


def ssh2(ip, username, passwd, cmd):
    try:
        print("start to connect")

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(ip, 22, username, passwd, timeout=5)

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

            out = stdout.readlines()

            for o in out:
                print (o),

        print ("%s\tOK\n" % (ip))

        ssh.close()

    except:

        print ("%s\tError\n" % (ip))


if __name__ == "__main__":

    print("Start.......")
    #cmd = ["echo hello", "python /home/pi/receive_data.py 2 640 480"]
    #cmd = ["echo hello", "tar -zcvf /home/pi/imgs.tar.gz ./img"]
    cmd = ["echo hello", "scp /home/pi/imgs.tar.gz enigma@138.38.72.201:/home/enigma/data/"]
    #cmd = ["echo hello", "scp" /home ]
    #cmd = ["echo hello", "rm -rf /home/pi/img;mkdir /home/pi/img"]
    username = "pi"

    passwd = "raspberry"

    threads = []

    ip1, ip2, ip3 = raw_input().split(",")

    print ("Begin......")

    for ip in [ip1, ip2, ip3]:

        a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        a.start()
