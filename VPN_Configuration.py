def makeVPN(classNum, inNet, sslNet,users):
    f = open('VPNconfig.txt','a')

    for i in range(1,users):
        f.write('''access-list CNS{}_Student{}_SSL_ACL standard permit 10.{}.{}.0 255.0.0.0
group-policy CNS{}_Student{}_GP internal
group-policy CNS{}_Student{}_GP attributes
 vpn-tunnel-protocol ssl-client
 split-tunnel-policy tunnelspecified
 split-tunnel-network-list value CNS{}_Student{}_SSL_ACL
!
ip local pool SSL_CNS{}_Student{}_POOL 172.{}.{}.1-172.{}.{}.100 mask 255.255.255.0
!
tunnel-group CNS{}_Student{}_TG type remote-access
tunnel-group CNS{}_Student{}_TG general-attributes
 address-pool SSL_CNS{}_Student{}_POOL
 default-group-policy CNS{}_Student{}_GP
tunnel-group CNS{}_Student{}_TG webvpn-attributes
 group-alias CNS{}_Student{}_NET enable
!
username CNS{}-student{} attributes
 group-lock value CNS{}_Student{}_TG
 service-type remote-access\n!\n!\n'''.format(classNum,i,inNet,i,classNum,i,classNum,i,classNum,i,classNum,i,sslNet,i,sslNet,i,classNum,i,classNum,i,
                                              classNum,i,classNum,i,classNum,i,classNum,i,classNum,i,classNum,i,classNum,i))
    f.close()
