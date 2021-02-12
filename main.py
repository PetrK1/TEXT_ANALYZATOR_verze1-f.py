TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 100 
feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',
]

#registrovani uzivatele

uzivatele={}
uzivatele.setdefault("osoba1", dict((("name",'bob'),("password",'123'))))
uzivatele.setdefault("osoba2", dict((("name",'ann'),("password",'pass123'))))
uzivatele.setdefault("osoba3", dict((("name",'mike'),("password",'password123'))))
uzivatele.setdefault("osoba4", dict((("name",'liz'),("password",'pass123'))))


#vstup uzivatele
username=input('username: ')
password=input('password: ')
print('-'*30)

#testovani, jestli odpovida uzivatelske jmeno a heslo nejakemu uzivateli
for klic in uzivatele:
    if uzivatele[klic]['name']==username and uzivatele[klic]['password']==password:
        print('Welcome to the app ',username)
        print('We have ',len(TEXTS),' texts to be analyzed')
        print('-'*30)
        break
else:
    print('Username or password is incorrect')
    exit()

#vyzve uzivatele, aby zadal cislo textu k analyze
text_number = input('enter  a number btw. 1 and 3 to select: ')

#overeni,jestli zadany udaj odpovida nejakemu clanku
if (text_number.isdigit() and int(text_number)>0 and int(text_number) in range(int(text_number)-1,len(TEXTS)+1)):
    pass
else:
    print('your choice is not correct')
    exit()

#vybere spravny index textu z listu TEXTS
cislo=int(text_number)-1
text_analyzed=TEXTS[cislo]

#rozdeli text na jednotliva slova
slova=text_analyzed.split(" ")

#vytvori seznam jednotlivych slov ocistenych od nezadoucich znaku
vycistena_slova = []
for slovo in slova:
  vycistena_slova.append(slovo.strip(".,: !"))

#vytvoreni slovniku pro vyskyt cetnosti jednotlivych druhu slov
vyskyt_slov = {}
vyskyt_slov['pocet']=len(vycistena_slova)

#vytvoreni slovniku pro frekvenci delek slov
frekvence_delky = {}

#Zjistovani druhu slov a zarazeni jejich poctu do slovniku
for cista_slova in vycistena_slova:
    if cista_slova.istitle():
        vyskyt_slov['poc_velka_pis'] = vyskyt_slov.setdefault('poc_velka_pis',0)+1
    elif cista_slova.isupper():
        vyskyt_slov['cela_velka_pis']= vyskyt_slov.setdefault('cela_velka_pis',0)+1
    elif cista_slova.islower():
        vyskyt_slov['mala_pismena']= vyskyt_slov.setdefault('mala_pismena',0)+1
    elif cista_slova.isdigit():
        vyskyt_slov['cisla']= vyskyt_slov.setdefault('cisla',0)+1
        vyskyt_slov['soucet']= vyskyt_slov.setdefault('soucet',0)+int(cista_slova)

    #Pocitani cetnosti slov jednotlivych delek
    frekvence_delky[len(cista_slova.strip())] = frekvence_delky.setdefault((len(cista_slova.strip())), 0) + 1

#Tvorba histogramu podle hodnot klice
histogram = sorted(frekvence_delky, key=frekvence_delky.get,reverse=False)

#serazeny histogram klicu
histogram_serazeny=sorted(histogram)

#Tisk statistiky analyzy
print('There are',vyskyt_slov.setdefault('pocet',0),' words in the selected text.')
print('There are',vyskyt_slov.setdefault('poc_velka_pis',0),' titlecase words.')
print('There are',vyskyt_slov.setdefault('cela_velka_pis',0),' uppercase words.')
print('There are',vyskyt_slov.setdefault('mala_pismena',0),' lowercase words.')
print('There are',vyskyt_slov.setdefault('cisla',0),' numeric strings.')
print('The sum of all the numbers', vyskyt_slov.setdefault('soucet',0))

#Tisk histogramu
print('-'*30)
print('LEN |','{:<20}'.format('OCCURENCES'),'| Nr.')
print('-'*30)

for _, cislo in enumerate(histogram_serazeny):
    print('{:<3}'.format(cislo), '|', '{:<20}'.format(frekvence_delky[cislo] * 'x'), '|', frekvence_delky[cislo])


