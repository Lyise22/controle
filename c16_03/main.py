note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

# 4.a
notes_eleve1 = (note1[2]+note2[2]+note3[2]+note4[2]+note5[2]+note6[2])
moyenne_eleve1 = notes_eleve1/6
print("La moyenne de l'elève 1 est de",moyenne_eleve1)

# 4.b
notes_maths_eleve1 = (note1[2]+note3[2]+note6[2])
moyenne_maths_eleve1 = notes_maths_eleve1/3
print("La moyenne en maths de l'elève 1 est de",moyenne_maths_eleve1)

# 4.c
def moyenne_tuples(notes, eleve, matiere):
  res = [item for item in notes if item[0] == eleve]
  res1 = [item for item in notes if item[1] == matiere]
  print(res)
  print(res1)
  return sum([x[2] for x in res1])/(len(res1))

print("La moyenne 1 est",moyenne_tuples(notes, "eleve1","math"))
print("La moyenne 2 est",moyenne_tuples(notes, "eleve1","eco"))
print("La moyenne 3 est",moyenne_tuples(notes, "eleve2","math"))

#### 
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

def __str__(self):
  return print(Note) #ce que vous voulez afficher"


