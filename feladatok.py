import random
def eslo():
    szam=0
    i=0
    while szam<10 or szam>100:
        szam=int(input("addj meg egy kétszámjegyü számot!:"))


def masodik():
    szamlista=[]
    i2=0
    i=0
    while i<10:
        beszam=random.randint(-30,5)
        szamlista.append(beszam)
        i+=1
        if beszam<0:
            i2+=1
    print(szamlista)
    print(F"A számok között {i2} db negatív szám van!")


def harmadik(szoveg):
    i=-1
    szoveghossz=len(szoveg)
    szoveghossz2=szoveghossz-szoveghossz*2
    while i>=szoveghossz2:
        print(szoveg[i], end=" ")
        i-=1

def negyedik():
    szoveg=""
    i=0
    szavaklistaja=[]
    szoveg=input("adj meg egy szavat: (@=exit)")
    while szoveg!="@":
        szavaklistaja.append(szoveg)
        szoveg=input("adj meg egy szavat: (@=exit)")
    return szavaklistaja

def otodik(szavaklistaja):
    i=0
    i2=0
    szoszam=len(szavaklistaja)
    while szoszam>i:
        elemhossz=len(szavaklistaja[i])
        if elemhossz>=5:
            i2+=1
        i+=1
    print(F"{i2} db 5betüs szó van benne!")
