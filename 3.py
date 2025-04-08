class Prof:
    def _init_(self, nom, email, specialite):
        self._nom = nom
        self._email = email
        self._specialite = specialite

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    def _str_(self):
        return f"{self.nom} - {self._specialite}"


class Cours:
    def _init_(self, nom, masse_horaire, description, prof, duree):
        self.nom = nom
        self.masse_horaire = masse_horaire
        self.description = description
        self.prof = prof
        self._duree = duree  # 

    @property
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self, valeur):
        if valeur > 0:
            self._duree = valeur
        else:
            raise ValueError("La durée doit être positive.")

    def _eq_(self, other):
        return isinstance(other, Cours) and self.duree == other.duree

    def _lt_(self, other):
        return isinstance(other, Cours) and self.duree < other.duree

    def _gt_(self, other):
        return isinstance(other, Cours) and self.duree > other.duree

    def _str_(self):
        return f"Cours: {self.nom} - Durée: {self.duree} heures"


class CoursPrésentiel(Cours):
    def _init_(self, nom, masse_horaire, description, prof, duree, salle, equipements):
        super()._init_(nom, masse_horaire, description, prof, duree)
        self.salle = salle
        self.equipements = equipements

    def _str_(self):
        return f"{super()._str_()} (En salle: {self.salle})"


class CoursDistanciel(Cours):
    def _init_(self, nom, masse_horaire, description, prof, duree, lien_teams, documents, equipe):
        super()._init_(nom, masse_horaire, description, prof, duree)
        self.lien_teams = lien_teams
        self._documents = documents
        self.equipe = equipe

    def get_docs(self):
        return self._documents

    def set_docs(self, new_docs):
        self._documents = new_docs

    def _str_(self):
        return f"{super()._str_()} (En ligne: {self.lien_teams})"


prof1 = Prof("Dr. Ahmed", "ahmed@example.com", "Informatique")

cours1 = CoursPrésentiel("POO", 40, "Programmation Orientée Objet", prof1, 5, "Salle B1", ["Projecteur"])
cours2 = CoursDistanciel("Algorithmique", 30, "Cours en ligne", prof1, 4, "https://teams.com/algos", ["doc1.pdf", "doc2.pdf"], ["Dr. Ahmed"])

print(cours1)
print(cours2)
print("Cours1 > Cours2 ?", cours1 > cours2)

print("Documents initiaux:", cours2.get_docs())
cours2.set_docs(["nouveau_doc.pdf"])
print("Documents après modification:", cours2.get_docs())

print("Durée avant:", cours1.duree)
cours1.duree = 6
print("Durée après:", cours1.duree)