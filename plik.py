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
    wariancja =wariancja/6
    print(f"Suma to:{suma},Srednia to:{srednia},najwieksza liczba to:{maxx}, a najmniejsza:{minn}, wariancja to:{wariancja}")
def Pr3():
    aa = open("in.txt","r")
    ab = open("dict.txt","r")
    ac = open("dict.txt","a")
    text = aa.read()
    for i in text:
        if i=="," or i=="." or i==";" or i=='"':
            i=""
    text.lower()
    text.split(" ")
    aa.split(" ")
    for i in aa:
        if i not in ab:
            ac.write(" "+i)
    aa.close()
    ab.close()
    ac.close()
            
        
             

            
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
Pr3()
 