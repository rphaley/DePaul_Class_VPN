import random

from VPN_Configuration import *
from PasswordConfig import *
from VLAN_Config import *

##users = 60 #Number of stuends/teams to create accounts for
##classNum = '378'
##chars = '0123456789abcdefghijklmnopqrstuvwxyz!@#$'
##inNet = '10'
##sslNet = '20'
##vlan = '100'


users = 70 #Number of stuends/teams to create accounts for
classNum = '340'
chars = '0123456789abcdefghijklmnopqrstuvwxyz!@#$'
inNet = '13'
sslNet = '23'
vlan = '4'



makePass(classNum, chars, users+1)
makeLayer3Vlan(classNum, inNet,vlan,users+1)
makeLayer2Vlan(classNum, inNet,vlan,users+1)
makeVPN(classNum, inNet, sslNet,users+1)
