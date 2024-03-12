import random
J1=input ("Nombre del jugador 1-> ")
J2=input ("Nombre del jugador 2-> ")
c1=0
c2=0
primos=[2,3,5,7,11]
while c1<5 and c2<5:

    r=random.randint(0,1)
    if r==0:
        c1<4:
        c1+=1
        print ("Marcador:",c1,"-",c2)
    else:
        d1=random.randint(1,6)+random.randint(1,6)
        print(J1,"Obtuvo",d1, "Al lanzar el dado")
        if d1 in primos:
            c1+=1
            print ("Marcador",c1,"-",c2)
        else:
            print(J1)