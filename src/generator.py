import sys

class GeneratorKulWody:
    def __init__(self, iloscCzastek=None, stalaSieci=None):
        self.iloscCzastek = iloscCzastek if iloscCzastek is not None else 1
        self.stalaSieci = stalaSieci if stalaSieci is not None else 3.4
        self.wspolrzedne = []
        self.atomy = []
        self.wiazania = []
        self.katy = []
        self.licznikCzastek = 0

    def zwrocWspolrzedne(self):
        self.generujWspolrzedne()
        self.wspolrzedne.sort()
        return self.wspolrzedne

    def generujWspolrzedne(self):
        self.ustalPromien()
        promien = self.promien
        i = (0 - promien)//self.stalaSieci * self.stalaSieci
        while i <= promien:
            j = (0 - promien) //self.stalaSieci * self.stalaSieci
            while j <= promien:
                k = (0 - promien) //self.stalaSieci * self.stalaSieci
                while k <= promien:
                    if (i*i + j*j + k*k) <= (promien*promien):
                        self.wspolrzedne.append((i,j,k))
                    k=k+self.stalaSieci
                j=j+self.stalaSieci;
            i=i+self.stalaSieci;

    def ustalPromien(self):
        self.zgadnijPromien()
        flaga = 0
        licznik = 0
        while self.policzAtomy() is not self.iloscCzastek:
            if self.policzAtomy() >  self.iloscCzastek:
                self.zmniejszPromien()
                if flaga is 1:
                    break
                flaga = -1
            else:
                self.zwiekszPromien()
                flaga = 1
            licznik=licznik+1
            if licznik is 1000:
                exit()

    def policzAtomy(self):
        liczbaAtomow = 0
        promien = self.promien
        i = (0 - promien)//self.stalaSieci * self.stalaSieci
        while i <= promien:
            j = (0 - promien) //self.stalaSieci * self.stalaSieci
            while j <= promien:
                k = (0 - promien) //self.stalaSieci * self.stalaSieci
                while k <= promien:
                    if (i*i + j*j + k*k) <= (promien*promien):
                        liczbaAtomow = liczbaAtomow + 1
                    k=k+self.stalaSieci
                j=j+self.stalaSieci
            i=i+self.stalaSieci
        return liczbaAtomow

    def zgadnijPromien(self):
        obj = self.stalaSieci*self.stalaSieci*self.stalaSieci*self.iloscCzastek
        self.promien = (obj*3/4/3.14)**(1/3)

    def zwiekszPromien(self):
        self.promien = self.promien + self.stalaSieci/4

    def zmniejszPromien(self):
        self.promien = self.promien - self.stalaSieci/4

    def wstawCzastki(self):
        for wspolrzedna in self.wspolrzedne:
            self.wstawCzasteczke(wspolrzedna)
        #print("#" + str(self.licznikCzastek) + " molecules created")
            
    def wstawCzasteczke(self,wspolrzedna):
        self.licznikCzastek = self.licznikCzastek + 1
        x = wspolrzedna[0]
        y = wspolrzedna[1]
        z = wspolrzedna[2]
        self.dodajAtomy(x,y,z)
        self.dodajWiazania()
        self.dodajKaty()


    def wydrukujWynik(self):
        #self.atomy.sort()
        #self.wiazania.sort()
        #self.katy.sort()
        print("Atoms")
        print("")
        for a in self.atomy:
            self.drukujAtom(a)
        print("")
        print("Bonds")
        print("")
        for w in self.wiazania:
            self.drukujWiazanie(w)
        print("")
        print("Angles")
        print("")
        for k in self.katy:
            self.drukujKat(k)

    def dodajAtomy(self, x, y, z):
        lc = self.licznikCzastek
        offsetNumeru = (lc-1)*3
        self.atomy.append(str(offsetNumeru+1) + " " + str(lc) + " 1 " + str(x) +  " " +  str(y+0.8164904) + " " + str(z) + " 0.0")
        self.atomy.append(str(offsetNumeru+2) + " " + str(lc) + " 2 " + str(x+0.4238+0.8476) +  " " +  str(y+1.6229808) + " " + str(z+0.577359) + " 0.0")
        self.atomy.append(str(offsetNumeru+3) + " " + str(lc) + " 2 " + str(x+0.4238+0.8476) +  " " +  str(y)+ " " + str(z+0.577359) + " 0.0")
        
    def dodajWiazania(self):
        lc = self.licznikCzastek
        offsetNumeruWiazania = (lc-1)*2
        offsetNumeruAtomu = (lc-1)*3
        self.wiazania.append(str(offsetNumeruWiazania+1) + " 1 " + str(offsetNumeruAtomu+1) + " " + str(offsetNumeruAtomu+2))
        self.wiazania.append(str(offsetNumeruWiazania+2) + " 1 " + str(offsetNumeruAtomu+1) + " " + str(offsetNumeruAtomu+3))
    def dodajKaty(self):
        lc = self.licznikCzastek
        offsetAtomu = (lc-1)*3
        self.katy.append(str(lc) + " 1 " + str(offsetAtomu + 2) + " " + str(offsetAtomu + 1) + " " + str(offsetAtomu + 3))

    def drukujAtom(self,atom):
        print(atom)
        
    def drukujWiazanie(self,wiazanie):
        print(wiazanie)
        
    def drukujKat(self,kat):
        print(kat)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv)!=2:
        print("Program do generowania kul z wody")
        print("Przyjmuje jako argument ile cząstek wody ma być w kuli")
        print("Zwraca współrzędne atomów, wiązania i kąty")
        print("w formie pliku LAMMPS do przeczytania komendą read_data")
        exit()
    try:
        generator = GeneratorKulWody(int(sys.argv[1]))
        generator.generujWspolrzedne()
        generator.wstawCzastki()
        generator.wydrukujWynik()
    except Exception as blad:
        print("Nie udało się: " + blad)
    
