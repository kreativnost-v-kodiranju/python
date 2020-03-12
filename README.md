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
Enovrstični komentarji se začnejo z znakom #, vse za tem znakom v vrsti se
ignorira (tako lahko # uporabimo na začetku vrste ali pa pozneje).
Večvrstični komentarji se začnejo in končajo s trojnim narekovajem ”””, vse
med začetkom in koncem pa se ignorira.
Komentarje se ponavadi napiše za uvod/obrazložitev programa, pred manj
razumljiv del kode, da obrazložimo njeno delovanje, ali pa če želimo kakšen del
kode trenutno umakniti iz programa, ne da bi ga izbrisali. Komentarji pogosto
tudi obrazložijo in dokumentirajo kodo in narekujejo njeno uporabo. Primer
rabe obeh vrst komentarjev:

```python
”””Primerek
programske
kode
”””
i = 0 # začetna vrednost števca
```
