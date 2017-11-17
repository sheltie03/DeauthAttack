# -*- coding utf-8 -*-
import pyshark
import sys
import time
import threading
from pprint import pprint


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


def wlan_sniffer(cap):
    aps = []
    for num, packets in enumerate(cap):
        data = ap_info_extractor(packets)
        data['num'] = num
        aps.append((data['bssid']))
        aps = list(set(aps))
        addr = ''
        for i in range(len(aps)):
            addr += aps[i] + ' '
        sys.stdout.write("\r\033[0K\033[G%s" % addr)
        sys.stdout.flush()
        time.sleep(1)
    return


if __name__ == '__main__':
    recv_iface = 'wlan0'
    cap = pyshark.LiveCapture(display_filter="wlan.fc.type_subtype == 0x0008",
                              interface=recv_iface)
    wlan_sniffer(cap)
