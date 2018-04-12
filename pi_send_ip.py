# /bin/env python
# -*-coding:utf-8-*-
import socket
import time
import smtplib
import urllib

def sendEmail(username, password, receiver, subject, msghtml):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    now = time.ctime(int(time.time()))
    headers = subject+' \r\n'
    headers += '\r\n'
    msg = headers+now+'\r\n'+msghtml

    server.sendmail('enigmashroom@gmail.com', receiver, msg)
    server.quit()

def check_network():
    while True:
        try:
            result = urllib.urlopen('http://baidu.com/').read()
            #print(result)
            print('Network is Ready!')
            break
        except Exception, e:
            print e
            print 'Network is not ready,Sleep 5s....'
            time.sleep(5)
    return True


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.1.1.1', 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr


if __name__ == '__main__':
    check_network()
    ipaddr = get_ip_address()
    email_add = 'enigmashroom@gmail.com'
    receiver = 'sx329@bath.ac.uk'
    password = 'Enigma!!@#%*13'
    sendEmail(email_add, password, [receiver], 'IP Address Of Raspberry Pi with UV camera', ipaddr)