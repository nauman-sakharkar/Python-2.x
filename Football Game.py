def isprime(num):
    result = True
    if (num>1):
        for i in range(2,num):
            if (num%i)==0:   
              result=False
              break
        return result 
    else:
        return not result

    
def evennum(num):
    if num%2==0:
        return True
    else:
        return False

    
def oddnum(num):
    if num%2==0:
        return False
    else:
        return True

def com_g(c):
    print("----------------------------------------------")
    if c==0:
        print("Goal! right footed shot from outside the box to the top right corner.")
    if c==1:
        print("Goal! header from very close range to the centre of the goal.")
    if c==2:
        print("Goal! left footed shot from the left side of the box to the bottom right corner.")
    if c==3:
        print("Goal! right footed shot from the centre of the box to the bottom right corner.")
    if c==4:
        print("Goal! left footed shot from the centre of the box to the bottom left corner")
    if c==5:
        print("Goal! from a free kick with a right footed shot to the top left corner.")
    if c==6:
        print("Goal! right footed shot from a difficult angle on the left to the bottom left corner")
    if c==7:
        print("Goal! header from the centre of the box to the top left corner.")
    if c==8:
        print("Goal! right footed shot from the centre of the box to the bottom right corner.")
    if c==9:
        print("Goal! right footed shot from the centre of the box to the centre of the goal.")

def Game1(g):
    a=int(input(PlayerName1))
    b=int(input(PlayerName2))
    print("=============================================")
    import random
    a11=random.randint(0,a+1)
    b11=random.randint(0,b+1)
    if isprime(a11)==True and isprime(b11)==True or evennum(a11)==True and evennum(b11)==True or oddnum(a11)==True and oddnum(b11)==True:
        Bp2(a11)
        blocked1(a)
    elif isprime(a11)==True and evennum(b11)==True or evennum(a11)==True and oddnum(b11)==True or oddnum(a11)==True and isprime(b11)==True:
        Cp1(a11)
        continues1(a)
    elif isprime(a11)==True and oddnum(b11)==True or evennum(a11)==True and isprime(b11)==True or oddnum(a11)==True and evennum(b11)==True:
        g=("Game")
        Gp1(g)
        goal1(g)

def Game2(g):
    a=int(input(PlayerName2))
    b=int(input(PlayerName1))
    print("=============================================")
    import random
    a11=random.randint(0,a+1)
    b11=random.randint(0,b+1)
    if isprime(a11)==True and isprime(b11)==True or evennum(a11)==True and evennum(b11)==True or oddnum(a11)==True and oddnum(b11)==True:
        Bp1(a11)
        blocked2(a)
    elif isprime(a11)==True and evennum(b11)==True or evennum(a11)==True and oddnum(b11)==True or oddnum(a11)==True and isprime(b11)==True:
        Cp2(a11)
        continues2(a)
    elif isprime(a11)==True and oddnum(b11)==True or evennum(a11)==True and isprime(b11)==True or oddnum(a11)==True and evennum(b11)==True:
        g=("Game")
        Gp2(g)
        goal2(g)


def Penalty(Football):
    count1=0
    count2=0
    G=int(input("Please Enter The Goals = "))
    print("=============================================")
    for i in range(G):
        a=int(input(PlayerName1))
        b=int(input(PlayerName2))
        print("=============================================")
        print("Commentary : ")
        print("----------------------------------------------")
        a11=random.randint(0,a)
        b11=random.randint(0,b)
        if isprime(a11)==True :
            print("Goal")
            goal1(g)
        if isprime(b11)==True:
            print("Goal")
            goal2(g)
        else:
            print(PN1,"Missed It")
    z=0
    final(z)

def Bp1(t):
    if team=="y":
        if t1=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp1=FCB1[s]
        elif t1=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp1=RM1[s]
        elif t1=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp1=BM1[s]
        elif t1=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp1=AM1[s]
        elif t1=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp1=S1[s]
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",bp1,"of",PN1)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN1)
    elif team1=="y":
        global m1
        global z1
        s=random.randint(0,z1-1)
        bp1=m1[s]
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",bp1,"of",PN1)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN1)
    else:
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",PN1)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN1)

def Bp2(t):
    if team=="y":
        if t2=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp2=FCB1[s]
        elif t2=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp2=RM1[s]
        elif t2=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp2=BM1[s]
        elif t2=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp2=AM1[s]
        elif t2=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp2=S1[s]
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",bp2,"of",PN2)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN2)
    elif team1=="y":
        global m2
        global z1
        s=random.randint(0,z1-1)
        bp2=m2[s]
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",bp2,"of",PN2)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN2)
    else:
        print("Great Defending")
        print("----------------------------------------------")
        print("Blocked by",PN2)
        print("----------------------------------------------")
        print("Now Ball is with the ",PN2)

def Cp1(t):
    if team=="y":
        if t1=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp1=FCB1[s]
        elif t1=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp1=RM1[s]
        elif t1=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp1=BM1[s]
        elif t1=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp1=AM1[s]
        elif t1=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp1=S1[s]
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(bp1,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN1)
    elif team1=="y":
        global m1
        global z1
        print(m1)
        s=random.randint(0,z1-1)
        bp1=m1[s]
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(bp1,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN1)
    else:
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(PN1,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN1)

def Cp2(t):
    if team=="y":
        if t2=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp2=FCB1[s]
        elif t2=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp2=RM1[s]
        elif t2=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp2=BM1[s]
        elif t2=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp2=AM1[s]
        elif t2=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp2=S1[s]
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(bp2,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN2)
    elif team1=="y":
        global m2
        global z1
        s=random.randint(0,z1-1)
        bp2=m2[s]
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(bp2,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN2)
    else:
        print("Good Dribbling Skills")
        print("----------------------------------------------")
        print(PN2,"Moving Towards Goal.","This Can Be A Goal")
        print("----------------------------------------------")
        print("Still Ball is with the ",PN2)

def Gp1(t):
    if team=="y":
        if t1=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp1=FCB1[s]
        elif t1=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp1=RM1[s]
        elif t1=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp1=BM1[s]
        elif t1=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp1=AM1[s]
        elif t1=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp1=S1[s]
        print("Goal from",bp1,"of",PN1)
    elif team1=="y":
        global m1
        global z1
        s=random.randint(0,z1-1)
        bp1=m1[s]
        print("Goal from",bp1,"of",PN1)
    else:
        print("Goal from",PN1)
    c=random.randint(0,9)
    com_g(c)
    

def Gp2(t):
    if team=="y":
        if t2=="FCB":
            FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
            FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
            s=random.randint(0,10)
            bp2=FCB1[s]
        elif t2=="Real Madrid C.F.":
            RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
            RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
            s=random.randint(0,10)               
            bp2=RM1[s]
        elif t2=="Bayern München":
            BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
            BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
            s=random.randint(0,10)
            bp2=BM1[s]
        elif t2=="Atlético Madrid":
            AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
            AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
            s=random.randint(0,10)
            bp2=AM1[s]
            print (bp2)
        elif t2=="Sevilla FC":
            S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
            S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
            s=random.randint(0,10)
            bp2=S1[s]
        print("Goal from",bp2,"of",PN2)        
    elif team1=="y":
        global m2
        global z1
        s=random.randint(0,z1-1)
        bp2=m2[s]
        print("Goal from",bp2,"of",PN2)
    else:
        print("Goal from",PN2)
    c=random.randint(0,9)
    com_g(c)
    


def blocked1(b):
    print("----------------------------------------------")
    g=("Game")
    Game2(g)
    
def blocked2(b):
    print("----------------------------------------------")
    g=("Game")
    Game1(g)

def continues1(c):
    print("----------------------------------------------")
    g=("Game")
    Game1(g)
    
def continues2(c):
    print("----------------------------------------------")
    g=("Game")
    Game2(g)
    
e=0
def count11(c):
    global e
    e=e+1
    count1(e)

def count1(c):
    global e
d=0
def count22(c):
    global d
    d=d+1
    count2(d)

def count2(c):
    global d
    

def goal1(g):
    c=0
    count11(c)
    
def goal2(g):
    c=0
    count22(c)

def Man_Match1(m):
    if t1=="FCB":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
        FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
        man=random.randint(0,10)
        print(FCB1[man],"From",t1)
    elif t1=="Real Madrid C.F.":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
        RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
        man=random.randint(0,10)
        print(RM1[man],"From",t1)
    elif t1=="Bayern München":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
        BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
        man=random.randint(0,10)
        print(BM1[man],"From",t1)
    elif t1=="Atlético Madrid":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
        AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
        man=random.randint(0,10)
        print(AM1[man],"From",t1)
    elif t1=="Sevilla FC":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
        S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
        man=random.randint(0,10)
        print(S1[man],"From",t1)
    elif team1=="y":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        global m1
        global z1
        man=random.randint(0,z1-1)
        print(m1[man],"From",t1)
    print("=============================================")
def Man_Match2(m):
    if t2=="FCB":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        FCB1={0:"Ter Stegen(1)",1:"Piqué(3)",2:"I. Rakitić(4)",3:"Busquets(5)",4:"Denis Suárez(6)",5:"Arda(7)",6:"A. Iniesta (Captain)(8)",7:"Suárez(9)",8:"Messi (Vice-Captain)(10)",9:"Neymar Jr(11)",10:"Mascherano(14)"}
        FCB2={0:"Rafinha(12)",1:"Cillessen(13)",2:"Jordi Alba(18)",3:"Paco Alcácer(17)"}
        man=random.randint(0,10)
        print(FCB1[man],"From",t2)
    elif t2=="Real Madrid C.F.":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        RM1={0:"Keylor Navas(1)",1:"Dani Carvajal(2)",2:"Pepe (2nd VC)(3)",3:"Sergio Ramos(C)(4)",4:"Raphaël Varane(5)",5:"Cristiano Ronaldo(3rd VC)(7)",6:"Toni Kroos(8)",7:"Karim Benzema(9)",8:"James Rodríguez(10)",9:"Gareth Bale(11)",10:"Marcelo(VC)(12)"}
        RM2={0:"Casemiro(14)",1:"Kiko Casilla(13)",2:"Mariano Díaz(18)",3:"Lucas Vázquez(17)"}
        man=random.randint(0,10)
        print(RM1[man],"From",t2)
    elif t2=="Bayern München":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        BM1={0:"Manuel Neuer(1)",1:"Mats Hummels(5)",2:"Thiago(6)",3:"Franck Ribéry(7)",4:"Javi Martínez (8)",5:"Robert Lewandowski(9)",6:"Arjen Robben(10)",7:"Douglas Costa(11)",8:"Xabi Alonso(14)",9:"Jérôme Boateng(17)",10:"Philipp Lahm(captain)(21)"}
        BM2={0:"Jérôme Boateng(17)",1:"Arturo Vidal(23)",2:"Juan Bernat(18)",3:"Tom Starke(22)"}
        man=random.randint(0,10)
        print(BM1[man],"From",t2)
    elif t2=="Atlético Madrid":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        AM1={0:"Miguel Ángel Moyà(1)",1:"Diego Godín(2)",2:"Filipe Luís(3)",3:"Gabi Captain(C)(14)",4:"Tiago(5)",5:"Antoine Griezmann(7)",6:"Saúl(8)",7:"Fernando Torres(9)",8:"Yannick Ferreira Carrasco(10)",9:"Ángel Correa(11)",10:"Augusto Fernández(12)"}
        AM2={0:"Stefan Savić(15)",1:"Jan Oblak(13)",2:"Šime Vrsaljko(16)",3:"Alessio Cerci(17)"}
        man=random.randint(0,10)
        print(AM1[man],"From",t2)
    elif t2=="Sevilla FC":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        S1={0:"Sergio Rico(1)",1:"Benoît Trémoulinas(2)",2:"Mariano(3)",3:"Matías Kranevitter(4)",4:"Timothée Kolodziejczak(5)",5:"Michael Krohn-Dehli(7)",6:"Vicente Iborra(Captain)(8)",7:"Luciano Vietto(9)",8:"Samir Nasri(10)",9:"Joaquín Correa(11)",10:"Wissam Ben Yedder(12)"}
        S2={0:"Daniel Carriço(Vice-Captain)(6)",1:"David Soria(13)",2:"Steven N'Zonzi(15)",3:"Pablo Sarabia(17)"}
        man=random.randint(0,10)
        print(S1[man],"From",t2)
    elif team1=="y":
        print("=============================================")
        print("Man Of The Match")
        print("----------------------------------------------")
        global m2
        global z1
        man=random.randint(0,z1-1)
        print(m2[man],"From",t1)
    print("=============================================")


def final(f):
    c=("")
    count1(c)
    count2(c)
    print("=============================================")
    print("Final Scores")
    print(PN1," : ",e)
    print(PN2," : ",d)
    if e>d:
        Man_Match1(e)
    if e<d:
        Man_Match2(e)
    if e>d:
        print("Congratulations!!! ",PN1,"Won")
        print("============================================")
    if e<d:
        print("Congratulations!!! ",PN2,"Won")
        print("=============================================")
    if e==d:
        P=input("Do You Want Penalty Shootout : ")
        if P=="Y":
            print("Let's Move To The Penalty Shootout : ")
            print("----------------------------------------------")
            print("Penalty Shootout")
            print("----------------------------------------------")
            Football="Penalty Shootout"
            Penalty(Football)
        else:
            P=="N"
            man=random.randint(0,9)
            if evennum(man):
                Man_Match1(man)
            if oddnum(man):
                Man_Match2(man)
            print("Draw")
            

def Game(Football):
    global e
    e=0
    global d
    d=0
    for j in range(1):
        G=int(input("Number of Game = "))
        print("=============================================")
        for i in range(G):
            a=int(input(PlayerName1))
            b=int(input(PlayerName2))
            print("=============================================")
            print("Commentary : ")
            print("----------------------------------------------")
            print("First Half begins.")
            print("----------------------------------------------")
            print("Lineups are announced and players are warming up.")
            print("----------------------------------------------")
            import random
            a11=random.randint(0,a)
            b11=random.randint(0,b)
            if isprime(a11)==True and isprime(b11)==True or evennum(a11)==True and evennum(b11)==True or oddnum(a11)==True and oddnum(b11)==True:
                Bp2(a11)
                blocked1(a)
            elif isprime(a11)==True and evennum(b11)==True or evennum(a11)==True and oddnum(b11)==True or oddnum(a11)==True and isprime(b11)==True:
                Cp1(a11)
                continues1(a)
            elif isprime(a11)==True and oddnum(b11)==True or evennum(a11)==True and isprime(b11)==True or oddnum(a11)==True and evennum(b11)==True:
                g=("Game")
                Gp1(g)
                goal1(g)
            if G>1:
                print("")
                print("==================Second-Game=============================")
                print("")
        z=0
        final(z)            
        C=input("Do You Want 1 More Match = ")
        if C=="y":
            print("=============================================")
            print("Another Game")
            print("=============================================")
            del e
            del d
            Football="Another Game"
            Game(Football)
        if C=="n":
            print("Thank You")
            print("")
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            import sys
            sys.exit()



import random
print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
print("")
print("Registered Teams")
print("----------------------------------------------")
print("FCB")
print("Real Madrid C.F.")
print("Bayern München")
print("Atlético Madrid")
print("Sevilla FC")
print("=============================================")
team=input("Do You Want To Play With The Registered Team : ")
if team=="y":
    print("----------------------------------------------")
    PlayerName1="Player 1, Please Enter Your Team Name = "
    t1=input(PlayerName1)
    PlayerName2="Player 2,  Please Enter Your Team Name = "
    t2=input(PlayerName2)
    PlayerName1=t1+" , Please Enter Your Number = "
    PlayerName2=t2+", Please Enter Your Number = "
    PN1=t1
    PN2=t2
else:
    team1=input("Do You Want To Play With The Your Team : ")
    if team1=="y":
        print("----------------------------------------------")
        z1=int(input("How many players will be playing in each Team ? : "))
        print("----------------------------------------------")
        print("Team 1")
        print("----------------------------------------------")
        PlayerName1=input("Enter Your Team Name : ")
        PN1=PlayerName1
        m1={}
        for i in range (z1):
            m1[i]=input("Name(No.) : ")
        print("----------------------------------------------")
        print("Team 2")
        print("----------------------------------------------")
        PlayerName2=input("Enter Your Team Name : ")
        PN2=PlayerName2
        m2={}
        for i in range (z1):
            m2[i]=input("Name(No.) : ")
        t1=PN1
        t2=PN2
        PlayerName1=PlayerName1+" , Please Enter Your Number = "
        PlayerName2=PlayerName2+", Please Enter Your Number = "
    if team1=="n":
        print("----------------------------------------------")
        PlayerName1=input("Please Enter The Player 1 Name : ")
        PN1=PlayerName1
        PlayerName2=input("Please Enter The Player 2 Name : ")
        PN2=PlayerName2
        PlayerName1=PlayerName1+" , Please Enter Your Number = "
        PlayerName2=PlayerName2+", Please Enter Your Number = "
        t1=PN1
        t2=PN2
for j in range(1):
    print("----------------------------------------------")
    G=int(input("Number of Game = "))
    print("=============================================")
    for i in range(G):
        a=int(input(PlayerName1))
        b=int(input(PlayerName2))
        print("=============================================")
        print("Commentary : ")
        print("----------------------------------------------")
        print("First Half begins.")
        print("----------------------------------------------")
        print("Lineups are announced and players are warming up.")
        print("----------------------------------------------")
        import random
        a11=random.randint(0,a)
        b11=random.randint(0,b)
        if isprime(a11)==True and isprime(b11)==True or evennum(a11)==True and evennum(b11)==True or oddnum(a11)==True and oddnum(b11)==True:
            Bp2(a11)
            blocked1(a)
        elif isprime(a11)==True and evennum(b11)==True or evennum(a11)==True and oddnum(b11)==True or oddnum(a11)==True and isprime(b11)==True:
            Cp1(a11)
            continues1(a)
        elif isprime(a11)==True and oddnum(b11)==True or evennum(a11)==True and isprime(b11)==True or oddnum(a11)==True and evennum(b11)==True:
            g=("Game")
            Gp1(g)
            goal1(g)
        if G>1:
            print("")
            print("==================Second-Game=============================")
            print("")
    z=0
    final(z)            
C=input("Do You Want 1 More Match = ")
if C=="y":
    print("=============================================")
    print("Another Game")
    print("=============================================")
    del e
    del d
    Football="Another Game"
    Game(Football)
if C=="n":
    print("Thank You")
    print("")
    print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
