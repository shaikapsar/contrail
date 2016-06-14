from fabric.api import env

# FOR LAB ONLY, DEFAULT IS 250
minimum_diskGB = 10

# MANAGEMENT USERNAME/IP ADDRESSES
host1 = 'root@10.10.10.241'

# EXTERNAL ROUTER DEFINITIONS
ext_routers = []

# AUTONOMOUS SYSTEM NUMBER
router_asn = 64512

# HOST FROM WHICH THE FAB COMMANDS ARE TRIGGERED
# TO INSTALL AND PROVISION
host_build = 'root@10.10.10.241'

# ROLE DEFINITIONS
env.roledefs = {
    'all': [host1],
    'database': [host1],
    'cfgm': [host1],
    'control': [host1],
    'compute': [host1],
    'collector': [host1],
    'webui': [host1],
    'openstack': [host1],
    'build': [host_build],
}

# NODE HOSTNAMES
env.hostnames = {
    'host1': ['install'],
}

# OPENSTACK ADMIN PASSWORD
env.openstack_admin_password = 'contrail'

# NODE PASSWORDS
env.passwords = {
    host1: 'contrail',
    host_build: 'contrail',
}

