import math

def main():
    while True:
        (x1, y1) = eval(input('Vnesi koordinati središča prve krožnice x1, y1: '))
        r1 = eval(input('Vnesi polmer prve krožnice r1: '))
        (x2, y2) = eval(input('Vnesi koordinati središča druge krožnice x2, y2: '))
        r2 = eval(input('Vnesi polmer druge krožnice r2: '))

        dx = x2 - x1
        dy = y2 - y1
        d = math.sqrt(dx**2 + dy**2)
        
        pozitivniPolmer = (r1 and r2 != 0)
        nicSkupnihTock = (r1 + r2 < d) or (abs(r1 - r2) > d)
        brezSredisca = (d != 0)
        sSrediscem = (d == 0)
        enaSkupnaTocka = (r1 + r2 == d) or (abs(r1 - r2) == d)
        dveSkupniTocki = (r1 + r2 > d) and (abs(r1 - r2) < d)
        vseSkupneTocke = (d == 0) and (r1 == r2)

        if pozitivniPolmer:
            if nicSkupnihTock:
                if brezSredisca:
                    print('Krožnici nimata nobene skupne točke, niti skupnega središča.')
                elif sSrediscem:
                    print('Krožnici nimata nobene skupne točke, imata pa skupno središče - sta koncentrični.')
            elif enaSkupnaTocka:
                print('Krožnici imata eno skupno točko - se dotikata.')
            elif dveSkupniTocki:
                print('Krožnici imata dve skupni točki - se sekata.')
            elif vseSkupneTocke:
                print('Krožnici imata vse skupne točke - se prekrivata.')
        else:
            print('Vneseni podatki ne določajo krožnic!')

        ponovi = input('Ponovim preverjanje lege krožnic? Za pritrdilen odgovor pritisni tipko d. ')
        if ponovi in ('d', 'D'):
            continue
        else:
            break

if __name__ == "__main__":
    main()