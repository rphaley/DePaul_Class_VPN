import random

def makePass(classNum, chars,users):
    f = open('Passconfig.txt','a')
    g = open('PassList.csv','a')

    for i in range(1,users):
        password = ''
        for j in range(10):
            password += random.choice(chars)
        f.write('username CNS{}-student{} password {} privilege 0\n!\n'.format(classNum,i,password))
        g.write('student{},{}\n'.format(i, password))
    f.close()
    g.close()
