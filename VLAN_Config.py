def makeVlan(classNum, inNet,vlan,users):
    f = open('VLANconfig.txt','a')
    for i in range(1,users):
        if i <10:
            f.write('''vlan {}0{}
name CNS{}_STUDNET{}_VLAN
int vlan {}0{}
ip address 10.{}.{}.254 255.255.255.0
no shut\n!\n!\n'''.format(vlan,i,classNum,i,vlan,i,inNet,i))
        else:
            f.write('''vlan {}{}
name CNS{}_STUDNET{}_VLAN
int vlan {}{}
ip address 10.{}.{}.254 255.255.255.0
no shut\n!\n!\n'''.format(vlan,i,classNum,i,vlan,i,inNet,i))
            
    f.close()
