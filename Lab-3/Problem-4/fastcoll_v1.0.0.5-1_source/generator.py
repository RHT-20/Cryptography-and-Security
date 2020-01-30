import subprocess
from hashlib import sha256

def generateSuffix():

    fpS = open("finalSuffix", "a")

    for i in range(0, 64):

        file = "file" + str(i)
        fpF = open(file, "rb")
        strF = fpf.read()
        fpF.close()

        if not i:
            text = "if sha256(blob).hexdigest() == " + "\"" + sha256(strF).hexdigest() + "\":"
            fpS.write(text)
            text = "MD. Rakibul Hasan, Guess: " + str(i)
            fpS.write(text)
        else:
            text = "elif sha256(blob).hexdigest() == " + "\"" + sha256(strF).hexdigest() + "\":"
            fpS.write(text)
            text = "MD. Rakibul Hasan, Guess: " + str(i)
            fpS.write(text)
    fpS.close()


def concate():

    for i in range(0, 64):
        f1 = "/FinalFiles/guess" + str(i) + ".py"
        call("cat finalPrefix > " + f1, shell=True)
        f2 = "file" + str(i)
        call("cat " + f2 + " >> " + f1, shell=True)






def main():
    generateSuffix()
    
if __name__ == main():
    main()
    
