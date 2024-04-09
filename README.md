
# Mikrotik Autiomation with Ansible

I am going to make the  **Ansible Playbooks**  to automatically configure the Mikrotik provided from the market, in this method, I want to configure the Mikrotik automatically. I start these steps:

- **Upgrade ROS**: Upgrade the RouterOS to latest stable edition.
-  **Upgrade Routerboard Firmware **: Upgrade the Mikrotik Routerboard Firmare
- **Initialize the Mikrotik**, Reset to Factory, remove the default configurations, assign IP to ethernet interface for Internet and at the end set the SSH setting.
-  **Assign the configuration**: Assign our setting to the Mikrotik
-  **Integrate with Netbox IPAM** get the configuration from the Netbox-IPAM and assign to Mikrotik.

## Requirements
Edit the following files:
```
/group_vars/mikrotik-routers
/group_vars/mikrotik-test
```
and create file for each group.

Create file for each device:
```
/host_vars/NAM_Down
/host_vars/NAM_Up
/host_vars/NAM_Room
/host_vars/NAM_Main
/host_vars/NAM-Test
```

Edit hosts file and add the member to each group:
```
[mikrotik-test]
NAM-Test

[mikrotik-routers]
NAM-Main
NAM-UP
NAM-Down
NAM-Room

[mikrotik-firewalls-AMS]
alparslan
albasan
voipmax
artuk
```

## Running 
To initiate the Mikrotik:
```
python3 init_mikrotik.py
```

To upgrade the RouterOS:
```
ansible-playbook Mikrotik-Upgrade-ROS.yml
```

To upgrade the Mikrotik Routerboard Firmware:
```
ansible-playbook Mikrotik-Upgrade-Firmware.yml
```
To Apply the Configuration to Mikrotik:
```
ansible- playbook Mikrotik-Initial-Setup.yml
```
