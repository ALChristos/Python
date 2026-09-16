class Hero:
    def __init__(self, NamaHero, Health, Defence): # <-- __init__ adalah Constructor
        self.nama = NamaHero # <-- Atribut
        self.hp = Health
        self.deff = Defence
        
hero1 = Hero("Alucard", 100, 80) # <-- Object
hero2 = Hero("Aldous", 150, 100)

print(hero1.nama)
print(hero1.__dict__)
print(hero2.__dict__)