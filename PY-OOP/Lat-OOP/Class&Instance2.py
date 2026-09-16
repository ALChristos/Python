"""Class dan Instance Variable"""
class Hero:
    jumlah = 0 # <-- Class variabel/Static Class
    def __init__(self, NamaHero, Health, Defence): # <-- __init__ adalah Constructor
        #Instance Variable --> Sebagai variabel contoh untuk object
        self.nama = NamaHero 
        self.hp = Health
        self.deff = Defence
        Hero.jumlah += 1
        print(f"Membuat Hero dengan Nama {NamaHero}")
        
hero1 = Hero("Alucard", 100, 80) # <-- Object
print(Hero.jumlah)
hero2 = Hero("Aldous", 150, 100)
print(Hero.jumlah)

