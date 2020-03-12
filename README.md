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

Python ima visoke standarde glede kakovosti in estetike. Imena spremenljivk
naj vsebujejo več kot eno črko, česar smo navajeni v matematiki. V kodiranju je
zelo pomembno, da so imena čimbolj opisna, saj tako hitreje razumemo, kaj
počne program. Za jasnejšo predstavo o spremenljivkah in njihovem pomenu
velja dogovor o zapisu njihovih imen: enostavna imena so zapisana z eno
besedo, sestavljena pa iz zaporedja več besed, ki jih pritaknemo drugo za drugo,
med seboj pa jih ločimo z veliko začetnico (**mixedCase** notacija z malo začetnico
na začetku). Smiselna imena in ustrezni presledki kodo naredijo veliko bolj
razumljivo in berljivo.

## 3  Komentarji

Komentarji so programerjeve opombe v programski kodi, namenjene bralcu —
sebi ali nekomu drugemu, ki bo to bral za njim. Interpreter jih ignorira.
V Pythonu obstajajo enovrstični in večvrstični komentarji.
Enovrstični komentarji se začnejo z znakom **#**, vse za tem znakom v vrsti se
ignorira (tako lahko # uporabimo na začetku vrste ali pa pozneje).
Večvrstični komentarji se začnejo in končajo s trojnim narekovajem **”””**, vse
med začetkom in koncem pa se ignorira.
Komentarje se ponavadi napiše za uvod/obrazložitev programa, pred manj
razumljiv del kode, da obrazložimo njeno delovanje, ali pa če želimo kakšen del
kode trenutno umakniti iz programa, ne da bi ga izbrisali. Komentarji pogosto
tudi obrazložijo in dokumentirajo kodo in narekujejo njeno uporabo. Primer
rabe obeh vrst komentarjev:

```python
"""
Primerek
programske
kode
"""

i = 0 # začetna vrednost števca
```

## 4  Števila in aritmetične operacije

Python v osnovi podpira dve vrsti števil — **cela števila** (integer, okr. int) in
**realna števila** v formatu plavajoče pike (float, double). Za cela števila ni omejitve na dolžino,
decimalna števila pa imajo standardne omejitve, a so za naše računanje dovolj
dobra. Veljavne vrednosti decimalnih števila sta tudi obe neskončnosti in
”NaN”, ki pomeni “Not a number”. Cela števila dobimo iz drugih tipov s
funkcijo **int**, decimalna pa s funkcijo **float**.
V Pythonu izvajamo nad števili naslednje osnovne računske operacije s
pripadajočimi operatorji:
- **+** za seštevanje,
- **-** za odštevanje,
- * za množenje in
- ** za potenciranje.
Za deljenje Python pozna dve operaciji:
- **/** za običajno deljenje in
- **//** za celoštevilsko deljenje, ki zavrže morebitni ostanek.
Če želimo izračunati samo ostanek, uporabimo operator **%**.
Prioriteta operatorjev je določena tako kot običajno: najtesneje veže
potenciranje, nato množenje in deljenji, nazadnje pa seštevanje in odštevanje.
Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Za lažjo
berljivost programske kode po dogovoru na vsaki strani operatorja prirejanja
vrednosti spremenljivke in dvomestne operacije pišemo presledek, prav tako
pišemo presledek za ločili, pred njimi pa ne. 
Primeri programske kode:

```python
imeSpremenljivke = vrenostKiJoZelimoShraniti # prireditveni stavek
y = x + 3
z = (x + 2 * y) ** (1 / 2)
x += c
a = 123456 # celo število
b = 123.456 # decimalno število
```

