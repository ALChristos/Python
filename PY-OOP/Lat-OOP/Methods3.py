class Hero:
    JumlahHero = 0
    
    def __init__(self, NamaHero, HPHero, DeffHero, PowerHero):
        self.nama = NamaHero
        self.hp = HPHero
        self.deff = DeffHero
        self.power = PowerHero
        Hero.JumlahHero += 1
        
    """Method"""
    """Method tanpa return"""
    def sapa(self):
        print(f"Nama gweh {self.nama}")
        
    """Method dengan argumen"""
    def regen(self, regen):
        self.hp += regen
        print(f"HP Naik Menjadi: {self.hp}")
        
    """Method dengan return"""
    def GetHp(self):
        return self.hp
        
hero1 = Hero("Alucard", 100, 30, 30)
hero2 = Hero("Aldous", 100, 50, 45)

hero1.sapa()
hero2.regen(50)

print(hero2.GetHp())
print(hero1.GetHp())


        
    