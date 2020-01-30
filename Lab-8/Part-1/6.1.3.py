import hashlib
from random import randint



def getRandomString():
    MX = 1000000000
    r1 = randint(0, MX)
    r2 = randint(0, MX)
    r3 = randint(0, MX)
    r4 = randint(0, MX)
    print(r1, r2, r3, r4)
    s = str(r1) + str(r2) + str(r3) + str(r4)
    return s


def isValidHash(s):


    #print(s)

    # L=len(s)
    idx= s.find("'='")

    if(idx!=-1):
        return True

    # if(idx==-1):
    #     idx=s.find("'or'")
    #
    # if (idx != -1):
    #     # if (idx + 4 < L and s[idx + 4] > '0' and s[idx + 4] <= '9'):
    #     if (s[idx + 4] > '0' and s[idx + 4] <= '9'):
    #         print(s[idx + 4])
    #         return True



    # else:
    #     if (idx+3<L and s[idx + 3] > '0' and s[idx + 3] <= '9'):
    #         print(s[idx + 3])
    #         return True

    return False

def findPassword():
    iter=0

    while(True):

        iter+=1
        print('iteration', iter)
        s=getRandomString()
        # s='129581926211651571912466741651878684928'

        res = hashlib.md5(s.encode())


        if(isValidHash(res.digest())==True):
            print('Found')
            print(s)
            print(res.digest())
            print("iterations",iter)
            break



findPassword()
