import random

from VPN_Configuration import *
from PasswordConfig import *
from VLAN_Config import *

users = 60 #Number of stuends/teams to create accounts for
classNum = '378'
chars = '0123456789abcdefghijklmnopqrstuvwxyz!@#$'
inNet = '10'
sslNet = '20'
vlan = '1'


##users = 5 #Number of stuends/teams to create accounts for
##classNum = '389'
##chars = '0123456789abcdefghijklmnopqrstuvwxyz!@#$'
##inNet = '11'
##sslNet = '21'
##vlan = '2'



makePass(classNum, chars, users+1)
makeVlan(classNum, inNet,vlan,users+1)
makeVPN(classNum, inNet, sslNet,users+1)
