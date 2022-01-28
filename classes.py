
class ITMsg:  # only for IT, since sectioned into two
    wsparcie = ['pgluszak', 'mwojcik', 'pdrzewiecki']
    systemy = ['jpiechnik', 'apiechnik', 'swyczalek', 'palbanowski']


class Team:
    def __init__(self, _id, name, kier, dn):
        self._id = _id
        self.name = name
        self.kier = kier
        self.dn = dn

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


class Teams:
    it = Team('mqayX5ocpq39kEwyC', 'IT', 'mdomanski', 'OU=ITPracownicy')
    wew = Team('HnS2sggDGCCwik3iz', 'oddzialchorobwewnetrznych', 'mzytkiewicz', 'OU=Wewnetrzny')
    place = Team('2mPqikSv6JhYm8Dc7', 'place', 'abronczyk', 'OU=Place')
    kadry = Team('CMKTnYtyGgGBeLer3', 'Kadry', 'mkaczmarek', 'OU=Kadry')
    ksiegowosc = Team('gFKkoAeaNs8rz5gji', 'ksiegowosc', 'rpiatek', 'OU=Ksiegowosc')
    dnm = Team('Gqvuu45Wg4HEhgbXH', 'NadzorMedyczny', 'jbrojewska', 'OU=NadzorMedyczny')
    dla = Team('n7dRyCDmZbNjNHYLM', 'logistycznoadministracyjny', 'dmajchrzak', 'OU=LogistykaAdministracja')
    inwentaryzacja = Team('5QsZK9s8YC6224H8b', 'inwentaryzacja', 'ddabrowski', 'OU=Inwentaryzacja')
    zaopatrzenie = Team('2fipuxzeMMXwcASgv', 'zaopatrzenie', 'rszumacher', 'OU=Zaopatrzenie')
    orgprawny = Team('uAdQPzEkzMCrdpD8S', 'organizacyjnoprawny', 'anowotarska', 'OU=Organizacja')
    # urologia = Team('YLC3SHMdT7H4LDuBw', 'urologia', '')
