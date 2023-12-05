def Pr1():
    x = open("dane.txt","r")
    x = x.read()
    x.close()
    x.split(" ")
    srednia=0
    suma = 0
    maxx = 0
    minn = 0
    wariancja = 0
    for i in x:
        if i>maxx:
            maxx = i
        if i<minn:
            minn = i
        suma+=i
    srednia = suma/len(x)
    for i in x:
        wariancja += (srednia-i)**2
    wariancja =wariancja/len(x)
    print(f"Suma to:{suma},Srednia to:{srednia},najwieksza liczba to:{maxx}, a najmniejsza:{minn}, wariancja to:{wariancja}")

        
             

            
def Pr2():
    x = open("in.txt","r")
    tekst= x.read()
    klucz = int(input("Podaj klucz "))
    zaszyfrowany = ""
    odszyfrowany = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(tekst[i])+ klucz -26)
        else:
            zaszyfrowany += chr(ord(tekst[i]) + klucz)
    print("Zaszyfrowany tekst:",zaszyfrowany)
    
    for d in range(len(zaszyfrowany)):
        if ord(zaszyfrowany[d]) > 122 - klucz:
            odszyfrowany += chr(ord(zaszyfrowany[d]) - klucz -26)
        else:
            odszyfrowany += chr(ord(zaszyfrowany[d]) - klucz)
    print("Odszyfrowany tekst:",odszyfrowany)




def Pr3():
    aa = open("in.txt","r")
    text = aa.read()
    #plik z tekstem text
    ac = open("dict.txt","a")
    
    #plik slownik text2
    ab = open("dict.txt","r")
    text2 = ab.read()
    zapisz = open("dict.txt","w")
    
    for i in text:
        if i=="," or i=="." or i==";" or i=='"':
            i.replace(".")
    
    text.lower()
    text.strip(".")
    text.split(" ")
    
    text2.split(" ")
    print(text)
    print(text2)
    
   
    
    powt = 0
    for i in text2:
        for j in text:
            if i==j:
                powt+=1
        if powt==0:
            text2.append(j)
        powt=0




    
    print(text2)
    print(text)
    text3=""
    for i in text2:
        text3+= " "+i
    zapisz.write(text3)
    zapisz.close()
    aa.close()
    ab.close()
    ac.close()


def zad3():
    with open('in_3.txt', 'r') as f:
        slowa = f.read().split()
        slownik = set()
        try:
            with open("dict.txt",'r') as f:
                slownik = set(line.strip() for line in f)

        except FileNotFoundError:
            with open('dict.txt', 'w') as f:
              pass
        slownik.update(word.lower() for word in slowa)

        with open('dict.txt','w') as f:
            for slowo in sorted(slownik):
                f.write(slowo+'\n')

zad3()
 