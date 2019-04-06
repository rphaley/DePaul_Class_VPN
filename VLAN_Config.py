def makeLayer3Vlan(classNum, inNet,vlan,users):
    f = open('VLAN_Layer3_config.txt','a')
    for i in range(1,users):
        if i <10:
            f.write('''vlan {0}0{1}
name CNS{2}_STUDNET{1}_VLAN
access-list 2{0}0{1} remark CNS{2}_STUDNET{1}_ACL
access-list 2{0}0{1} permit ip any 10.{3}.{1}.0 0.0.0.255
access-list 2{0}0{1} deny ip any 10.0.0.0 0.255.255.255
access-list 2{0}0{1} permit ip any any
int vlan {0}0{1}
description CNS{2}_STUDNET{1}
ip address 10.{3}.{1}.254 255.255.255.0
no shut
ip access-group 2{0}0{1} in
access-list MGMT_VPN_TUNNEL_LIST extended permit ip object SSL_CNS{2}_NET object ADMIN_SSL_NET
router ospf 1000
network 10.1{1}.0.0 0.0.255.255 area 0\n!\n!\n'''.format(vlan,i,classNum,inNet))
        else:
            f.write('''vlan {0}{1}
name CNS{2}_STUDNET{1}_VLAN
access-list 2{0}{1} remark CNS{2}_STUDNET{1}_ACL
access-list 2{0}{1} permit ip any 10.{3}.{1}.0 0.0.0.255
access-list 2{0}{1} deny ip any 10.0.0.0 0.255.255.255
access-list 2{0}{1} permit ip any any
int vlan {0}{1}
description CNS{2}_STUDNET{1}
ip address 10.{3}.{1}.254 255.255.255.0
no shut
ip access-group 2{0}{1} in\n!\n!\n'''.format(vlan,i,classNum,inNet))
            
    f.close()

def makeLayer2Vlan(classNum, inNet,vlan,users):
    f = open('VLAN_Layer2_config.txt','a')
    for i in range(1,users):
        if i <10:
            f.write('''vlan {0}0{1}
name CNS{2}_STUDNET{1}_VLAN\n!\n!\n'''.format(vlan,i,classNum,inNet))
        else:
            f.write('''vlan {0}{1}
name CNS{2}_STUDNET{1}_VLAN\n!\n!\n'''.format(vlan,i,classNum,inNet))
            
    f.close()

