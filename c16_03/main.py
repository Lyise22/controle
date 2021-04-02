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

# Question 4.a
notes_eleve1 = (note1[2]+note2[2]+note3[2]+note4[2]+note5[2]+note6[2])
moyenne_eleve1 = notes_eleve1/6
print("Question4a : La moyenne de l'elève 1 est de",moyenne_eleve1)

# Question 4.b
notes_maths_eleve1 = (note1[2]+note3[2]+note6[2])
moyenne_maths_eleve1 = notes_maths_eleve1/3
print("Question4b : La moyenne en maths de l'elève 1 est de",moyenne_maths_eleve1)

# Question 4.c
def moyenne_tuples(notes, eleve = None, matiere = None):
  res = [item for item in notes if item[0] == eleve] if eleve is not None else notes
  res1 = [item1 for item1 in res if item1[1] == matiere] if matiere is not None else res
  print(res)
  print(res1)
  return sum([x[2] for x in res1])/(len(res1))

print("Question4c : La moyenne de l'élève 1 en maths est",moyenne_tuples(notes, "eleve1","math"))
print("Question4c : La moyenne de l'élève 1 en eco est",moyenne_tuples(notes, "eleve1","eco"))
print("Question4c : La moyenne de l'élève 2 en maths est",moyenne_tuples(notes, "eleve2","math"))

#### 
# Question 5.
n = []
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self = n.append(self)

  def afficher(self):
    return print('eleve :', self.eleve, ', matiere :', self.matiere, ', note :', self.valeur)
  
  # Question 6. 
  def __str__(self):
    return print('eleve :', self.eleve, ', matiere :', self.matiere, ', note :', self.valeur)

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

onotes = []
question5 = [n1 for n1 in notes if onotes.append(Note(n1[0],n1[1],n1[2]))]
print("Question5 : Afficher",question5)


print("Question6 : Affiche",Note.__str__(onote))
    
# Question 7.


# Question 8.
def moyenne_Notes(eleve = None, matiere = None):
  maliste = n
  b = []
  maliste1 = []
  for i in maliste :
    maliste1 = [x for x in maliste if x.eleve == eleve or eleve == None]
    maliste_matiere = [x for x in maliste1 if x.matiere == matiere or matiere == None]
    b = [x.valeur for x in maliste_matiere]
    moy = sum(b)/len(b)
    return moy

print("Question8 : La moyenne des Notes est", moyenne_Notes())

###

class Demo:
  classattr = 'defaut'
  def __init__(self, a):
    self.a = a

demo1 = Demo(1)
demo2 = Demo(2)
demo12 = Demo(12)

print(demo1.a)
print(demo2.a)
print(demo12.a)

print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)
print(demo12.classattr)

Demo.classattr = 23

print(demo1.classattr)
print(demo2.classattr)

demo1.classattr = -1

print(Demo.classattr)
print(demo1.classattr)

demo2.classattr = 22
print(demo2.classattr)

Demo.classattr = 14

demo12.classattr = 12
print(demo12.classattr)


# Question 9.
aa = []
class instances:
  instances = []
  classattr = 'defaut'

  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self.instances.append(self)

  def __init__(self, a):
    self.a = a
  
  @classmethod
  def default_len(cls):
    return len(cls.classattr)

# Question 10
  @classmethod
  def vider(cls):
    cls.instances = []
  

print("Question9 : ", instances.default_len())
print("Question10 : ", instances.vider())


# Question 11


# Question 12





