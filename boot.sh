#! /bin/bash


 /usr/bin/python -u /home/pi/receive_data.py 8 1296 972 > camera.txt
 /usr/bin/python -u /home/pi/Downloads/pi_send_ip.py > monitor.txt

