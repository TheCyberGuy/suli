import copy as cp


class Boxolo:
    def __init__(self, name, nationality, weight, weight_loss, max_loss):
        self.name = name
        self.nationality = nationality
        self.weight = weight
        self.weight_loss = weight_loss
        self.max_loss = max_loss

    def sulycsoport(instance):
        if instance.weight > 0 and instance.weight <= kategoriak[0]:
            print(f'{instance.name} 0-tol {kategoriak[0]}-ig harcol')
        elif instance.weight > kategoriak[0] and instance.weight <= kategoriak[1]:
            print(f'{instance.name} {kategoriak[0]} {kategoriak[1]}-ig harcol')
        elif instance.weight > kategoriak[1] and instance.weight <= kategoriak[2]:
            print(
                f'{instance.name} {kategoriak[1]}tol {kategoriak[2]}-ig harcol')
        elif instance.weight > kategoriak[2] and instance.weight <= kategoriak[3]:
            print(f'{instance.name} {kategoriak[2]} {kategoriak[3]}-ig harcol')
        elif instance.weight > kategoriak[3] and instance.weight <= kategoriak[4]:
            print(f'{instance.name} {kategoriak[3]} {kategoriak[4]}-ig harcol')
        elif instance.weight > kategoriak[4] and instance.weight <= kategoriak[5]:
            print(f'{instance.name} {kategoriak[4]} {kategoriak[5]}-ig harcol')

    def kategorizalas(instance, dest):
        if instance.weight > 0 and instance.weight <= kategoriak[0]:
            dest['pehely'].append(instance)
        elif instance.weight > kategoriak[0] and instance.weight <= kategoriak[1]:
            dest['konnyu'].append(instance)
        elif instance.weight > kategoriak[1] and instance.weight <= kategoriak[2]:
            dest['atlag'].append(instance)
        elif instance.weight > kategoriak[2] and instance.weight <= kategoriak[3]:
            dest['atlag-feletti'].append(instance)
        elif instance.weight > kategoriak[3] and instance.weight <= kategoriak[4]:
            dest['nehez'].append(instance)
        elif instance.weight > kategoriak[4] and instance.weight <= kategoriak[5]:
            dest['extra-nehez'].append(instance)


kategoriak = [52, 57, 63, 71, 79, 91]

boxolok = []

with open('boxolok.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.split(',')
        name = data[0]
        nationality = data[1]
        weight = int(data[2])
        weight_loss = int(data[3])
        max_loss = int(data[4].strip())
        boxolok.append(Boxolo(name=name, nationality=nationality,
                       weight=weight, weight_loss=weight_loss, max_loss=max_loss))


magyarok = []


def feladat_1():
    print('1. feladat:')
    for boxolo in boxolok:
        if boxolo.nationality == 'hu':
            magyarok.append(boxolo)
    print(f'osszesen {len(magyarok)} boxolo van')


def feladat_2():
    print('\n2. feladat:')
    magyar_suly = []
    for versenzyo in magyarok:
        magyar_suly.append(versenzyo.weight)
    print(
        f'magyar versenyzok atlag sulya: {sum(magyar_suly) / len(magyar_suly)}kg')


def feladat_3():
    print('\n3. feladat:')
    legnehezebb = boxolok[0]
    for i in boxolok:
        if i.weight > legnehezebb.weight:
            legnehezebb = i
    print(
        f'A legnehezebb boxolo {legnehezebb.name}, akinek a sulya: {legnehezebb.weight}kg')


def feladat_4():
    print('\n4. feladat:')
    # name = input('adja meg az egyik boxolo nevet: ')
    #! change back the test name to an input like above
    name = 'Donald Duck'
    for i in boxolok:
        if i.name == name:
            i.sulycsoport()


sulycsoport = {"pehely": [], 'konnyu': [], 'atlag': [],
               'atlag-feletti': [], 'nehez': [], 'extra-nehez': []}


def feladat_5():
    print('\n5. feladat')
    for i in boxolok:
        i.kategorizalas(dest=sulycsoport)
    print(f"""a kulonbozo sulycsoportban ennyien versenyeznek:
pehely suly: {len(sulycsoport["pehely"])}
konnyu suly: {len(sulycsoport["konnyu"])}
atlag suly: {len(sulycsoport['atlag'])}
atlag-feletti suly: {len(sulycsoport['atlag-feletti'])}
nehez suly: {len(sulycsoport['nehez'])}
extra-nehez suly: {len(sulycsoport['extra-nehez'])}
    """)


def feladat_6():
    print('\n6. feladat')
    print('a kulonbozo sulycsoportban ok versenyeznek')
    print(
        f'pehely suly: {" ".join([i.name for i in sulycsoport["pehely"]]) if len(sulycsoport["pehely"]) != 0 else "ures a suly csoport"}')
    print(
        f'konnyu suly: {", ".join([i.name for i in sulycsoport["konnyu"]]) if len(sulycsoport["konnyu"]) != 0 else "ures a suly csoport"}')
    print(
        f'atlag suly: {", ".join([i.name for i in sulycsoport["atlag"]]) if len(sulycsoport["atlag"]) != 0 else "ures a suly csoport"}')
    print(
        f'atlag-feletti suly: {", ".join([i.name for i in sulycsoport["atlag-feletti"]]) if len(sulycsoport["atlag-feletti"]) != 0 else "ures a suly csoport"}')
    print(
        f'nehez suly: {", ".join([i.name for i in sulycsoport["nehez"]]) if len(sulycsoport["nehez"]) != 0 else "ures a suly csoport"}')
    print(
        f'extra-nehez suly: {", ".join([i.name for i in sulycsoport["extra-nehez"]]) if len(sulycsoport["extra-nehez"]) != 0 else "ures a suly csoport"}')


def feladat_7():
    print('\n 7. feladat')
    egyeduliek = []
    for i in sulycsoport:
        if len(i) == 1:
            egyeduliek.append(i)
    if len(egyeduliek) == 0:
        print('nincs olyan sulycsoporot ahol egy ember indulna csak')
    else:
        print(
            f'van olyan suly csoport ahol csak egy ember indul es ez(ek) az(ok) a sulycsoprt(ok): {", ".join(egyeduliek)}')


def feladat_8():
    print('\n8. feladat')
    only_HU = []
    for suly in sulycsoport:
        versenyzok = []
        # zaj szures
        if len(sulycsoport[suly]) == 0:
            continue
        else:
            for versenyzo in sulycsoport[suly]:
                versenyzok.append(versenyzo.nationality)
            versenzyok_copy = versenyzok.copy()
            for k in range(len(versenzyok_copy)-1):
                versenzyok_copy[k] = 'hu'
            if versenyzok == versenzyok_copy:
                only_HU.append(suly)
    print(f'a {"".join(only_HU)} sulycsoportban garantalt a magyar aranyerem, mivel csak magyarok indulnak')


def feladat_9():
    print('\n9. feladat')
    angolok = []
    azonos = []
    for i in boxolok:
        if i.nationality == 'en':
            angolok.append(i)
    for i in range(len(angolok)-1):
        for j in range(len(angolok)-1):
            if angolok[i].weight == angolok[j].weight and angolok[i].name != angolok[j].name:
                azonos.append([angolok[i].name, angolok[j].name])
    print(azonos if len(azonos) > 0 else 'nincs azonos sulyu angol boxolo')


def feladat_10():
    print('\n10. feladat')
    merkozesek = []
    for i in sulycsoport['extra-nehez']:
        for j in sulycsoport['extra-nehez']:
            if i.name != j.name:
                merkozesek.append([i.name, j.name])
    for i in merkozesek:
        print(' vs. '.join(i))


sulycsoport_new = {"pehely": [], 'konnyu': [], 'atlag': [],
                   'atlag-feletti': [], 'nehez': [], 'extra-nehez': []}


def feladat_11(napok):
    print('\n11. feladat')
    # * deepcopy-t kell haszanlni mivel a sima = illetve az array.copy() metodus ugyaz azt a memroia cimet modifikaljha a memoriaban igy az eredeti tombot is modifikalja
    boxolok_fogyas = cp.deepcopy(boxolok)

    for i in range(len(boxolok_fogyas)):
        loss = 0
        print(boxolok[i].name)
        for j in range(napok + 1):
            loss += boxolok[i].weight_loss
            if loss == boxolok[i].max_loss:
                boxolok_fogyas[i].weight -= boxolok[i].weight_loss
                break
            else:
                boxolok_fogyas[i].weight -= boxolok[i].weight_loss
    for i in range(len(boxolok) - 1):
        print(
            f'\n{boxolok[i].name}: {boxolok[i].weight} -> {boxolok_fogyas[i].weight}')
    for j in boxolok_fogyas:
        j.kategorizalas(dest=sulycsoport_new)

    print('old\n')
    for keys in sulycsoport:
        if len(sulycsoport[keys]) != 0:
            print([i.name for i in sulycsoport[keys]])
    print('new:\n')
    for keys in sulycsoport_new:
        if len(sulycsoport_new[keys]) != 0:
            print([i.name for i in sulycsoport_new[keys]])


feladat_1()
feladat_2()
feladat_3()
feladat_4()
feladat_5()
feladat_6()
feladat_7()
feladat_8()
feladat_9()
feladat_10()
feladat_11(3)
