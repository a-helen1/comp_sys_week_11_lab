#! /bin/bash

# presence-detect.sh
# searches for the MAC address of known devices

# do arp_scan to get connected mac addresses
connectedDevices=$(sudo arp-scan -l)

knownDevices=("d4:28:d5:37:7e:a2" "2c:0e:3d:92:79:ef")

for device in "${knownDevices[@]}"
do
    if [[ "$connectedDevices" = *"$device"* ]]; then
        echo "$device is present!"
    else
        echo "$device is NOT present!"
    fi
done
