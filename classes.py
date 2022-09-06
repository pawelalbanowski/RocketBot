class ITMsg:  # only for IT, since sectioned into two
    wsparcie = ['pgluszak', 'mwojcik', 'pdrzewiecki']
    systemy = ['jpiechnik', 'apiechnik', 'swyczalek', 'palbanowski']


class Team:
    def __init__(self, _id, name, kier, dn, header, category):
        self._id = _id
        self.name = name
        self.kier = kier
        self.dn = dn
        self.header = header
        self.category = category

    def __str__(self):
        return str(self.name)

    def getId(self):
        return self._id

    def getName(self):
        return self.name

    def getKier(self):
        return self.kier

    def getDn(self):
        return self.dn

    def getCategory(self):
        return self.category

    def getHeader(self):
        return self.header


class Teams:
    it = Team('mqayX5ocpq39kEwyC', 'IT', 'mdomanski', 'OU=ITPracownicy',
              'INFORMATYKA', 'administracja')

    wew = Team('HnS2sggDGCCwik3iz', 'oddzialchorobwewnetrznych', 'mzytkiewicz', 'OU=Wewnetrzny',
               'ODDZIAŁ CHORÓB WEWNĘTRZNYCH', 'szpital')

    place = Team('2mPqikSv6JhYm8Dc7', 'place', 'abronczyk', 'OU=Place',
                 'PŁACE', 'administracja')

    kadry = Team('CMKTnYtyGgGBeLer3', 'Kadry', 'mkaczmarek', 'OU=Kadry',
                 'KADRY', 'administracja')

    ksiegowosc = Team('gFKkoAeaNs8rz5gji', 'ksiegowosc', 'rpiatek', 'OU=Ksiegowosc',
                      'KSIĘGOWOŚĆ', 'administracja')

    dnm = Team('Gqvuu45Wg4HEhgbXH', 'NadzorMedyczny', 'jbrojewska', 'OU=NadzorMedyczny',
               'NADZÓR MEDYCZNY', 'administracja')

    dla = Team('n7dRyCDmZbNjNHYLM', 'logistycznoadministracyjny', 'dmajchrzak', 'OU=LogistykaAdministracja',
               'LOGISTYCZNO-ADMINISTRACYJNY', 'administracja')

    inwentaryzacja = Team('5QsZK9s8YC6224H8b', 'inwentaryzacja', 'ddabrowski', 'OU=Inwentaryzacja',
                          'INWENTARYZACJA', 'administracja')

    zaopatrzenie = Team('2fipuxzeMMXwcASgv', 'zaopatrzenie', 'rszumacher', 'OU=Zaopatrzenie',
                        'ZAOPATRZENIE', 'administracja')

    orgprawny = Team('uAdQPzEkzMCrdpD8S', 'organizacyjnoprawny', 'anowotarska', 'OU=Organizacja',
                     'ORGANIZACYJNO-PRAWNY', 'administracja')

    zamowienia = Team('MEckW2gTE8KDXM6GK', 'zamowienia', 'ajackowiak', 'OU=Zamowienia',
                      'ZAMÓWIENIA PUBLICZNE', 'administracja')

    dyrekcja = Team('8hhTD9nqMhXHBxGLx', 'dyrekcja', 'bgruszka', 'OU=Dyrekcja',
                    'DYREKCJA', 'administracja')

    akredytacja = Team('8hhTD9nqMhXHBxGLx', 'dyrekcja', 'vmatecka', 'OU=Akredytacja',
                       'AKREDYTACJA', 'administracja')

    techniczny = Team('nn4EPzpefbn6qGJNK', 'dzialtechniczny', 'lgalkowski', 'OU=DzialTechniczny',
                      'TECHNICZNO-EKSPLOATACYJNY', 'administracja')

    apteka = Team('bYRdJrXYLEEcfqj5j', 'apteka', 'dkurasz', 'OU=Apteka', 'APTEKA', 'szpital')

    iso = Team('dtsfQ5PwQBCW97uXN', 'iso', 'ekapecka', 'OU=ISO', 'ISO', 'administracja')

    inwestycje = Team('KCX9W59CMMjh7mepZ', 'inwestycje', 'pkachel', 'OU=Inwestycje',
                      'INWESTYCJE', 'administracja')

    epidemiologia = Team('uMjnyfuAP5pyimfEq', 'epidemiologia', '', 'OU=PielEpidemiologiczna',
                         'EPIDEMIOLOGIA', 'administracja')

    bhp = Team('kWauhZNtjLg2RgF7n', 'bhp', 'mmaciejewski', 'OU=Bhp',
               'BHP', 'administracja')

    fizykoterapia = Team('2epAzHvmKMeqWMvaw', 'fizykoterapia', 'edera', 'OU=Fizykoterapia',
                         'FIZYKOTERAPIA', 'szpital')

    labo = Team('baHp67Fm3RAoTt4br', 'laboratorium', 'mlisiecka', 'OU=Laboratorium',
                'LABORATORIUM', 'szpital')

    urologia = Team('t8dAMJB58F8dyBGJe', 'Urologia', 'aantczak', 'OU=Urologia',
                    'ODDZIAŁ UROLOGII', 'szpital')

    blok = Team('2mtM949XqhNw8wsfC', 'BlokOperacyjny', 'pszymczak', 'OU=BlokOperacyjny',
                'BLOK OPERACYJNY', 'szpital')

    chirkol = Team('DzrbjkDaeEh7rYNth', 'ChirurgiaKolorektalna', 'jkaron', 'OU=ChirurgiaOgolnaKolorektalna',
                   'ODDZIAŁ CHIRURGII OGÓLNEJ KOLOREKTALNEJ', 'szpital')

    chirlap = Team('jG8xJw3NDAfkGpQpu', 'ChirurgiaLaparaskopowa', 'phajkowicz', 'OU=ChirurgiaOgolnaLaparaskopowa',
                   'ODDZIAŁ CHIRURGII OGÓLNEJ LAPARASKOPOWEJ', 'szpital')

    chiruraz = Team('x3FhZ3GDwWLoAJQy5', 'ChirurgiaUrazowaOparzenia', 'pgrala', 'OU=ChirurgiaUrazowa',
                    'ODDZIAŁ CHIRURGII URAZOWEJ Z PODODDZIAŁEM OPARZEŃ', 'szpital')

    iom = Team('qW9PmYAMPBthgSQza', 'OAiIT', 'pszczesniewski', 'OU=IOM',
               'ODDZIAŁ ANESTEZJOLOGII I INTENSYWNEJ TERAPII', 'szpital')

    kch = Team('PCjxpE5j36sw6tydQ', 'Kardiochirurgia', 'pbugajski', 'OU=Kardiochirurgia',
               'ODDZIAŁ KARDIOCHIRURGII', 'szpital')

    kardiologia = Team('PkdCc9XC4NzKMQuMo', 'Kardiologia', 'mslomczynski', 'OU=Kardiologia',
                       'ODDZIAŁ KARDIOLOGII', 'szpital')

    neurochirurgia = Team('GfPnpYkPzpCnF3NFH', 'Neurochirurgia', 'bsokol', 'OU=Neurochirurgia',
                          'ODDZIAŁ NEUROCHIRURGII', 'szpital')

    neurologiaudary = Team('6mHucDbEJN24jpPRy', 'NeurologiaUdary', 'adruzdz', 'OU=Neurologia/Udary',
                           'ODDZIAŁ NEUROLOGII Z PODODDZIAŁEM UDAROWYM', 'szpital')

    okulistyka = Team('ZpzbXT3qNFvmkczYw', 'Okulistyka', 'kwaliszewski', 'OU=Okulistyka',
                      'ODDZIAŁ OKULISTYCZNY', 'szpital')

    ortopedia = Team('WT4rYEaMFdvtvqdb2', 'Ortopedia', 'lkubaszewski', 'OU=Ortopedia',
                     'ODDZIAŁ ORTOPEDII', 'szpital')

    reumatologia = Team('rEoHgcNihBDeb4myC', 'Reumatologia', 'pleszczynski', 'OU=Reumatologia',
                        'ODDZIAŁ REUMATOLOGII', 'szpital')

    sor = Team('NreJexzksYK8hHBr6', 'SOR', 'kmikolajczyk', 'OU=SOR',
               'SZPITALNY ODDZIAŁ RATUNKOWY', 'szpital')

    zakazny = Team('Ah9RmqeeHLwoGwCas', 'Zakazny', 'ilisewska', 'OU=Zakazny',
                   'ODDZIAŁ ZAKAŹNY', 'szpital')

    teams = [it, wew, place, kadry, ksiegowosc, dnm, dla, inwentaryzacja,
             zaopatrzenie, orgprawny, zamowienia, dyrekcja, akredytacja, techniczny, apteka,
             inwestycje, iso, epidemiologia, bhp, fizykoterapia, labo, urologia, blok, chirkol,
             chirlap, chiruraz, iom, kch, kardiologia, neurochirurgia, neurologiaudary,
             okulistyka, ortopedia, reumatologia, sor, zakazny]
