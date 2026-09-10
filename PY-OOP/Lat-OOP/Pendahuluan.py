"""Programing Paradigma:
1. Struktural --> Prosedural --> Dieksekusi berdasarkan urutan
2. Object --> Oriented Programing"""

"""Cara Membuat Class, Objek dan Atribut"""
class Hero: # <-- Class
    pass


hero1 = Hero() # <-- Object
hero2 = Hero()

hero1.name = "Alucard" #<-- Atribut
hero1.hp = 100

hero2.name = "Aldous"
hero2.hp = 150

print(hero1.__dict__)
print(hero2.name)