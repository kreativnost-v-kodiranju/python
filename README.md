# Osnovni koncepti in konstrukti

## 1  Delo s Pythonom

S Pythonom komuniciramo prek interaktivne konzole, do katere lahko
dostopamo na več načinov:
- neposredno iz ukazne vrstice,
- z uporabo enostavnega okolja IDLE, ki je priloženo vsaki namestitvi
  Pythona,
- ali pa prek kakšnega od naprednejših razvijalskih okolij, na primer **Visual Studio Code** ali
**PyCharmCE**.

## 2  Pisanje pregledne kode

Python ima visoke standarde glede kakovosti in estetike. Imena spremenljivk naj vsebujejo več kot eno črko, česar smo navajeni v matematiki. V kodiranju je zelo pomembno, da so imena čimbolj opisna, saj tako hitreje razumemo, kaj počne program. Za jasnejšo predstavo o spremenljivkah in njihovem pomenu velja dogovor o zapisu njihovih imen: enostavna imena so zapisana z eno
besedo, sestavljena pa iz zaporedja več besed, ki jih pritaknemo drugo za drugo, med seboj pa jih ločimo z veliko začetnico (**mixedCase** notacija z malo začetnico na začetku). Smiselna imena in ustrezni presledki kodo naredijo veliko bolj
razumljivo in berljivo.

## 3  Komentarji

Komentarji so programerjeve opombe v programski kodi, namenjene bralcu — sebi ali nekomu drugemu, ki bo to bral za njim. Interpreter jih ignorira. V Pythonu obstajajo enovrstični in večvrstični komentarji. Enovrstični komentarji se začnejo z znakom **#**, vse za tem znakom v vrsti se ignorira (tako lahko # uporabimo na začetku vrste ali pa pozneje).
Večvrstični komentarji se začnejo in končajo s trojnim narekovajem **”””**, vse med začetkom in koncem pa se ignorira.
Komentarje se ponavadi napiše za uvod/obrazložitev programa, pred manj razumljiv del kode, da obrazložimo njeno delovanje, ali pa če želimo kakšen del kode trenutno umakniti iz programa, ne da bi ga izbrisali. Komentarji pogosto tudi obrazložijo in dokumentirajo kodo in narekujejo njeno uporabo. 
Primer rabe obeh vrst komentarjev:

```python
"""
Primerek
programske
kode
"""

i = 0 # začetna vrednost števca
```

## 4  Števila in aritmetične operacije

Python v osnovi podpira dve vrsti števil — **cela števila** (integer, okr. int) in **realna števila** v formatu plavajoče pike (float, double). Za cela števila ni omejitve na dolžino, decimalna števila pa imajo standardne omejitve, a so za naše računanje dovolj dobra. Veljavne vrednosti decimalnih števila sta tudi obe neskončnosti in ”NaN”, ki pomeni “Not a number”. Cela števila dobimo iz drugih tipov s funkcijo **int**, decimalna pa s funkcijo **float**.
V Pythonu izvajamo nad števili naslednje osnovne računske operacije s pripadajočimi operatorji:
- **+** za seštevanje,
- **-** za odštevanje,
- **\*** za množenje in
- **\**** za potenciranje.
Za deljenje Python pozna dve operaciji:
- **/** za običajno deljenje in
- **//** za celoštevilsko deljenje, ki zavrže morebitni ostanek.
Če želimo izračunati samo ostanek, uporabimo operator **%**. Prioriteta operatorjev je določena tako kot običajno: najtesneje veže potenciranje, nato množenje in deljenji, nazadnje pa seštevanje in odštevanje. Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Za lažjo berljivost programske kode po dogovoru na vsaki strani operatorja prirejanja vrednosti spremenljivke in dvomestne operacije pišemo presledek, prav tako pišemo presledek za ločili, pred njimi pa ne. 
Primeri programske kode:

```python
imeSpremenljivke = vrenostKiJoZelimoShraniti # prireditveni stavek
y = x + 3
z = (x + 2 * y) ** (1 / 2)
x += c
a = 123456 # celo število
b = 123.456 # decimalno število
```

## 5  Logične vrednosti

Poleg števil Python pozna tudi logični vrednosti **True** in **False**, ki označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat primerjav, kot so enakost z operatorjem **==**, neenakost z operatorjem **!=** ali urejenostne relacije **<, >, <=, >=**, ter prek logičnih operacij and, or in not. Uporabo logičnih operacij izvedemo z logičnimi izrazi, ki opredeljujejo enostavne ali sestavljene pogoje. Sestavljene pogoje dobimo s kombinacijo enostavnih z uporabo logičnih operacij. 
Primeri programske kode:

```python
p1 = (a == 0) and (b != 0)
(3 < 5) or (10 > 20) # vrne True
```

## 6  Pogojni stavek

Zaporedno izvrševanje programske kode ter s tem toka ukazov in podatkov spreminjamo s krmilnimi stavki, ki vsebujejo **logične izraze**. Če želimo, da se naš program pod drugačnimi pogoji (logične vrednosti) obnaša različno, uporabimo **if** stavek. 
Če je pogojev več, lahko za **if** uporabimo še razširjeni pogojni stavek **elif** (**else if**), ki doda dodatne pogoje. 
Če imamo pogojev veliko, **elif** uporabimo večkrat. Za konec pa lahko damo še **else**, ki se izvede takrat, ko ni bil izpolnjen noben od pogojev v **if** in **elif** stavkih. **elif** in **else** deli niso obvezni. 
Primer programske kode:

```python
"""Osnovni if stavek"""
if (pogoj):
# stavki, ki jih izvedemo,
# ko pogoj drži
else:
# stavki, ki jih izvedemo,
# ko pogoj ne drži
"""Razširjeni pogojni stavek if — elif"""
if (pogoj1):
# stavki, ki jih izvedemo,
# ko pogoj1 drži
elif (pogoj2):
# stavki, ki jih izvedemo,
# ko pogoj1 ne drži, ampak drži pogoj2
elif (pogoj3):
# stavki, ki jih izvedemo,
# ko tudi pogoj2 ne drži, ampak drži pogoj3
else:
# stavki, ki jih izvedemo,
# ko noben od pogojev ne drži
```

## 7  Zanke

Zanke v kodiranju uporabljamo takrat, kadar želimo enega ali več stavkov določenega dela programske kode ponoviti večkrat zaporedoma. Vsaki posamezni izvedbi ponovitve, pri kateri se neko stanje spreminja, pravimo **iteracija**. Poznamo dve osnovni obliki iteracije:
- **iteracija prek oštevilčenih množic** in
- **iteracija, krmiljena z logičnimi izrazi**.
Včasih že vnaprej vemo, kolikokrat bomo določene stavke ponovili. V teh primerih uporabimo iteracijo prek oštevilčenih množic, ki jo realiziramo s **for** zanko. 
Primer zapisa **for** zanke:

```python
for spremenljivka in zbirka:
# se izvaja dokler spremenljivka ne preteče vseh elementov zbirke
```

Spremenljivka preteče vse elemente dane zbirke, ki je lahko razpon števil, seznam, niz znakov, slovar ipd. Na začetku for zanko uporabljamo skupaj s funkcijo **range(n)**, ki vrne vse elemente v razponu od 0 do n – 1, ter funkcijo **range(a, b)**, ki vrne vse elemente v razponu od vključno prvega (a) do tistega pred drugim (b – 1).
Kadar želimo, da se določeni stavki programske kode ponavljajo toliko časa, dokler velja nek pogoj, uporabimo **while** zanko. Primer zapisa **while** zanke:

```python
while (pogoj):
# se izvaja dokler je pogoj izpolnjen
```

Pri while zanki moramo biti zelo pozorni na **neskončne zanke**. Neskončna zanka se zgodi takrat, ko je pogoj vedno izpolnjen, program pa bo tekel v neskončnost. Če se nam to slučajno zgodi, pritisnemo kombinacijo tipk **ctrl+c**, s čimer izvajanje programa prekinemo.

## 8  Stavki *break*, *continue* in *pass*

V zankah lahko uporabimo tudi posebne ukaze, ki spreminjajo običajen potek programskih stavkov. Če kjerkoli v zanki napišemo ukaz **break**, bo zanka takrat prekinjena. Občasno programiramo tudi tako, da zanalašč naredimo neskončno zanko, in potem ob določenih pogojih pokličemo **break**. Ukaz break prekine le ”najbližjo” zanko — če imamo gnezdenih več zank (npr. for zanka znotraj while zanke) se bo prekinila le notranja zanka (v našem primeru for zanka).
Stavek **continue** je podoben stavku **break**, le da ne prekine najbolj notranje zanke, ampak preskoči vse do konca trenutne iteracije in takoj začne izvajanje naslednje. To je uporabno na primer za filtriranje neveljavnih podatkov. Stavek
**continue** lahko vedno nadomestimo z ustreznim **if else** stavkom, a je to lahko veliko manj berljivo.
Stavek **pass** lahko uporabljamo kjerkoli v Pythonu, ne le v zankah. Najpogosteje ga uporabimo takrat, kadar Python zahteva, da napišemo vsaj en ukaz, vendar ne želimo storiti ničesar. Stavek pass ne stori ničesar, zato ga lahko pustimo v kodi.

## 9  Funkcije

Funkcije so zelo uporabljene strukture v kodiranju. Zaradi splošnosti in lepih načinov za dodajanje novih funkcionalnosti in zato, ker naredijo kodo mnogo bolj berljivo in uporabno so eden najpomembnejših konceptov, ki se je zelo razvit in zelo pomemben v resnem programiranju. Velika prednost funkcij je to, da ni potrebno vedeti, kako točno deluje (lahko nam kakšno funkcijo npr. napiše kdo drug, jo skopiramo iz interneta itd.). Poleg tega funkcije naredijo kodo lažje za vzdrževanje, saj omogočajo preprosto popravljanje in spreminjanje. Če namreč v funkciji pride do kakšne napake, lahko napako popravimo le v definiciji, namesto da bi jo morali popraviti povsod, kjer funkcijo uporabimo.
Funkcijo vedno začnemo z rezervirano besedo **def**, nato pride **ime funkcije** (kot ime spremenljivke mora biti nujno iz ene besede) in v oklepaju poljubno število **parametrov**. Telo funkcije je potrebno zamakniti. 
Primer zapisa funkcije:

```python
def imeFunkcije(parameter1, parameter2):
# koda, ki se izvede, ko pokličemo funkcijo
```

Če hočemo, da funkcija kaj vrne, to povemo z ukazom return. Ko funkcija nekaj vrne, lahko to ujamemo in s tem nekaj naredimo (npr. shranimo v spremenljivko, izpišemo itd.) ali pa ne naredimo ničesar — s tem bo stvar, ki jo je funkcija vrnila, izgubljena. Ko se v funkciji izvede return ukaz, se funkcija konča, tudi če je pod stavkom še kaj kode. Če ukaza return ni, potem funkcija na koncu vrne None.
Ko izvedemo program, ki vsebuje samo definicije funkcij, se ne zgodi nič. Funkcijo je treba namreč še poklicati (po imenu). Naše funkcije kličemo popolnoma enako kot že vdelane funkcije (npr. print(), range(), ...)
Primer zapisa funkcije s klicanjem funkcije:

```python
def f(x,y):
 Funkcija f, ki pri danih parametrih x, y izračuna … ”””
  r = i1(x, y) # poljuben izraz za izračun vrednosti r
  t = i2(x, y) # poljuben izraz za izračun vrednosti t
  return (r,t)
  
a =
b =
(u,v) = f(a,b) # prirejanje vrednosti funkcije f argumentoma u in v
```
