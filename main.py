import sipfullproxy
import socket
import socketserver
import time
HOST, PORT = '0.0.0.0', 5060


def ipaddr():
    ipaddress = socket.gethostbyname_ex(socket.gethostname())[2][1]
    return ipaddress


def check_ip(ipaddress):
    print("SIP proxy IP :", ipaddress)
    temp = input("Je to spravna IP ?[Y/N] ")
    if temp == 'Y':
        return ipaddress
    if temp == 'N':
        new_ip = input("Zadajte ip : ")
        return new_ip

def logs():
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log',
                                     level=sipfullproxy.logging.INFO, datefmt='%H:%M:%S')
    sipfullproxy.logging.info(time.strftime("PROXY STARTED AT %a, %d %b %Y %H:%M:%S ", time.localtime()))


def init(ipaddress):
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)


def proxy_start():
    print("Proxy started")
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == '__main__':
    ipaddress = ipaddr()
    ipaddress = check_ip(ipaddress)
    logs()
    init(ipaddress)
    proxy_start()


